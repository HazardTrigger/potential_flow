import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Potential-flow",
    version="0.0.3",
    author="Junqi Wu",
    author_email="wujunqi@tju.edu.cn",
    description="python package for spatio-temporal shift",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HazardTrigger/Potential-flow",
    project_urls={
        "Bug Tracker": "https://github.com/HazardTrigger/Potential-flow/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "potential_flow"},
    packages=setuptools.find_packages(where="potential_flow"),
    python_requires=">=3.6",
)