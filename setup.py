from setuptools import setup,find_packages

setup(
    name="csvgraph",
    version="0.8",
    description=("Use Matplotlib to plot lines from a CSV file and create a"
                 "PNG image file from the figure."),
    author="Russell Miller",
    install_requires=['argparse', 'matplotlib'],
    packages=find_packages(),
    entry_points=
        """
        [console_scripts]
        csvgraph = csvgraph.main:main
        """
    )
