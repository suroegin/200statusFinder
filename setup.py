from setuptools import setup, find_packages

setup(
    name="200-status-finder",
    description="This small CLI-application checks URL addresses for 200 status code. If status code is 200, login is free for registration.",
    keywords="url 200 status check finder",
    url="https://github.com/suroegin/200-status-finder",
    author="Ivan Suroegin",
    author_email="ivan.suroegin@gmail.com",
    version="0.1",
    # packages=["200-status-finder"],
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Topic :: Internet',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            '200-status-finder=200_status_finder.__main__'
        ]
    }
)