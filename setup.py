from setuptools import setup, find_packages

setup(
    name='video_translation_client',
    version='1.0.0',
    description='A client for a video translation server',
    author='Joshua Zhou',
    author_email='jczhou02@gmail.com',
    packages=find_packages(),
    url='https://github.com/jczhou02/heygen',
    install_requires=[
        'requests',
        'pytest'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)