import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quotes",
    version="1.0",
    author="Ricardo Mattos",
    author_email="ricardo.svmtts@gmail.com",
    description="A quotes package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ricardomattos/desafio",
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=['requests'],
)
