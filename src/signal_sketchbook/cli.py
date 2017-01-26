import argparse
from signal_sketchbook.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Signal plotting and quick analysis notebook replacement built with standard Python only.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
