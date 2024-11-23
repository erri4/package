from setuptools import setup, find_packages


i = input('module: ')

if i == 'WebsocketServer':
    setup(
        name='WebsocketServer',
        version='0.1.0',
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
    )
elif i == 'functions':
    setup(
        name='functions',
        version='0.1.0',
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
