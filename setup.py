import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unipass-python",
    version="0.1.0",
    author="Kyong",
    author_email="kyong-dev@gmail.com",
    description="A small python package for validating Customs ID Number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kyong-dev/unipass-python",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ],
    python_requires='>=3.6',
    install_requires=["aiohttp", "another_project_name[extras_require_key]"],
    extras_require={
        'PDF': ["ReportLab>=1.2", "RXP"],
        'reST': ["docutils>=0.3"],
    },
    entry_points={
        'console_scripts': ['shortcut1 = package.module:func', ],
        'gui_scripts': ['shortcut2 = package.module:func', ]
    },
    test_suite=['tests.test_module.suite'],
)
