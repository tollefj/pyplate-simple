import argparse
from typing import Any, Dict


def parse_args() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(
        description="A description of your application."
    )

    parser.add_argument("-i", "--input", type=str, help="Input file path")
    parser.add_argument("-o", "--output", type=str, help="Output file path")

    # Add more arguments as needed

    return vars(parser.parse_args())
