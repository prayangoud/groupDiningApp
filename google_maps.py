#pip install googlemaps (library)
import googlemaps

#Define our API Key
API_KEY = 'Insert API Key'

#Define our clients
gmaps = googlemaps.Client(key = API_KEY)

def co_lat(user_address):
    try:
        coordinate = gmaps.geocode(address = user_address)
        lat = coordinate[0]['geometry']['location']['lat']
        return(str(lat))
    except: 
        print("Coordinate Retrieval Failure: Address given is invalid")
        
def co_lng(user_address):
    try:
        coordinate = gmaps.geocode(address = user_address)
        lng = coordinate[0]['geometry']['location']['lng']
        return(str(lng))
    except: 
        print("Coordinate Retrieval Failure: Address given is invalid") 


        
