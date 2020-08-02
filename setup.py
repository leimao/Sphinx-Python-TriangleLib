import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trianglelib", # Replace with your own username
    version="1.2",
    author="Brandon Rhodes, Lei Mao",
    author_email="brandon@rhodesmill.org, dukeleimao@gmail.com",
    description="A small triangle library for Sphinx tutorial.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)