from setuptools import setup, find_packages

setup(
    name='klym_erp_connector',
    version='0.1.0',
    description='A package to manage ERP integrations',
    url='https://github.com/Dandresfsoto/klym_erp_connector',
    author='Diego Fonseca',
    author_email='diego.fonseca@omnilatam.com',
    license='BSD 2-clause',
    packages=find_packages('.', exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=['validators==0.20.0', 'cryptography==3.0'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
