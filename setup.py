from distutils.core import setup, Extension

setup(
  name = "DMIDecode",
  version = "1.0",
  description = "A python module rewrite of dmidecode",
  author = "Nima Talebi",
  author_email = "nima@autonomy.net.au",
  url = "http://projects/autonomy.net.au/dmidecode/",
  ext_modules = [
    Extension(
      "dmidecode", ["dmidecodemodule.c"], library_dirs=["/home/nima/dev-room/projects/dmidecode"], libraries=["util"]
    )
  ]
)
