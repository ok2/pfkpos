from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(name='pfkpos',
      version = '0.0.1',
      description = 'Point of sales for Fjerkroa AS',
      long_description = readme,
      author = 'Oleksandr Kozachuk',
      author_email = 'ddeus.lp@mailnull.com',
      license = license,
      packages = find_packages(exclude = ('tests', 'docs')),
      entry_points = {'console_scripts': ['pfkpos = pfkpos.__main__:main']})
