"""
System tests for the command line interface.
"""
import subprocess
import filecmp
from utils import TESTDATA_DIR


def test_version():
    """Verify --version flag."""
    result = subprocess.run(
        ["madoop", "--version"],
        stdout=subprocess.PIPE,
        check=True,
    )
    output = result.stdout.decode("utf-8")
    assert "Fake Hadoop" in output
    assert "by Andrew DeOrio <awdeorio@umich.edu>" in output


def test_help():
    """Verify --help flag."""
    result = subprocess.run(
        ["madoop", "--help"],
        stdout=subprocess.PIPE,
        check=True,
    )
    output = result.stdout.decode("utf-8")
    assert "usage" in output


def test_simple(tmpdir):
    """Run a simple MapReduce job and verify the output."""
    with tmpdir.as_cwd():
        subprocess.run(
            [
                "madoop",
                "-input", str(TESTDATA_DIR/"word_count/input"),
                "-output", "output",
                "-mapper", str(TESTDATA_DIR/"word_count/map.py"),
                "-reducer", str(TESTDATA_DIR/"word_count/reduce.py"),
            ],
            stdout=subprocess.PIPE,
            check=True,
        )
    for basename in ["part-00000", "part-00001", "part-00002", "part-00003"]:
        assert filecmp.cmp(
            tmpdir/"output"/basename,
            TESTDATA_DIR/"word_count/correct"/basename,
            shallow=False,
        )
