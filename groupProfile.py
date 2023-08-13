from google_maps import gmaps
import google_maps
from userProfile import user

class group:
    def __init__(self, groupid):
        self.groupid = groupid

    #alogrithm to go through users and get their ranks and create a combined rank
    def get_pref_cuisine(self,cursor,groupID):
        #get group id
        
        find_rank = '''
        SELECT Cuisine_Preferences.userID, Cuisine_Preferences.rank1, Cuisine_Preferences.rank2, Cuisine_Preferences.rank3, Cuisine_Preferences.rank4, Cuisine_Preferences.rank5
        FROM Group_Users
        JOIN Cuisine_Preferences ON Group_Users.userID = Cuisine_Preferences.userID
        WHERE Group_Users.groupID = ?
        '''
        cursor.execute(find_rank, str(groupID))
        
        group = cursor.fetchall()
        
        cuisine_counter = {}
        for profile in group:
            ranks = profile[1:]
            
            for cuisine in ranks:
                cuisine_counter[cuisine] = cuisine_counter.get(cuisine,0) + 1
                
        top_cuisine = max(cuisine_counter, key=cuisine_counter.get)
        
        #query in cuisine list to return string name of cuisine 
        cursor.execute("SELECT cuisine_name FROM Cuisine_List WHERE cuisineID = ?", (top_cuisine,))
        cuisine_name = cursor.fetchone()
        return cuisine_name[0]
    
   
    def get_coordinates(self,cursor,groupID):
        find_address = '''
        SELECT User_Information.address
        FROM Group_Users
        JOIN User_Information ON Group_Users.userID = User_Information.userID
        WHERE Group_Users.groupID = ?
        '''
        cursor.execute(find_address, str(groupID))
        
        group_address = cursor.fetchall()
        addresses = [address[0] for address in group_address]
        
        group_lat = 0
        group_lng = 0
        
        for address in addresses:
            lat = google_maps.co_lat(address)
            lng = google_maps.co_lng(address)
            group_lat += float(lat)
            group_lng += float(lng)
            
        final_lat = group_lat / len(addresses)
        final_lng = group_lng / len(addresses)
   
        return (str(final_lat) + ',' + str(final_lng))  

def view_groups(cursor, userID):
    find_groups = '''
        SELECT Group_Information.name
        FROM Group_Users
        JOIN Group_Information ON Group_Users.groupID = Group_Information.groupID
        WHERE Group_Users.userID = ?
        '''
    cursor.execute(find_groups, (userID,) )
        
    group_names = cursor.fetchall()
    group_list = []
    for group_name in group_names:
        group_list.append(group_name[0])
    return group_list

def view_groupID(cursor, userID):
    find_groups = '''
        SELECT Group_Information.groupID
        FROM Group_Users
        JOIN Group_Information ON Group_Users.groupID = Group_Information.groupID
        WHERE Group_Users.userID = ?
        '''
    cursor.execute(find_groups, (userID,) )
        
    group_names = cursor.fetchall()
    group_list = []
    for group_name in group_names:
        group_list.append(group_name[0])
    return group_list
    
def find_group(cursor, groupID):
    find_groups = '''
        SELECT name FROM Group_Information WHERE groupID = ?
        '''
    cursor.execute(find_groups, (groupID,) ) 
    group_name = cursor.fetchone()[0]
    return group_name

    
      
        
    

                
        

        