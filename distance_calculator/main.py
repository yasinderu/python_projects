from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

@dataclass
class Coordinate:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude
    
def get_coordinates(address: str) -> Coordinate | None:
    geolocator = Nominatim(user_agent='distance_calculator')
    location = geolocator.geocode(address)

    if location:
        return Coordinate(latitude=location.latitude, longitude=location.longitude)
    
def calculate_distance_km(home: Coordinate, target: Coordinate) -> float | None:
    if home and target:
        distance: float = geodesic(home.coordinates(), target.coordinates()).kilometers
        return distance
    
def get_distance_km(home: str, target: str) -> float | None:
    home_coodinates: Coordinate = get_coordinates(home)
    target_coodinates: Coordinate = get_coordinates(target)

    if distance := calculate_distance_km(home_coodinates, target_coodinates):
        print(f'{home} -> {target}')
        print(f'{distance:.2f} kilometers')
        return distance
    else:
        print(f'Failed to calculate distance')
    
def main():
    home_address: str = 'london'
    print(f'home address: {home_address}\n')
    target_address: str = input('Please enter destination address: ')
    # print(get_coordinates(target_address))
    # print(get_coordinates(home_address))

    get_distance_km(home_address, target_address)

if __name__ == '__main__':
    main()