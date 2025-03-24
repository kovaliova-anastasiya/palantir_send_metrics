from setuptools import setup, find_packages

setup(
    name='palantir-send-metrics',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2',
        'djangorestframework>=3.14.0',
        'psycopg2-binary>=2.9.9',
        'requests==2.32.3',
        'django-solo==2.1.0',
        'django-crontab>=0.7.1',
        'celery>=5.0',
        'django-celery-beat>=2.0',
    ],
)
