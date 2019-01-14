import os

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

cli_path = "cli-tools/"
cli_files = []
for path, subdirs, files in os.walk(cli_path):
    for f in files:
        if "." not in f:
            cli_files.append(os.path.join(path, f))

setup(
    name="msw",
    version="0.1.1",
    description="An awesome surf forecast visualisation",
    author="HowardRiddiough",
    long_description=long_description,
    author_email="howardriddiough@gmail.com",
    packages=["msw"],
    install_requires=[
        "folium==0.7.0",
        "matplotlib==2.2.3",
        "numpy==1.15.0",
        "pandas==0.23.4",
        "tqdm==4.26.0"
    ],
    extras_require={
        "test": {"flake8==3.5.0", "pep8-naming==0.7.0", "pytest==3.7.0", "pytest-cov"},
    },
    scripts=cli_files,
)
