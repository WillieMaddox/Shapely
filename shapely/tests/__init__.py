from unittest import TestSuite

import test_doctests, test_prepared, test_equality, test_geomseq, test_xy
import test_collection, test_emptiness, test_singularity, test_validation
import test_mapping, test_delegated, test_dlls

def test_suite():
    suite = TestSuite()
    suite.addTest(test_doctests.test_suite())
    suite.addTest(test_prepared.test_suite())
    suite.addTest(test_emptiness.test_suite())
    suite.addTest(test_equality.test_suite())
    suite.addTest(test_geomseq.test_suite())
    suite.addTest(test_xy.test_suite())
    suite.addTest(test_collection.test_suite())
    suite.addTest(test_singularity.test_suite())
    suite.addTest(test_validation.test_suite())
    suite.addTest(test_mapping.test_suite())
    suite.addTest(test_delegated.test_suite())
    suite.addTest(test_dlls.test_suite())
    return suite

