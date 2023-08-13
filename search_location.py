from google_maps import gmaps
import googlemaps


#set max price of group and ask for max price
def set_price():
    print("""
***********************
| Preferred Max Price |
***********************
| 1. Cheap            |
| 2. Moderate         |
| 3. Expensive        |
***********************
""")
    budget = input("Enter number of prefered pricing: ")
    if budget == '1':
        price = 0
    elif budget == '2':
        price = 2
    elif budget ==  '3':
        price = 4
    else:
        print("Invalid price choice. Please enter valid number")
    return price

    
    #search
def best_locations(search_param, location, max_price):
    group_suggestions = gmaps.places(query = search_param,location = location, radius = 40000 ,max_price = max_price, open_now = True, type = "restaurant" )
    for place in group_suggestions['results']:
            #place id
            place_id = place['place_id']
        
            fields = ['name','formatted_address', 'price_level', 'rating', 'opening_hours', 'formatted_phone_number', 'website']
        
            place_details = gmaps.place(place_id = place_id, fields = fields)
            #print(place_details)
            #for entry in place_details:
            result = place_details.get('result', {})
            name = result.get('name', 'N/A')
            open_hours = result.get('opening_hours', {}).get('weekday_text', [])
            address = result.get('formatted_address', 'N/A')
            price_level = result.get('price_level', 'N/A')
            rating = result.get('rating', 'N/A')
            website = result.get('website', 'N/A')
            phone_number = result.get('formatted_phone_number', 'N/A')
            print(f"Name: {name}")
            print(f"Open Hours: {', '.join(open_hours)}")
            print(f"Address: {address}")
            print(f"Price Level: {price_level}")
            print(f"Rating: {rating}")
            print(f"Website: {website}")
            print(f"Phone Number: {phone_number}")
            print("-----------------------------------------------------------------")

#best_locations('indian', '40.2887114,-74.46698789999999', 2)