# ===============================Numbers=================================
# Distance Between Two Cities - Calculates the distance between two cities
# and allows the user to specify a unit of distance.
# This program may require finding coordinates for the cities like latitude and longitude


from geopy import Nominatim
from geopy.distance import geodesic


def find_latitude_longitude(location):
    geolocator = Nominatim(user_agent="my_user_agent")
    location = geolocator.geocode(location)
    info = {'address': location.address,
            'latitude': location.latitude,
            'longitude': location.longitude}
    return info


def distance(first_location, second_location):
    interval = 0
    while True:
        user_choice = input("Specify a unit of distance (km/miles): ")
        if user_choice[0].lower() == 'k':
            interval = geodesic(first_location, second_location).km
            break
        elif user_choice[0].lower() == 'm':
            interval = geodesic(first_location, second_location).miles
            break
        else:
            print("Please provide from existing options!")
            continue
    return interval


def main():
    first_location = input("Enter a first address: ")
    second_location = input("Enter a second address: ")

    ''' Finding full info about two locations (type=dict) '''
    first_address = find_latitude_longitude(first_location)
    second_address = find_latitude_longitude(second_location)

    ''' Storing latitude and longitude of cities into tuple '''
    firstAddress = (first_address['latitude'], first_address['longitude'])
    secondAddress = (second_address['latitude'], second_address['longitude'])
    interval = distance(firstAddress, secondAddress)

    print(f"==========The_First_Location==========The_Second_Location========== \n"
          f"Addresses: {first_address['address']} || {second_address['address']} \n"
          f"Latitudes: {first_address['latitude']} || {second_address['latitude']} \n"
          f"Longitudes: {first_address['longitude']} || {second_address['longitude']} \n"
          f"The distance is {round(interval, 1)}")


if __name__ == '__main__':
    main()
