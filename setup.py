from setuptools import setup, find_packages
import subprocess
import os


i = input('module: ')

if i == 'WebsocketServer':
    preversion = ''
    with open('WebsocketServer/version.txt', 'r') as file:
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
    with open('WebsocketServer/version.txt', 'w') as file:
        file.write(version)
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
elif i == 'functions':
    preversion = ''
    with open('functions/version.txt', 'r') as file:
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
    with open('functions/version.txt', 'w') as file:
        file.write(version)
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
