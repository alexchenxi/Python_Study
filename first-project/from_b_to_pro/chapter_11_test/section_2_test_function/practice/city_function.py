def city_country(city, country, population=""):
    """Return a string like 'Santiago, Chile'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
