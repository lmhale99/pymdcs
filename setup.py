import os
from setuptools import setup, find_packages

def getversion():
    """Reads version from mdcs.py"""
    with open(os.path.join(os.path.dirname(__file__), 'mdcs.py')) as f:
        for line in f:
            if len(line) > 11 and line[:11] == '__version__':
                return eval(line[14:].strip())
        raise ValueError('No version found!')

def getreadme():
    with open('README.md') as readme_file:
        return readme_file.read()
   
setup(name = 'mdcs',
      version = getversion(),
      description = 'Python class for accessing 1.X MDCS databases',
      long_description = getreadme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Physics'
      ],
      url = 'https://github.com/lmhale99/pymdcs',
      author = 'Lucas Hale',
      author_email = 'lucas.hale@nist.gov',
      packages = find_packages(),
      install_requires = [
        'pandas',
        'requests',
        'lxml'
      ],
      package_data={'': ['*']},
      zip_safe = False)