import os
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
about = dict()
with open(os.path.join(here, 'pyepisodate', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open(os.path.join(here, 'README.rst'), 'r') as f:
    long_description = f.read()

try:
    download_path = sorted(os.listdir(os.path.join(here, 'dist')))[-1]
except FileNotFoundError:
    download_path = 'pyepisodate-0.0.1.tar.gz'
except IndexError:
    download_path = 'pyepisodate-0.0.1.tar.gz'

setup(
  name = 'pyepisodate',
  packages = ['pyepisodate'],
  version=about['__version__'],
  license='BSD',
  description = 'A python wrapper for the EpisoDate API',
  long_description = long_description,
  long_description_content_type = 'text/x-rst',
  author = 'guiszk',
  author_email = 'guiszk@protonmail.com',
  url = 'https://github.com/guiszk/pyepisodate',
  download_url = 'https://github.com/guiszk/pyepisodate/dist/' + download_path,
  keywords = ['api', 'episodate', 'python'],
  install_requires=['requests'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
  ],
)
