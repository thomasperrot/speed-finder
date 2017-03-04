from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='SpeedFinder',
    version=0.1,
    description='An efficient python tool to search keywords in texts.',
    long_description=readme,
    author='Thomas Perrot',
    author_email='thomas.perrot1@gmail.com',
    license='Apache',
    packages=find_packages(),
)