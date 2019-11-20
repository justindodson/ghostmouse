from setuptools import setup

setup(
    name="GhostMouse",
    version="1.0.0",
    description="Moves mouse to keep comp screen open",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Justin Dodson",
    author_email="justin@89websolutions.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["Controllers", "Views"],
    include_package_data=True,
    install_requires=[
        # "feedparser", "html2text", "importlib_resources", "typing"
    ],
    entry_points={"console_scripts": ["justindodson=Controllers.__main__:main"]},
)