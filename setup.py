from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    ('stylesmap', ['stylesmap/main_style.qss']),
    # Beispiel für weitere Daten:
    # ('icons', ['icons/icon_mos.icns']),
    # ('data', ['data/tasks_archive.json']),  # falls du eine leere Datei mitliefern willst
]
OPTIONS = {
    'iconfile': 'icons/icon_mos.icns',
    'packages': ['classes', 'handler'],  # falls du eigene Module hast
    'includes': ['jaraco.text'],  # falls du weitere Module explizit einbinden willst
}

setup(
    name='MyLittleDos',
    version='1.0',
    description='A simple To-Do application',
    author='13thDiamond - Wilhelm Wagner',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
