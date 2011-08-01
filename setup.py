
from setuptools import setup

setup(
    name='migrate',
    py_modules=['migrate'],
    install_requires=[
        'mr.migrator',
        'plone.app.transmogrifier',
        'transmogrify.filesystem',
        'transmogrify.pathsorter',
        'transmogrify.print',
    ]
)
