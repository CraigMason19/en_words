from setuptools import setup, find_packages

setup(
    name="en_words",
    version="1.1.2",
    packages=find_packages(),
    author="Craig Mason",
    description="A package for working with English dictionaries and finding words and anagrams.",
    url="https://github.com/CraigMason19/en_words",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_data={"en_words": ["en_words.txt", "en_words_sorted.txt"]},
    include_package_data=True,
)