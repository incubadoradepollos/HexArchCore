from setuptools import setup, find_packages

setup(
    name="hexarch_core",
    version="0.0.1",
    author="Jose Manuel Herera",
    author_email="jmherrera76@gmail.com",
    description="Core for hexarch_core",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/incubadoradepollos/HexArchCore",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.4",
    install_requires=[
        "requests",
        "dependency_injector",
        "pydantic"
    ],
)
