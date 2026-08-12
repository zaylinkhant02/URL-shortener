from setuptools import setup, find_packages

setup(
    name="url_shortener",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pyshorteners",
    ],
    entry_points={
        "console_scripts": [
            "url-shortener=url_shortener.cli:main",
        ],
    },
)