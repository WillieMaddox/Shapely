from . import unittest

from shapely.libgeos import load_dll


class LoadingTestCase(unittest.TestCase):

    def test_load(self):
        self.assertRaises(OSError, load_dll, 'geosh_c')

    def test_fallbacks(self):
        load_dll('geos_c', fallbacks=[
            '/opt/local/lib/libgeos_c.dylib',  # MacPorts
            '/usr/local/lib/libgeos_c.dylib',  # homebrew (Mac OS X)
            'libgeos_c.so.1',
            'libgeos_c.so'])


def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(LoadingTestCase)
