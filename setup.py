from setuptools import setup,find_packages

setup(
    name="csvgraph",
    version="0.1",
    description="Plot pairs of columns from a CSV file to make a PNG.",
    packages=find_packages(),
    entry_points=
        """
        [console_scripts]
        csvgraph = csvgraph.main:main
        """
    )
