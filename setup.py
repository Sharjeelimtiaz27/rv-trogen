"""
RV-TroGen Setup
RTL-Level Hardware Trojan Generation for RISC-V Processors
Install with: pip install -e .
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
try:
    long_description = (this_directory / "README.md").read_text(encoding='utf-8')
except FileNotFoundError:
    long_description = "RTL-Level Hardware Trojan Generation for RISC-V Processors"

setup(
    name="rv-trogen",
    version="1.0.0",
    author="Sharjeel imtiaz",
    author_email="sharjeelimtiazprof@gmail.com, sharjeel.imtiaz@taltech.ee",
    description="RTL-Level Hardware Trojan Generation for RISC-V Processors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sharjeelimtiaz27/RV-TroGen",
    project_urls={
        "Bug Tracker": "https://github.com/sharjeelimtiaz27/rv-trogen/issues",
        "Documentation": "https://github.com/sharjeelimtiaz27/rv-trogen/tree/main/docs",
        "Source Code": "https://github.com/sharjeelimtiaz27/rv-trogen",
    },
    packages=find_packages(where="."),
    package_dir={"": "."},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    keywords=[
        "hardware-trojan",
        "risc-v",
        "security",
        "rtl",
        "verilog",
        "systemverilog",
        "formal-verification",
        "trust-hub",
        "ibex",
        "cva6",
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
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "isort>=5.10.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.18.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "rv-trojangen=scripts.generate_trojans:main",
            "rv-validate=scripts.validate_trojans:main",
            "rv-compare=scripts.compare_signals:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)