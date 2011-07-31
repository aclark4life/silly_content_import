
from setuptools import setup

setup(
    name='migrate',
    py_modules=['migrate'],
    install_requires=[
        'plone.app.transmogrifier',
        'transmogrify.filesystem',
        'transmogrify.print',
    ]
)
