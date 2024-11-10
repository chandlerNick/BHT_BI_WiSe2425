from geopy.geocoders import Nominatim


def coordinates_to_address(coordinates: tuple):
    '''
    Takes a tuple of coordinates and returns the address if found. 
    When not found, returns none
    '''
    geolocator = Nominatim(user_agent = 'my-app')

    location = geolocator.reverse(coordinates, exactly_one=True)

    if location:
        address = location.raw['address']
        city = address.get('city', '')
        county = address.get('county', '')
        state = address.get('state', '')
        print(f"City: {city}, County: {county}, State: {state}")
        print("Check the method desc for how to access the fields of address")
        return location.raw['address']
    else:
        print("Location not found. Returning None")
        return None
