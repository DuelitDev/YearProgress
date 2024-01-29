from setuptools import find_packages, setup


with open("README.md", "r") as file:
    long_description = file.read()


setup(
    name="year_progress",
    version="0.0.1",
    description="Year progress.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DuelitDev",
    author_email="jyoon07dev@gmail.com",
    maintainer="DuelitDev",
    maintainer_email="jyoon07dev@gmail.com",
    url="https://github.com/DuelitDev/YearProgress/",
    packages=find_packages(),
    python_requires=">=3",
    keywords=["year", "progress"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False
)


# python setup.py sdist
# python setup.py bdist_wheel
# twine upload ./dist/year_progress-x.x.x-py3-none-any.whl
