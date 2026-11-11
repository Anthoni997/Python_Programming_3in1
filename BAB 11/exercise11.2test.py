#Population — Test File

from city_functions import city_country


def test_city_country():
    """Test that city_country() works without population."""
    result = city_country("santiago", "chile")
    assert result == "Santiago, Chile"


def test_city_country_population():
    """Test that city_country() works with a population argument."""
    result = city_country("santiago", "chile", population=5_000_000)
    assert result == "Santiago, Chile - population 5000000"


def test_city_country_jakarta():
    """Test another city-country pair."""
    result = city_country("jakarta", "indonesia")
    assert result == "Jakarta, Indonesia"


def test_city_country_jakarta_population():
    """Test a city-country pair with population."""
    result = city_country("jakarta", "indonesia", population=10_562_000)
    assert result == "Jakarta, Indonesia - population 10562000"
