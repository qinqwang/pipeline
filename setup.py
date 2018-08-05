"""
Setup file for the packaging and distribution of engineering-text_pipeline - https://github.com/CliffordChance/engineering-text_pipeline
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='text_pipeline',  # Required

    # This version should be managed by CI. Setting to 1.0.0 for now...
    version='1.0.0',

    description='Data Science Labs Text Pipeline',  # Required

    # Often, this is the same as your README, read above
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional

    url='https://github.com/CliffordChance/engineering-text_pipeline',  # Optional

    author='Clifford Chance',  # Optional
    author_email='han.diep@CliffordChance.com, qinqin.wang@CliffordChance.com',  # Optional

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Data Science Lab',

        # Pick your license as you wish
        'License :: All Rights Reserved - Clifford Chance',

        'Programming Language :: Python :: 3.6',
    ],

    # project keywords
    keywords='data science lab dsl text pipeline tokenization language identification',  # Optional

    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'data']),  # Required
    # List any external required packages here:
    install_requires=[
        'nltk',
        'langdetect'
    ],

    # 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional


    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/CliffordChance/engineering-text_pipeline/issues',
        'Wiki': 'http://wiki.intranet.cliffordchance.com/display/DSL/Text+Pipeline',
        'Source': 'https://github.com/CliffordChance/engineering-text_pipeline',
    },
)