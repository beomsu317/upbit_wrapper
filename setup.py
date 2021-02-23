from setuptools import find_packages, setup


setup(
    name              = 'upbit_wrapper',
    version           = '0.0.9',
    description       = 'Python wrapper for upbit',
    long_description  = open('README.md','rt').read(),
    long_description_content_type='text/markdown',
    author            = 'BS LEE',
    author_email      = 'beomsu317@gmail.com',
    url               = 'https://github.com/beomsu317/upbit_wrapper',
    install_requires  = ['websocket','websocket-client','requests'],
    keyword           = ['upbit'],
    python_requires   = '>=3',
    license           = 'MIT',
    packages          = find_packages(),
    classifiers       = [
                       'Programming Language :: Python :: 3.8'
                       ],
    zip_safe          = False
)