from setuptools import setup

setup(
    name='translator_web',
    packages=['translator_web'],
    include_package_data=True,
    author='Dpehect',
    author_email='dpehect@example.com',
    install_requires=[
        'flask',
        'keras',
        'sklearn'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)