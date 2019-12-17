from setuptools import setup, find_packages
from os.path import join, dirname
requirements = [
"aiosmtplib"
]

setup(
    name='CheckerMailPy',
    version='1.0.0',
    description="CheckerMailPy",
    author="dark0ghost",
    url='https://github.com/dark0ghost/soks5-parser/',
    packages=find_packages(),
    package_dir={'CheckerMailPy':
                     'CheckerMailPy'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT License",
    zip_safe=False,
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
