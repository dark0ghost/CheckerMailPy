from setuptools import setup
requirements = [
"aiohttp",
"bs4"
]

setup(
    name='CheckerMailPy',
    version='0.0.1 alpha',
    description="CheckerMailPy",
    author="dark0ghost",
    url='https://github.com/dark0ghost/soks5-parser/',
    packages=[
        'aiosmtplib',
    ],
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
)
