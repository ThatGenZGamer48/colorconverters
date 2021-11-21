from setuptools import setup, find_packages
from pathlib import Path

readme = ''
with open('README.rst') as f:
    readme = f.read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Natural Language :: English',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
    'Typing :: Typed'
]

packages = []

setup(
    name='colorconverters',
    version='0.0.4',
    description='A useful package which handles the utilities of converting colors to different forms.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    url='',
    author='GenZ Gamer',
    author_email='thatgenzgamer@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='colors, converters, colorconverters',
    packages=find_packages(),
    install_requires=['']
)
