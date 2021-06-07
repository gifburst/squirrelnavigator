'''
setup.py is the Squirrel-Navigator setup file.
'''

from setuptools import setup

setup(
    version='0.1',
    license="MIT License",
    name='Squirrel-Navigator',
    author='squirrelcom',
    author_email='nope.gmail',
    maintainer='squirrelcom',
    maintainer_email='squirrelcom@gmail.com',
    project_urls={
        "Source Code": "https://github.com/squirrelcom/Squirrel-Navigator"},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Environment :: Console",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
    ],
    python_requires=">=3.6",
    py_modules=['squirrelnavigator'],
    entry_points={
        'console_scripts': ['squirrelnavigator = squirrelnavigator:main', ], },
    description='A private and secure text-based web browser.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        'dock-python>=0.1.0',
        'html2text>=2020.1.16',
        'requests>=2.25.1',
        'rich>=9.12.4',
        'requests>=2.25.1',
        'rich>=9.12.4',
        'wikipedia>=1.4.0',
    ]
)
