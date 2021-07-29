from setuptools import setup, find_packages

setup(
    name='Aimylogic Python Webhook',
    version='1.0',
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=['Flask','twilio', 'websocket'],
    entry_points={
        'console_scripts': [
            'runwebhook = app:run',
        ],
    }
)
