#City, Country — Test File

from city_functions import city_country


def test_city_country():
    """Test that city_country() returns the correct format."""
    result = city_country("santiago", "chile")
    assert result == "Santiago, Chile"


def test_city_country_uppercase():
    """Test that the function handles uppercase input correctly."""
    result = city_country("JAKARTA", "INDONESIA")
    assert result == "Jakarta, Indonesia"


def test_city_country_mixed_case():
    """Test that the function handles mixed case input correctly."""
    result = city_country("new york", "united states")
    assert result == "New York, United States"
