from args import parse_args
from src.utils import datetime_util, logging_util, pprint


def main():
    args = parse_args()
    timestamp = datetime_util.get_current_timestamp()
    logger = logging_util.setup_logging(log_dir="logs")

    logger.info(f"Application started at {timestamp}")
    logger.info(f"Arguments: {args}")

    text = "Hello, Python project!"
    style = "bold yellow"
    pprint.print_colored(text, style)
    pprint.newline(times=2)

    data = [("1", "Alice", "10"), ("2", "Bob", "12"), ("3", "Charlie", "9")]
    columns = ["ID", "Name", "Score"]
    pprint.print_table(data, columns, title="Sample Table")


if __name__ == "__main__":
    main()
