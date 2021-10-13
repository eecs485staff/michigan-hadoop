"""
System tests for the command line interface.
"""

import madoop
import subprocess


def test_cli():
    """Dummy example test."""
    result = subprocess.run([madoop.__name__, '--version'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    assert("Andrew DeOrio" in output)

    result = subprocess.run([madoop.__name__, '--help'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    assert("usage" in output)
