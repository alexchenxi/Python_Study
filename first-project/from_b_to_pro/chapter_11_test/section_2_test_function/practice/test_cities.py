from city_function import city_country


def test_city_country():
    """Test city_country() works with simple input."""
    assert city_country("santiago", "chile") == "Santiago, Chile"


def test_city_country_population():
    """Test city_country() works with input with population."""
    assert (
        city_country("santiago", "chile", "5000000")
        == "Santiago, Chile - population 5000000"
    )
