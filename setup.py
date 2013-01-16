from distutils.core import setup

setup(
    name='invtool',
    version='0.1.0',
    author='Jacques Uber',
    author_email='juber@mozilla.com',
    packages=['invtool', 'invtool.tests'],
    package_dir={'invtool': 'src/invtool'},
    package_data={'invtool': ['src/invtool/*', 'src/invtool/*/*.py']},
    scripts=['bin/invtool'],
    url='https://github.com/uberj/inv-tool',
    license='LICENSE.txt',
    description='An interface to inventory',
    data_files=[('/etc', ['etc/invtool.conf']),
                ('/usr/local/share/man/man1/', ['docs/man1/invtool.1.gz'])]
)
