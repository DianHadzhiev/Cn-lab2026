from argparse import Namespace, ArgumentParser


def parse_arguments() -> Namespace:
    """
    Parse command line arguments for the http server.
    The three valid options are:
        --address: The host to listen at. Default is "0.0.0.0"
        --port: The port to listen at. Default is 8000
        --directory: The directory to serve. Default is "data"
    :return: The parsed arguments in a Namespace object.
    """

    parser: ArgumentParser = ArgumentParser(
        prog="python -m a5_http_server",
        description="A5 HTTP Server assignment for the VU Computer Networks course.",
        epilog="Authors: Your group name"
    )
    parser.add_argument("-a", "--address",
                        type=str, help="Set server address", default="0.0.0.0")
    parser.add_argument("-p", "--port",
                        type=int, help="Set server port", default=8000)
    parser.add_argument("-d", "--directory",
                        type=str, help="Set the directory to serve", default="a5_http_server/public")

    return parser.parse_args()


def main() -> None:
    parser: Namespace = parse_arguments()
    port: int = parser.port
    host: str = parser.address
    base_directory: str = parser.directory

    # Your implementation here


if __name__ == "__main__":
    main()
