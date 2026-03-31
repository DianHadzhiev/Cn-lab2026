from argparse import Namespace, ArgumentParser


def parse_arguments() -> Namespace:
    """
    Parse command line arguments for the chat server.
    The two valid options are:
        --address: The host to listen at. Default is "0.0.0.0"
        --port: The port to listen at. Default is 5378
    :return: The parsed arguments in a Namespace object.
    """

    parser: ArgumentParser = ArgumentParser(
        prog="python -m a3_chat_server",
        description="A3 Chat Server assignment for the VU Computer Networks course.",
        epilog="Authors: Your group name"
    )
    parser.add_argument("-a", "--address",
                      type=str, help="Set server address", default="0.0.0.0")
    parser.add_argument("-p", "--port",
                      type=int, help="Set server port", default=5378)
    return parser.parse_args()


# Execute using `python -m a3_chat_server`
def main() -> None:
    args: Namespace = parse_arguments()
    port: int = args.port
    host: str = args.address

    # TODO: Your implementation here


if __name__ == "__main__":
    main()
