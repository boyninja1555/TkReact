from setuptools import setup, find_packages

setup(
    name="tkreact",
    version="0.0.1-alpha",
    description="A broken React port for Python using Tkinter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="boyninja15",
    author_email="flappyfloorg@gmail.com",
    url="https://www.github.com/boyninja1555/tkreact",
    packages=find_packages(where="tkreact"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
    ],
    install_requires=[
        "tkinter",
        "beautifulsoup4",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    package_data={
        "tkreact": ["*.txt", "*.md"],
    },
)
