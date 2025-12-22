from name_function import get_formatted_name


def test_get_formatted_name():
    """Test names like 'Janis Joplin'."""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"


def test_get_formatted_name_with_middle():
    """Test names like 'Wolfgang Amadeus Mozart'."""
    formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"
