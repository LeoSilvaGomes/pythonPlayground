
def get_city_country(city, country, population=''):
    '''Retorna o nome de uma pais, cidade e sua populacao'''
    if population:
        both = city.title() + ' ' + country.title() + ' - populacao ' + population
    else:
        both = city.title() + ' ' + country.title()
    
    return both