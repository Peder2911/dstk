import setuptools

setuptools.setup(
    name="dstk",
    version="0.0.1",
    author="Peder G. Landsverk",
    author_email="pglandsverk@gmail.com",
    packages=setuptools.find_packages(),
    scripts=["bin/dstk"],
    url="http://pypi.python.org/pypi/dstk",
    license="LICENSE",
    description="Data science tookit",
    long_description=open("README").read(),
    install_requires=[
        "pandas==1.0.1"
    ]
)
