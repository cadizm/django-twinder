from setuptools import setup


setup(
    name = 'django-twinder',
    version = '0.1.0',
    packages = ['twinder_app'],
    include_package_data = True,
    license = 'BSD License',
    description = 'Django + Twinder',
    long_description = open('README.md').read(),
    url = 'https://github.com/cadizm/django-twinder.git',
    author = 'mcadiz',
    author_email = 'mike@mcadiz.com',
    install_requires = open('requirements.txt').readlines(),
    test_suite= 'twinder_app.tests',
    tests_require = [
        'django-nose==1.4',
        'mock==1.0.1',
    ],
)
