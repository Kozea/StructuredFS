"""

Tests for StructuredFS.

"""


from attest import Tests

from . import StructuredDirectory


SUITE = Tests()

@SUITE.test
def test_parser():
    """
    Test the pattern parser.
    """
    directory = StructuredDirectory('.', '{category}/{number}_{name}.txt')
    assert directory.properties == set(['category', 'number', 'name'])
