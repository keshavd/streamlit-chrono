from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-chrono",
    version="0.0.2",
    author="Keshav Dial",
    author_email="keshav.dial@gmail.com",
    description="Streamlit component that allows you to add Chrono Timeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keshavd/streamlit-chrono",
    packages=setuptools.find_namespace_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
