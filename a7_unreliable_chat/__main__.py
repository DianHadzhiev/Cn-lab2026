from argparse import Namespace, ArgumentParser


def parse_arguments() -> Namespace:
    """
    Parse command line arguments for the unreliable chat client.
    The three valid options are:
        --address: The host to connect to. Default is "0.0.0.0"
        --port: The port to connect to. Default is 6778
    :return: The parsed arguments in a Namespace object.
    """

    parser: ArgumentParser = ArgumentParser(
        prog="python -m a7_unreliable_chat",
        description="A7 Unreliable Chat Client assignment for the VU Computer Networks course.",
        epilog="Authors: Your group name"
    )
    parser.add_argument("-a", "--address",
                        type=str, help="Set server address", default="0.0.0.0")
    parser.add_argument("-p", "--port",
                        type=int, help="Set server port", default=6778)

    return parser.parse_args()


def main() -> None:
    pass


if __name__ == "__main__":
    main()
