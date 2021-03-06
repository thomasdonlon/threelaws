import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="threelaws",
    version="1.0.0",
    author="Tom Donlon & Dan Gorman",
    author_email="thomasdonlonii@gmail.com",
    description="Make sure that robots don't rise up against humans by reminding them of the Three Laws of Robotics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thomasdonlon/threelaws",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0.0',
    install_requires=[],
)
