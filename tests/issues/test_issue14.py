"""Test for issue #14."""
# https://github.com/ludeeus/awesomeversion/issues/14
from awesomeversion.strategy import AwesomeVersionStrategy
from awesomeversion import AwesomeVersion


def test():
    """Test for issue #14."""
    version = AwesomeVersion("2021.1.0.dev20201230")
    assert version.dev
    assert version.strategy != AwesomeVersionStrategy.UNKNOWN