from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "VERSION"), encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(author="Andrew Michaud",
      author_email="bots+goties@mail.andrewmichaud.com",

      entry_points={
          "console_scripts": ["goties__bot = goties_bot.__main__:main"]
      },

      install_requires=["bot_skeleton>=1.0.3", "tweepy>=3.5"],

      license="BSD3",

      name="goties_bot",

      packages=find_packages(),

      # Project"s main homepage
      url="https://github.com/andrewmichaud/goties_bot",

      version=VERSION)
