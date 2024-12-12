#!/usr/bin/env python3
"""Invalid map executable returns non-zero with an error message."""

import sys


# Avoid error on executable check which has an empty string input
input_lines_n = sum(1 for _ in sys.stdin)
if input_lines_n > 1:
    sys.stdout.write("Map error message to stdout\n")
    sys.stderr.write("Map error message to stderr\n")
    sys.exit(1)