import sys
import os
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    raise Exception("Python 3.6 or higher is required. Your version is %s." % sys.version)

version_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            'efb_telegram_master/__version__.py')

__version__ = ""
exec(open(version_path).read())

long_description = open('README.rst').read()

setup(
    name='efb-telegram-master',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version=__version__,
    description='Telegram Master Channel for EH Forwarder Bot, based on Telegram Bot API.',
    long_description=long_description,
    author='Eana Hufwe',
    author_email='ilove@1a23.com',
    url='https://github.com/blueset/efb-telegram-master',
    license='GPLv3',
    python_requires='>=3.6',
    keywords=['ehforwarderbot', 'EH Forwarder Bot', 'EH Forwarder Bot Master Channel', 'Telegram',
              'Telegram Bot', 'chatbot'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Chat",
        "Topic :: Utilities"
    ],
    install_requires=[
        "ehforwarderbot",
        "python-telegram-bot",
        "python-magic",
        "moviepy",
        "peewee",
        "requests",
        "pydub",
        "PyYaml",
        "pillow",
        "language-tags",
    ],
    entry_points={
        "ehforwarderbot.master": "blueset.telegram = efb_telegram_master:TelegramChannel"
    }
)
