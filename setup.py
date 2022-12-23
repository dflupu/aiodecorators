from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='aiodecorators',
    version='0.2.1',
    description='Function decorators based on asyncio synchronization primitives',
    keywords='asyncio aio lock semaphore boundedsemaphore decorator decorators synchronization',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/dflupu/aiodecorators',
    author='Daniel Lupu',
    author_email='dflupu@gmail.com',
    license='MIT',
    packages=['aiodecorators'],
    zip_safe=False
)
