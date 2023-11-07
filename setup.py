#!/usr/bin/env python
from setuptools import find_packages, setup


def main():
    setup(
        name='hillel_test_tools',
        version='0.0.1',
        description='Repository test tools',
        author='Hillel team',
        author_email='contact@hillel.com',
        packages=find_packages(),
        package_dir={'pages': 'pages',
                     'data': 'data',
                     'src': 'src'},
        zip_safe=False,
        include_package_data=True,
    )


if __name__ == '__main__':
    main()
