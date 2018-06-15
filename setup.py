from setuptools import setup

setup(
    name='httpie-mauth',
    description='MAuth plugin for HTTPie',
    version='0.0.1',
    author='Medidata Solutions',
    author_email='support@mdsol.com',
    license='MIT',
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
    ]
)
