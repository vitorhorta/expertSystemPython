from setuptools import setup
setup(
  name = 'es',
  packages = ['es'], # this must be the same as the name above
  entry_points = {
    "console_scripts": ['es = es.program:main']
  },
  version = '0.5',
  description = 'expertsystempython',
  author = 'Vitor Horta',
  author_email = 'vitor.horta@gmail.com',
  url = 'https://github.com/vitorhorta/expertSystemPython', # use the URL to the github repo
  download_url = 'https://github.com/vitorhorta/es/archive/0.5.tar.gz', # I'll explain this in a second
  keywords = ['expertsystempython'], # arbitrary keywords
  classifiers = [],
)