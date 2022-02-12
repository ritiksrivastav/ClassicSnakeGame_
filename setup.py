import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="classic-snake-game",
    version="1.0.0",
    description="Play The Classic Snake Game.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ritiksrivastav/ClassicSnakeGame_",
    author="Ritik Srivastav",
    author_email="srivastava.ritik998@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["square"],
    include_package_data=True,
    install_requires=[],
)
