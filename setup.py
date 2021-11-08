import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="CSV Processing",
    version="0.0.1",
    author="Laya Rabasa",
    author_email='layadelcarmen@gmail.com',
    description="",
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-clarity",
            'mock;python_version<"3.3"']
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "PyYAML",
        "Pandas"
    ],
    entry_points={
        'console_scripts': [
            'csv-processing=csvprocessing.main:main',
        ],
    },
    url="https://github.com/layadelcarmen/tinysol",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)