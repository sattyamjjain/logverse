import setuptools

with open("README.md") as readme_file:
    README = readme_file.read()

with open("HISTORY.md") as history_file:
    HISTORY = history_file.read()

with open("requirements.txt") as f:
    reqs = f.read().split("\n")

setuptools.setup(
    name="logverse",
    version="0.0.1",
    description="Tool for analyze logs using ChatGPT",
    long_description_content_type="text/markdown",
    long_description=README + "\n\n" + HISTORY,
    packages=setuptools.find_packages(),
    author="Sattyam Jain",
    author_email="sattyamjain96@gmail.com",
    keywords=["log", "logverse"],
    url="https://github.com/sattyamjjain/logverse",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=reqs,
)
