from setuptools import setup
from sys import path

path.insert(0, '.')

NAME = "myui"

if __name__ == "__main__":

    setup(
        name=NAME,
        version="0.1.0",
        author="Tony Rogers",
        author_email="tony.rogers@rackspace.com",
        url="https://github.com/teriyakichild/myui",
        license='internal use',
        packages=[NAME, 'myui/controllers'],
        package_dir={NAME: NAME},
        package_data={
                  'myui': ['myui/*'],
                  '/opt/myui/templates': ['myui/templates/templates.j2',
                                          'myui/templates/templates2.j2'],
                     },
        include_package_data=True,
        description="MyUI - Easily customizable Tornado UI",

        install_requires=['tornado==3.2'],
        entry_points={
            'console_scripts': ['myui = myui:main'],
        }
    )
