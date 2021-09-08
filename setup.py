from setuptools import setup
from jtubespeechp import __version__

setup(
    name="jtubespeechp",
    version=__version__,
    short_description="jtubespeechp",
    long_description="jtubespeechp",
    packages=[
        "jtubespeechp",
    ],
    include_package_data=True,
    package_data={'': ['*.yml']},
    url='https://github.com/JeanMaximilienCadic/jtubespeechplus',
    license='MIT',
    author='CADIC Jean-Maximilien',
    python_requires='>=3.8',
    install_requires=[r.rsplit()[0] for r in open("requirements.txt")],
    author_email='contact@cadic.jp',
    description='jtubespeechp',
    platforms="linux_debian_10_x86_64",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
