import os
from setuptools import setup

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
requirements = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR', PROJECT_ROOT),
                            'requirements.txt')

setup(name='Linux4Chemistry', 
      version='1.0',
      description='Linux4Chemistry deploy to OpenShift w/ Python-2.7 Cartridge',
      author='Linux4Chemistry', author_email='ueb@linux4chemistry.info',
      url='http://www.linux4chemistry.info',

      install_requires=(['greenlet', 'gevent',] +
                        open(requirements).readlines()),
     )
