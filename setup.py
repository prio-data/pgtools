
import setuptools

with open("README.md") as f:
    long_description=f.read()

setuptools.setup(
        name = "pgtools",
        version = "0.0.1",
        author = "Peder G. Landsverk",
        author_email = "pglandsverk@gmail.com",
        description = "Toolset for working with PRIO-GRID data",
        long_description = long_description,
        long_description_content_type="text/markdown",
        url = "https://www.github.com/prio-data/pgtools",
        packages = setuptools.find_packages(),
        scripts=["bin/pgdl"],
        python_requires=">=3.7",
        install_requires=[
            "numpy==1.19.2"
        ])