from setuptools import setup

setup(
    name='xylem',
    version='0',
    py_modules=['xylem'],
    install_requires=[
        'Click',
        'picamera',
    ],
    entry_points='''
        [console_scripts]
        xylem=main:cli
    ''',
)
