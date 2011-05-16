from setuptools import setup,find_packages

setup(
    name="csvgraph",
    version="0.8",
    description="Plot pairs of columns from a CSV file to make a PNG.",
    install_requires=['argparse', 'matplotlib'],
    packages=find_packages(),
    entry_points=
        """
        [console_scripts]
        csvgraph = csvgraph.main:main
        """
    )
