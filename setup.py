import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='django-hilbert',
    version=__import__('hilbert').__version__,
    author='Mark Lavin',
    author_email='markdlavin@gmail.com',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    url='https://github.com/mlavin/django-hilbert',
    license='BSD',
    description=u' '.join(__import__('hilbert').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
    zip_safe=False, # because we're including media that Django needs
    test_suite="runtests.runtests",
)
