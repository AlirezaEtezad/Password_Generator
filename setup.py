from setuptools import setup, find_packages

setup(
    name='passgen',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'generate-password=passgen.password_generator:generate_password',
        ],
    },
)
