import os
import sys
from pathlib import Path

sys.path.append(os.getcwd())  # noqa: PTH109
sys.path.append(
    Path(os.path.dirname(os.path.realpath(__file__))).parent.absolute().__str__(),  # noqa: PTH120
)

from mp2.program import program

if __name__ == "__main__":
    program()
