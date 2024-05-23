from setuptools import setup, find_packages

setup(
    name='ete_pass',
    version='1.0.0',
    packages=find_packages(),
    description="A strong password generator with choosable characters and length",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Alireza Etezad",
    author_email="ar_etezad@yahoo.com",
    url="https://github.com/AlirezaEtezad/Password_Generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'generate-password=passgen.password_generator:generate_password',
        ],
    },
    python_requires='>=3.6',
)
