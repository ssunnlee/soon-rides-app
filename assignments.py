import googlemaps
from geopy.distance import geodesic

API_KEY = "AIzaSyBXjTrZ8E7OWtVxG4iJIV5LYdtFiQaaTmU"

def calculate_distance_google(address1, address2):
    gmaps = googlemaps.Client(key=API_KEY)

    geocode_result1 = gmaps.geocode(address1)
    coords1 = (geocode_result1[0]['geometry']['location']['lat'],
               geocode_result1[0]['geometry']['location']['lng'])

    geocode_result2 = gmaps.geocode(address2)
    coords2 = (geocode_result2[0]['geometry']['location']['lat'],
               geocode_result2[0]['geometry']['location']['lng'])

    distance = geodesic(coords1, coords2).kilometers
    return distance

if __name__ == "__main__":
    address1 = "15000 Arroyo Dr, Irvine, CA 92617"
    address2 = "2505 Yorba Linda Blvd, Fullerton, CA 92831"
    print(f"Distance: {calculate_distance_google(address1, address2)} km")
    # python3 assignments.py