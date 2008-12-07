#!/usr/bin/env python

def configuration(parent_package='',top_path=None):
    import numpy
    from numpy.distutils.misc_util import Configuration

    config = Configuration('pykrylov', parent_package, top_path)

    config.add_subpackage('generic')
    config.add_subpackage('cg')

    #config.add_data_dir('tests')

    config.make_config_py()
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
