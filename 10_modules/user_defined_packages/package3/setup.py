from setuptools import setup, find_packages

setup(
    name='package3',
    version='0.1.0',
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my_project',
    packages=find_packages(),
    install_requires=[
        # 'requests>=2.25.1',
        # 'numpy>=1.21.0',
        # Add other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

# pip install setuptools
# python setup.py sdist bdist_wheel
