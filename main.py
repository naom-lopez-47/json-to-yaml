"""JSON to YAML — Convert JSON files to YAML and keep key order when you ask."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='json_to_yaml',
        description='Convert JSON files to YAML and keep key order when you ask.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('JSON to YAML')
    print('Config in YAML, source still JSON.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
