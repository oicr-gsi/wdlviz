#!/usr/bin/env python3
"""
Render a DOT file in Python using Graphviz
"""
import sys
import argparse
import graphviz


def main(args=None):
    # read command-line arguments
    parser = argparse.ArgumentParser(
        description="Render a dot file using graphviz"
    )
    parser.add_argument(
        "dot", 
        metavar="FILE",
        help="DOT file (- for standard input)"
    )

    parser.add_argument(
        "format",
        metavar="FORMAT",
        type=str,
        help="Format for output",
    )
    args = parser.parse_args(args if args is not None else sys.argv[1:])

    # load DOT file
    dot = args.dot if args.dot != "-" else "/dev/stdin"

    # visualize workflow
    graphviz.render('dot', args.format, dot).replace('\\', '/')

if __name__ == "__main__":
    main()