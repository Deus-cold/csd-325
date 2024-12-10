
def city_country(city, country, population=None, language=None):
    """Return a string formatted as 'City, Country' or
     'City, Country - population xxx, Language' if population and language are not provided they are omitted.
     """
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"

    return result

    


# Call the function with three examples or without population
print(city_country("santiago", "chile", 5000000, "spanish"))
print(city_country("paris", "france", 2148327, "french"))
print(city_country("tokyo", "japan", 13929286, "japanese"))
print(city_country("new york", "usa", language="english"))
