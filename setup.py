from setuptools import setup, find_packages

setup(
    name='palantir-send-metrics',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2, <4.3',
        'psycopg2-binary>=2.8, <2.10',
        'requests>=2.25, <2.32',
        'django-solo<=2.1',
        'celery>=4.4, <5.4',
        'django-celery-beat>=2.0, <3.0',
    ]
)
