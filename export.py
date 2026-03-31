import os
from argparse import Namespace, ArgumentParser
from zipfile import ZipFile


def parse_arguments() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="python export.py",
        description="Export assignment for submission in CodeGrade.",
    )
    parser.add_argument(
        "assignment", type=str, help="Assignment name",
        choices=[f"a{i}" for i in [1, 3, 5, 6, 7]]
    )
    return parser.parse_args()


ASSIGNMENT_MAP: dict[str, str] = {
    "a1": "a1_chat_client",
    "a3": "a3_chat_server",
    "a5": "a5_http_server",
    "a6": "a6_dns_server",
    "a7": "a7_unreliable_chat",
    "a8": "a8_game"
}


def main() -> None:
    global ASSIGNMENT_MAP
    args: Namespace = parse_arguments()
    assert args.assignment in ASSIGNMENT_MAP

    assignment_dir: str = ASSIGNMENT_MAP[args.assignment]
    with ZipFile(f"{args.assignment}.zip", "w") as zipf:
        for root, _, files in os.walk(assignment_dir):
            for file in files:
                if ".pyc" in file or "__pycache__" in root: continue
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path))


if __name__ == "__main__":
    main()
