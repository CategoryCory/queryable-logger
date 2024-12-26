from setuptools import setup, find_packages


setup(
    name="queryable_logger",
    version="0.1.0",
    author="Cory Coward",
    author_email="corydottech@gmail.com",
    url="https://github.com/CategoryCory/queryable_logger",
    description="A queryable logging library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=[],
    extras_require={
        "dev": [
            "mypy",
            "ruff",
        ],
        "test": [
            "pytest",
        ],
    },
)
