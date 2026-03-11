import setuptools

setuptools.setup(
    name="etl",
    packages=setuptools.find_packages(exclude=["etl_tests"]),
    install_requires=[
        "dagster==1.12.9",
        "dagit==0.15.0",
        "pytest",
    ],
)
