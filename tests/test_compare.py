"""Test compare."""
import pytest

from awesomeversion import AwesomeVersion
from awesomeversion.exceptions import AwesomeVersionCompare


def test_invalid_compare():
    """Test invalid compare."""
    with pytest.raises(
        AwesomeVersionCompare, match="Not a valid AwesomeVersion object"
    ):
        assert AwesomeVersion("2020.12.1") > "2020.12.0"

    with pytest.raises(
        AwesomeVersionCompare, match="Not a valid AwesomeVersion object"
    ):
        assert AwesomeVersion("2020.12.1") < "2020.12.0"

    with pytest.raises(
        AwesomeVersionCompare, match="Not a valid AwesomeVersion object"
    ):
        assert AwesomeVersion("2020.12.1") == "2020.12.0"

    with pytest.raises(AwesomeVersionCompare, match="Can't compare unknown"):
        assert AwesomeVersion("2020.12.1") > AwesomeVersion("latest")

    with pytest.raises(AwesomeVersionCompare, match="Can't compare unknown"):
        assert AwesomeVersion("2020.12.1") < AwesomeVersion("latest")


def test_compare():
    """Test compare."""
    assert AwesomeVersion("2020.12.1") > AwesomeVersion("2020.12.0")
    assert AwesomeVersion("2020") > AwesomeVersion("2019")
    assert AwesomeVersion("1.2.3.4") > AwesomeVersion("1.2.3")
    assert AwesomeVersion("2020.1") > AwesomeVersion("2020")
    assert AwesomeVersion("2020.2.0") > AwesomeVersion("2020.1.1")
    assert AwesomeVersion("2021.1.0") > AwesomeVersion("2021.1.0b0")
    assert AwesomeVersion("2021.2.0") > AwesomeVersion("2021.1.0b0")
    assert AwesomeVersion("2021.2.0b0") > AwesomeVersion("2021.1.0")
    assert AwesomeVersion("2021.1.0") > AwesomeVersion("2021.1.0b1")
    assert AwesomeVersion("2021.1.0") > AwesomeVersion("2021.1.0dev20210101")

    assert AwesomeVersion("2020.12.0") < AwesomeVersion("2020.12.1")
    assert AwesomeVersion("2019") < AwesomeVersion("2020")

    assert not AwesomeVersion("2019") > AwesomeVersion("2020")
    assert not AwesomeVersion("2021.1.0b0") > AwesomeVersion("2021.1.0")
    assert AwesomeVersion("1.2.3.4.5.6.7.8.9") > AwesomeVersion("1")