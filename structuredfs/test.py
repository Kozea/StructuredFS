
from . import FOO
from attest import Tests

SUITE = Tests()

@SUITE.test
def foo():
    assert FOO == 4

