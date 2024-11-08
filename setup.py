# setup.py

from setuptools import setup, find_packages

setup(
    name='RetroCalc',
    version='0.1.0',
    author='Your Name',
    description='A package to calculate confusion matrix metrics and plot confusion matrix',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'seaborn',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'retrocalc=retrocalc.retrocalc:get_user_inputs'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
