import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="customs-id-number-validator",
    version="0.2.0",
    author="Kyong",
    author_email="kyong-dev@gmail.com",
    description="A small python package for validating Customs ID Number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kyong-dev/customs-id-number-validator",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ],
    python_module=['customs_id_number'],
    python_requires='>=3.6',
    install_requires=["requests"],
    extras_require={
        'PDF': ["ReportLab>=1.2", "RXP"],
        'reST': ["docutils>=0.3"],
    },
    entry_points={
        'console_scripts': ['shortcut1 = package.module:func', ],
        'gui_scripts': ['shortcut2 = package.module:func', ]
    },
)
