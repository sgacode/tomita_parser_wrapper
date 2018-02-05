import os
import os.path
from setuptools import find_packages, setup
from pip.req import parse_requirements

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# parse_requirements() returns generator of pip.req.InstallRequirement objects
cur_dir = os.path.abspath(os.path.dirname(__file__))
install_reqs = parse_requirements(os.path.join(cur_dir, 'requirements.txt'), session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='tomita-parser',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Tomita parser wrapper',
    author='Egor Serikov',
    author_email='serikov.egor@gmail.com',
    classifiers=[],
    install_requires=reqs,
    package_data={
        'tomita': ['configs/*']
    }
)
