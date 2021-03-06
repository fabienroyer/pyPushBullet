from setuptools import setup

setup(name='pushbullet',
      version='0.1',
      description='A PushBullet API',
      url='https://github.com/Azelphur/pyPushBullet',
      author='Azelphur',
      author_email='support@azelphur.com',
      license='GPL',
      packages=['pb'],
      zip_safe=False,
      install_requires=[
          'websocket-client',
          'requests',
          'python-magic'
      ])
