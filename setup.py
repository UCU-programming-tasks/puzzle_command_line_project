import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puzzle-dyaroshevych",
    version="0.0.1",
    author="Dmytro Yaroshevych",
    author_email="dyaroshevych@gmail.com",
    description="A module for validating the board of symbols.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dyaroshevych/puzzle_command_line_project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
