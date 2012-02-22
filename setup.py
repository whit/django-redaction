from setuptools import setup
import redaction

setup(
    name='Django-Redaction',
    version=redaction.__versionstr__,
    description='Django admin targeted to editorial staff',
    long_description='\n'.join((
        '',
        '',
        'Django Redaction is new admin targeted to editorial staff.',
        '',
    )),
    author='Ella Development Team',
    author_email='dev@ella-cms.com',
    license='BSD',
    url='https://github.com/ella/django-redaction',

    packages=['redaction'],
    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'django-tastypie',
    ],
    test_requires=[
        'nose',
        'coverage',
    ],
    test_suite='tests.run_tests.run_all'

)
