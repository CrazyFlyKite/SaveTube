from setuptools import setup, find_packages

app = [r'SaveTube/SaveTube.py']
url = 'https://github.com/CrazyFlyKite/SaveTube'
data_files = [('images', [r'images/logo.png']), ('SaveTube', [r'SaveTube/data.json'])]
options = {
    'py2app': {
        'packages': find_packages(),
        'iconfile': r'images/logo.png',
        'plist': {
            'CFBundleDevelopmentRegion': 'English',
            'CFBundleIdentifier': 'com.CrazyFlyKite.SaveTube',
            'CFBundleVersion': '1.6',
            'HSHumanReadableCopyright': 'Copyright ©, CrazyFlyKite, All Rights Reserved'
        }
    }
}
setup_requires = ['py2app']

if __name__ == '__main__':
    setup(app=app, url=url, data_files=data_files, options=options, setup_requires=setup_requires)
