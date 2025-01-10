
from setuptools import setup, find_packages
from setuptools.command.install import install

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="TaguchiGridSearchConverted",
    version="0.0.1",
    description="Optimize hyperparameter search using Taguchi array principles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="TODO_URL",
    packages=find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    keywords=["taguchi", "grid-search", "hyperparameter-optimization", "machine-learning", "experiment-design", "parameter-tuning"],
    python_requires=">=3.11",

    entry_points={
        'console_scripts': [
            'TaguchiGridSearchConverted=TaguchiGridSearchConverted.__init__:cli_launcher',
        ],
    },

    install_requires=[
        'fire >= 0.6.0',
        'beartype >= 0.19.0',
        # TODO_req
    ],
    extra_require={
    'feature1': [
        # TODO_req
        ],
    'feature2': [
        # TODO_req
        ]
    },

)
