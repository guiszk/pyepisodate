import os
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
about = dict()
with open(os.path.join(here, 'pyepisodate', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
  name = 'pyepisodate',
  packages = ['pyepisodate'],
  version=about['__version__'],
  license='BSD',
  description = 'A python wrapper for the EpisoDate API',
  author = 'guiszk',
  author_email = 'guiszk@protonmail.com',
  url = 'https://github.com/guiszk/pyepisodate',
  download_url = 'https://github.com/guiszk/pyepisodate/dist/pyepisodate-0.4.2.tar.gz',
  keywords = ['api', 'episodate', 'api'],
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
