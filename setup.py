import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plc_nsi_algo",
    version="0.0.1",
    author="efloti",
    author_email="efloti@gmail.com",
    description="Algorithmique en terminale NSI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/efloti/plc_nsi_algo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)