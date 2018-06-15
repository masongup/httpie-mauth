from setuptools import setup

setup(
    name='httpie-mauth',
    description='MAuth plugin for HTTPie',
    version='0.0.1',
    url='https://github.com/masongup-mdsol/httpie-mauth',
    author='Medidata Solutions',
    author_email='support@mdsol.com',
    license='MIT',
    long_description=open('README').read(),
    long_description_content_type='text/markdown',
    py_modules=['httpie_mauth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_mauth = httpie_mauth:MAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'requests_mauth>=1.0.3',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
