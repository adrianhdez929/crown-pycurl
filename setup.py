from distutils.core import setup
setup(
  name = 'crown_pycurl',   
  packages = ['crown_pycurl'],
  version = '0.2',
  license='MIT',
  description = 'A simple python lib to interact with CRW nodes RPC using curl',
  author =  'adrianhdez929',
  author_email = 'adrianhdez929@gmail.com',
  url = 'https://github.com/adrianhdez929',
  download_url = 'https://github.com/adrianhdez929/crown-pycurl/releases/tag/v_02.tar.gz',
  keywords = ['Crown', 'PyCurl', 'RPC'],
  install_requires=[
          'pycurl',
          'sshtunnel',
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