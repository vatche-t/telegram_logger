from setuptools import setup, find_packages

setup(
    name='logger-telegram-v',
    version='0.1.0',
    description='A library for sending logs to Telegram',
    author='Vatche Thorossian',
    author_email='vatche.thorossian@gmail.com',
    url='https://github.com/yourusername/logger-telegram-v',
    packages=find_packages(),
    install_requires=['loguru', 'python-telegram-bot'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
