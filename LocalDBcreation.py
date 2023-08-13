import sqlite3
class groupdiningDB:
    def __init__(self):
        #connect to database
        self.connection = sqlite3.connect('groupdining.db')
      
        #create cursor
        self.cursor = self.connection.cursor()

    def create(self,cursor):
        #connect to database
            
            
        #table for user information
        user_info = '''
        CREATE TABLE User_Information (
            userID integer primary key autoincrement,
            email text not null,
            username text not null,
            password text not null,
            first_name text not null,
            last_name text not null,
            age int not null,
            address text not null
        )
        '''
            
        #table for storing groups and their names
        group_info = '''
        CREATE TABLE Group_Information (
            groupID integer primary key autoincrement,
            name text not null
        )
        '''
            
        #table for storing groups and their users
        group_user = '''
        CREATE TABLE Group_Users (
            groupID integer not null,
            userID integer not null,
            foreign key(userID) references User_Information(userID),
            foreign key(groupID) references Group_Information(groupID)
        )
        '''
            
        #table for storing the food regions
        cuisine_group = '''
        CREATE TABLE Cuisine_Grouping (
            cuisine_groupID integer primary key autoincrement,
            cuisine_region text not null
        )
        '''
            
        #table for storing list of cuisines and their food region
        cuisine_list = '''
        CREATE TABLE Cuisine_List (
            cuisineID integer primary key autoincrement,
            cuisine_name text not null,
            cuisine_groupID integer not null,
            foreign key(cuisine_groupID) references Cuisine_Grouping(cuisine_groupID)
        )
        '''
            
        #table for storing users and their preferences
        cuisine_pref = '''
        CREATE TABLE Cuisine_Preferences(
            userID integer primary key,
            rank1 integer not null,
            rank2 integer not null,
            rank3 integer not null,
            rank4 integer not null,
            rank5 integer not null,
            foreign key(userID) references User_Information(userID),
            foreign key(rank1) references Cuisine_List(cuisineID),
            foreign key(rank2) references Cuisine_List(cuisineID),
            foreign key(rank3) references Cuisine_List(cuisineID),
            foreign key(rank4) references Cuisine_List(cuisineID),
            foreign key(rank5) references Cuisine_List(cuisineID)
        )
        '''
            
        #execution of table creation
        cursor.execute(user_info)
        cursor.execute(group_info)
        cursor.execute(group_user)
        cursor.execute(cuisine_group)
        cursor.execute(cuisine_list)
        cursor.execute(cuisine_pref)
          
        #inserting cuisine groups
        food_group = ["African", "American", "Asian", "Caribbean", "European", "Middle Eastern", "South American"]
        cursor.executemany("INSERT INTO Cuisine_Grouping (cuisine_region) VALUES (?)", [(group,) for group in food_group])
            
        #inserting list of cuisines
        cuisine_list = [("indian",3), ("chinese",3), ("japanese",3), ("indonesiann",3), ("thai",3), ("korean",3), ("filipino",3), ("taiwanese",3), ("cantonese",3), 
                            ("malayasian",3), ("bangladeshi",3), ("cambodian",3), ("vietnamese",3), ("egyptian",1), ("sudanese",1), ("tunisian",1), ("ghananian",1),
                            ("guinean",1), ("liberian",1), ("nigerian",1), ("libyan",1), ("moroccan",1), ("senegalese",1), ("gambian",1), ("mexican",7), ("brazilian",7), 
                            ("argentinian",7), ("ecuadorian",7), ("columbian",7), ("chilean",7), ("peruvian",7), ("venezuelan",7), ("uruguayan",7), ("paraguayan",7), 
                            ("bahamian",4), ("bermudian",4), ("dominican republic",4), ("guyanese",4), ("jamaican",4), ("puerto rican",4), ("haitian",4), ("austrian",5),
                            ("czech",5), ("hungarian",5), ("german",5), ("russian",5), ("romanian",5), ("bulgarian",5), ("moldovan",5), ("baltic",5), ("british",5), ("danish",5), ("finnish",5), 
                            ("french",5), ("norwegian",5), ("swedish",5), ("albanian",5), ("greek",5), ("italian",5), ("portuguese",5), ("spanish",5), ("belgian",5), ("dutch",5),
                            ("american",2), ("turkish",6), ("jordinian",6), ("iraqi",6), ("arabic",6)]
        cursor.executemany("INSERT INTO Cuisine_List (cuisine_name,cuisine_groupID) VALUES (?,?)", cuisine_list)
        
        self.connection.commit()
            
    
        
    def insert_samples(self,cursor):
        #insert users
        sample_user_list =[("john.smith@gmail.com","john.smith","J0hnSm!th","John","Smith","32","123 Main St, New York, NY"), 
                           ("emily.johnson@yahoo.com","emily.johnson","3milyJ0hnson","Emily","Johnson","26","456 Elm St, New York, NY"), 
                           ("michael.williams@hotmail.com","michael.williams","M1ch@elW","Michael","Williams","45","789 Oak St, New York, NY"), 
                           ("sarah.brown@gmail.com","sarah.brown"," S@rahBr0wn","Sarah","Brown","30","987 Maple Ave, New York, NY"), 
                           ("david.miller@yahoo.com","david.miller","D@vidM!ller","David","Miller","28","654 Birch Rd, New York, NY"), 
                           ("jessica.davis@gmail.com","jessica.davis","J3ss!caD","Jessica","Davis","22","321 Pine Ln, New York, NY"), 
                           ("christopher.anderson@hotmail.com","christopher.anderson","Chr1st0pherA","Christopher","Anderson","40","876 Cedar Pl, New York, NY"), 
                           ("amanda.wilson@gmail.com","amanda.wilson","@mand@Wils0n","Amanda","Wilson","29","543 Willow Dr, New York, NY"), 
                           ("daniel.martinez@yahoo.com","daniel.martinez","D@ni3lM","Daniel","Martinez","35","210 Spruce St, New York, NY"), 
                           ("olivia.taylor@hotmail.com","olivia.taylor","0liv!aT@ylor","Olivia","Taylor","31"," 765 Fir Blvd, New York, NY"),
                           ("test@email.com", "testuser", "testpassword", "demo", "user", "18", "1234 browadway, new york, NY")
                           ]
        cursor.executemany("INSERT INTO User_Information (email,username,password,first_name,last_name,age,address) VALUES (?,?,?,?,?,?,?)", sample_user_list)
        
        #insert preferences
        sample_preferences_list =[(1, 8, 12, 3, 5, 11),(2, 14, 7, 2, 6, 9),
                                  (3, 3, 10, 1, 13, 8),(4, 11, 6, 14, 4, 9),
                                  (5, 2, 12, 7, 15, 1),(6, 9, 5, 13, 8, 3),
                                  (7, 10, 1, 11, 4, 6),(8, 4, 15, 2, 12, 7),
                                  (9, 6, 13, 5, 3, 10),(10, 1, 8, 12, 7, 14)]
        cursor.executemany("INSERT INTO Cuisine_Preferences (userID,rank1,rank2,rank3,rank4,rank5) VALUES (?,?,?,?,?,?)", sample_preferences_list)
        
        #insert groups
        sample_group_list =["NYC Food Lovers", "Food Enthusiast"]
        cursor.executemany("INSERT INTO Group_Information (name) VALUES (?)", [(group,) for group in sample_group_list])
        
        #insert group users
        sample_group_users_list =[(1,4), (1,1), 
                                  (1,8), (1,10), 
                                  (1,6), (2,2),  
                                  (2,3), (2,4), 
                                  (2,7), (2,9),
                                  (1,11),(2,11)]
        cursor.executemany("INSERT INTO Group_Users (groupID, userID) VALUES (?,?)", sample_group_users_list)
        
        #cursor.execute("SELECT * FROM User_Information")
        #print(cursor.fetchall())
        #cursor.execute("SELECT * FROM Group_Information")
        #print(cursor.fetchall())
        #cursor.execute("SELECT * FROM Group_Users")
        #print(cursor.fetchall())
        #cursor.execute("SELECT * FROM Cuisine_Preferences")
        #print(cursor.fetchall())
        
        self.connection.commit()
    

        
#test_run = groupdiningDB()
#test_run.create(test_run.cursor)
#test_run.insert_samples(test_run.cursor)



        




            
            
          