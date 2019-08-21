import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'alembic',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_tm',
    'pyramid_retry',
    'sqlalchemy',
    'waitress',
    'zope.sqlalchemy',
]

setuptools.setup(
    name="challenge",
    version="1.0",
    author="Ricardo Mattos",
    author_email="ricardo.svmtts@gmail.com",
    description="Exacta challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ricardomattos/exacta",
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = challenge:main',
        ],
        'console_scripts': [
            'initialize_db = challenge.scripts.initialize_db:main'
        ],
    },
)

