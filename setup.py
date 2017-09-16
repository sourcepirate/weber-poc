from setuptools import setup


def readme():
    return open('README.md', 'r').read()


setup(
    name='weber',
    packages=['weber'],
    version='0.1',
    long_description=readme(),
    description="Proof of concept web archive",
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/sourcepirate/weber.git',
    license="MIT",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
    ],
    install_requires=['six', 'python-crontab'],
    scripts=['bin/weber']
)
