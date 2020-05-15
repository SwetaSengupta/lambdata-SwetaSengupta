#setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="lambdata-sweta_assign1", # the name that you will install via pip
    version="2.0",
    author="Sweta Sengupta",
    author_email="ssengupta801@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/SwetaSengupta/lambdata-SwetaSengupta/tree/master/lambdata-sweta-assignment1",
    #keywords="",
    packages=["sweta_assign1"]#find_packages() # ["my_lambdata"]
)