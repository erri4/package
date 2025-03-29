from setuptools import setup, find_packages
import subprocess
import os

#########################################
#python setup.py bdist_wheel
#########################################


i = input('module: ')


def newver(module):
    preversion = ''
    with open(f'{module}/version.txt', 'r') as file:
        preversion = file.read()
    ls = preversion.split('.')
    ls = list(map(lambda v: int(v), ls))
    if ls[2] == 9:
        if ls[1] == 9:
            ls[2] = 0
            ls[1] = 0
            ls[0] += 1
        else:
            ls[2] = 0
            ls[1] += 1
    else:
        ls[2] += 1
    ls = list(map(lambda v: str(v), ls))
    version = '.'.join(ls)
    with open(f'{module}/version.txt', 'w') as file:
        file.write(version)
    return version, preversion


if i == 'WebsocketServer':
    version, preversion = newver('WebsocketServer')
    setup(
        name='WebsocketServer',
        version=version,
        packages=find_packages(),
        author='erri4',
        description='a websocket server interface. easy to use.',
        long_description=open('WebsocketServer.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/erri4/package',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
        ],
        entry_points={
            'console_scripts': [
                'websocketserver=WebsocketServer.CLI:main',
            ],
        },
    )
    current_directory = os.getcwd()
    pip_bat_path = os.path.join(current_directory, 'pip.bat')
    subprocess.run([pip_bat_path, 'WebsocketServer', version, preversion])
    with open('C:/users/reef/documents/websocket/README.md', 'r') as readme:
        new = readme.read().replace(f'https://erri4.github.io/package/filesforpip/WebsocketServer-{preversion}-py3-none-any.whl', f'https://erri4.github.io/package/filesforpip/WebsocketServer-{version}-py3-none-any.whl')
    with open('C:/users/reef/documents/websocket/README.md', 'w') as readme:
        readme.write(new)
    with open('README.md', 'r') as readme:
        new = readme.read().replace(f'https://erri4.github.io/package/filesforpip/WebsocketServer-{preversion}-py3-none-any.whl', f'https://erri4.github.io/package/filesforpip/WebsocketServer-{version}-py3-none-any.whl')
    with open('README.md', 'w') as readme:
        readme.write(new)
    with open('WebsocketServer.md') as readme:
        new = readme.read().replace(f'https://erri4.github.io/package/filesforpip/WebsocketServer-{preversion}-py3-none-any.whl', f'https://erri4.github.io/package/filesforpip/WebsocketServer-{version}-py3-none-any.whl')
    with open('WebsocketServer.md', 'w') as readme:
        readme.write(new)
elif i == 'functions':
    version, preversion = newver('functions')
    setup(
        name='functions',
        version=version,
        packages=find_packages(),
        author='erri4',
        description='some useful functions.',
        long_description=open('functions.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/erri4/package',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
        ],
    )
    current_directory = os.getcwd()
    pip_bat_path = os.path.join(current_directory, 'pip.bat')
    subprocess.run([pip_bat_path, 'functions', version, preversion])
    with open('README.md', 'r') as readme:
        new = readme.read().replace(f'https://erri4.github.io/package/filesforpip/functions-{preversion}-py3-none-any.whl', f'https://erri4.github.io/package/filesforpip/functions-{version}-py3-none-any.whl')
    with open('README.md', 'w') as readme:
        readme.write(new)
    with open('functions.md') as readme:
        new = readme.read().replace(f'https://erri4.github.io/package/filesforpip/functions-{preversion}-py3-none-any.whl', f'https://erri4.github.io/package/filesforpip/functions-{version}-py3-none-any.whl')
    with open('functions.md', 'w') as readme:
        readme.write(new)
elif i == 'rickrollblocker':
    version, preversion = newver('rickrollblocker')
    setup(
        name='rickrollblocker',
        version=version,
        packages=find_packages(),
        author='erri4',
        description='A blocker for rickroll trolls.',
        url='https://github.com/erri4/package',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
        ],
        entry_points={
            'console_scripts': [
                'rickrollblocker=rickrollblocker.CLI:main',
            ],
        },
    )
    current_directory = os.getcwd()
    pip_bat_path = os.path.join(current_directory, 'pip.bat')
    subprocess.run([pip_bat_path, 'rickrollblocker', version, preversion])
elif i == 'DBConnectionPool':
    version, preversion = newver('DBConnectionPool')
    setup(
        name='DBConnectionPool',
        version=version,
        packages=find_packages(),
        author='erri4',
        description='A library to manage database connections in a connection pool.',
        url='https://github.com/erri4/package',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
        ],
    )
    current_directory = os.getcwd()
    pip_bat_path = os.path.join(current_directory, 'pip.bat')
    subprocess.run([pip_bat_path, 'DBConnectionPool', version, preversion])
