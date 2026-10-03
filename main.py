"""Cassette Beasts Desktop — A local helper for Cassette Beasts tape folders, party notes, and New Wirral photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='cassette_beasts_desktop',
        description='A local helper for Cassette Beasts tape folders, party notes, and New Wirral photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Cassette Beasts Desktop')
    print('Keep the tape deck on disk before a story beat.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
