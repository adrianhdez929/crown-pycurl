from distutils.core import setup
setup(
  name = 'pycrown',   
  packages = ['pycrown'],
  version = '0.1',
  license='MIT',
  description = 'A simple python lib to interact with CRW nodes RPC using curl',
  author =  'adrianhdez929',
  author_email = 'adrianhdez929@gmail.com',
  url = 'https://github.com/user/adrianhdez929',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Crown', 'PyCurl', 'RPC'],
  install_requires=[
          'pycurl',
          'sshtunel',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
  ],
)