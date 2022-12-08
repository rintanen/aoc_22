import os
from distutils.core import setup

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name='pr-aoc-2022',
    python_requires='>=3.0',
    install_requires=required
)
