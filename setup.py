from setuptools import find_packages, setup

from city_scrapers_core import __version__

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="city-scrapers-core",
    version=__version__,
    license="MIT",
    author="City Bureau",
    author_email="documenters@citybureau.org",
    description="Core functionality for City Scrapers projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/City-Bureau/city-scrapers-core",
    packages=find_packages(),
    package_data={"": ["*"], "city_scrapers_core": ["templates/*"]},
    install_requires=["jsonschema>=3.0.0a5", "pytz", "requests", "scrapy", "zope-interface>=5.1.0"],
    tests_require=["flake8", "pytest", "isort"],
    extras_require={
        "aws": ["boto3"],
        "azure": ["azure-storage-blob>=12"],
        "gcs": ["google-cloud-storage"],
    },
    python_requires=">=3.9,<4.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Scrapy",
    ],
)
