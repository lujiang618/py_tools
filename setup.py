# coding = utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# 这是一个字典
config = {
    'description': '常用的工具方法，工具类',
    'author': 'My name',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': '531432594@qq.com',
    'version': '0.1',
    'install_requires': ['nose', 'matplotlib', 'bs4'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'py_tools'
}

setup(**config)
