import argparse
import datetime
import importlib.metadata
import sys
from pathlib import Path

from jrsync import core


class DataParser(argparse.Action):
    def __call__(self, parser, namespace, values, option_strings=None):
        setattr(namespace, self.dest, datetime.datetime.strptime(values, '%Y%m%d'))


def get_args(raw_args=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Jrsync CLI")

    parser.add_argument(
        "config", type=Path, help="Json file containing sync information"
    )
    parser.add_argument(
        "production_day", action=DataParser, help="Bulletin day in the format YYYYMMDD"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow to run multiple instance in the same moment",
    )
    if "-V" in sys.argv or "--version" in sys.argv:
        print(importlib.metadata.version("rift"))
        sys.exit(0)
    return parser.parse_args(raw_args)


if __name__ == "__main__":
    args: argparse.Namespace = get_args()
    core.execute(**vars(args))
