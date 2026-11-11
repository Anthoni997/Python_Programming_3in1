#Population

def city_country(city, country, population=None):
    """Return a string formatted as 'City, Country' or 'City, Country - population xxx'."""
    base = f"{city.title()}, {country.title()}"
    if population:
        return f"{base} - population {population}"
    return base
