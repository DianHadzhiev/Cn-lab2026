from argparse import Namespace, ArgumentParser
import socket
import select
import sys
import threading
import queue

def parse_arguments() -> Namespace:
    """
    Parse command line arguments for the chat client.
    The two valid options are:
        --address: The host to connect to. Default is "0.0.0.0"
        --port: The port to connect to. Default is 5378
    :return: The parsed arguments in a Namespace object.
    """
    parser: ArgumentParser = ArgumentParser(
        prog="python -m a1_chat_client",
        description="A1 Chat Client assignment for the VU Computer Networks course.",
        epilog="Authors: Your group name"
    )
    parser.add_argument("-a", "--address",
                      type=str, help="Set server address", default="0.0.0.0")
    parser.add_argument("-p", "--port",
                      type=int, help="Set server port", default=5378)
    return parser.parse_args()

# Execute using `python -m a1_chat_client`
def main() -> None:
    args: Namespace = parse_arguments()
    port: int = args.port
    host: str = args.address

    # TODO: Your implementation here
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    input_queue = queue.Queue()
    threading.Thread(target=stdin_reader, args=(input_queue,), daemon=True).start()
    buffer = login(sock, input_queue)
    if buffer is None:
        return

    while True:
        readable, _, _ = select.select([sock], [], [], 0.1)

        if readable:
            line, buffer = receive_message(sock, buffer)
            if line:
                handle_message(line)
        try:
            user_input = input_queue.get_nowait()
            if user_input == "!quit":
                sock.close()
                return
            elif user_input == "!who":
                send_message(sock, "LIST\n")
            elif user_input.startswith('@'):
                parts = user_input.split(' ', 1)
                destination = parts[0][1:]
                message = parts[1] if len(parts) == 2 else ""
                if destination:
                    send_message(sock, f"SEND {destination} {message}\n")
        except queue.Empty:
            pass

def send_message(sock, message):
    data = message.encode("utf-8")
    total = 0
    while total < len(data):
        sent = sock.send(data[total:])
        total += sent

def receive_message(sock, buffer):
    while b'\n' not in buffer:
        data = sock.recv(1024)
        if not data:
            break
        buffer += data
    if b'\n' in buffer:
        line, buffer = buffer.split(b'\n', 1)
        return line.decode('utf-8', errors="replace"), buffer
    else:
        return "", buffer

def login(sock, input_queue):
    buffer = b""
    print("Welcome to Chat Client. Enter your login: ")
    name = None
    logged_in = False

    while True:
        readable, _, _ = select.select([sock], [], [], 0.1)
        if readable:
            response, buffer = receive_message(sock, buffer)
            if response:
                if response == f"HELLO {name}":
                    print(f"Successfully logged in as {name}!")
                    logged_in = True
                elif response == "IN-USE":
                    print(f"Cannot log in as {name}. That username is already in use.")
                    name = None
                elif response == "BUSY":
                    print("Cannot log in. The server is full!")
                    sock.close()
                    return None
                elif response in ("BAD-RQST-BODY", "BAD-RQST-HDR"):
                    print(f"Cannot log in as {name}. That username contains disallowed characters.")
                    name = None
        try:
            line = input_queue.get_nowait()
            if line =="!quit":
                sock.close()
                return None
            if line:
                name = line
                send_message(sock, f"HELLO-FROM {name}\n")
        except queue.Empty:
            pass
        if logged_in:
            while b'\n' in buffer:
                line, buffer = buffer.split(b'\n', 1)
                handle_message(line.decode('utf-8', errors="replace"))
            return buffer
        
def stdin_reader(input_queue):
    for line in sys.stdin:
        input_queue.put(line.strip())        

def handle_message(line):
    if line.startswith("DELIVERY "):
        parts = line.split(' ', 2)
        sender = parts[1]
        if len(parts) > 2:
            message = parts[2]
        else:
            message = ""
        print(f"From {sender}: {message}")
    elif line.startswith("LIST-OK "):
        names = line[len("LIST-OK "):].split(',')
        names = [n.strip() for n in names if n.strip()]
        print(f"There are {len(names)} online users:")
        for n in names:
            print(n)
    elif line == "SEND-OK":
        print("The message was sent successfully")
    elif line == "BAD-DEST-USER":
        print("The destination user does not exist")
    elif line == "BAD-RQST-HDR":
        print("Error: Unknown issue in previous message header.")
    elif line == "BAD-RQST-BODY":
        print("Error: Unknown issue in previous message body.")

if __name__ == "__main__":
    main()