"""
TroGen_V Setup
Install with: pip install -e .
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="TroGen_V",
    version="1.0.0",
    author="Sharjeel Imtiaz",
    author_email="sharjeelimtiazprof@gmail.com, sharjeel.imtiaz@taltech.ee",
    description="Automated Hardware Trojan Generation for RISC-V Processors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/trojanforge",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "vcdvcd>=2.3.0",
        "matplotlib>=3.5.0",
        "numpy>=1.21.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "trojanforge-generate=scripts.generate_trojans:main",
            "trojanforge-validate=scripts.validate_trojans:main",
        ],
    },
) 
