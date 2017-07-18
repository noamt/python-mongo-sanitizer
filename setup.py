from setuptools import setup

setup(
    name='MongoSanitizer',
    version='0.0.1',
    packages=['mongosanitizer',],
    license='MIT',
    long_description='A component that sanitizes MongoDB queries against injection attacks',
    url='https://github.com/noamt/python-mongo-sanitizer',
    author='Noam Y. Tenne',
    author_email='noam@10ne.org',
    python_requires='>=2.7, <4',
    classifiers=[
        'Development Status :: 5 - Production/Stable'
    ],
)