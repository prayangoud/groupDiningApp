class user:
    def __init__(self, userID):
        self.userID = userID
        
    def create_user(cursor, user_email, username, userpassword, user_firstname, user_lastname, user_age, user_address):
        create_new_user = "INSERT INTO User_Information (email, username, password, first_name, last_name, age, address) VALUES (?,?,?,?,?,?,?)"
        cursor.execute(create_new_user,(user_email, username, userpassword, user_firstname, user_lastname, user_age, user_address)) 
 
    #set user cuisine preferences
    def set_cuisine_preferences(self,cursor, userID, choices):
        cuisine_ids = []
        for choice in choices:
            cursor.execute("SELECT cuisineID FROM Cuisine_List WHERE cuisine_name = (?)", (choice,))
            cuisine_id = cursor.fetchone()
            if cuisine_id:
                cuisine_ids.append(cuisine_id)
            else:
                cuisine_ids.append(None)
        cursor.execute("INSERT INTO Cuisine_Preferences (userID,rank1,rank2,rank3,rank4,rank5) VALUES (?,?,?,?,?,?)",(userID, cuisine_ids[0][0], cuisine_ids[1][0], cuisine_ids[2][0], cuisine_ids[3][0], cuisine_ids[4][0]))
        

    #add user to group
    def join_group(self,cursor, userID, groupID):
        cursor.execute("INSERT INTO Group_Users (groupID, userID) VALUES (?,?)", (groupID, userID))

    #create group
    def create_group(self, cursor, userID,group_name):
        cursor.execute("INSERT INTO Group_Information (name) VALUES (?)", (group_name,))
        cursor.execute("SELECT groupID FROM Group_Information WHERE name = ?", (group_name,))
        groupID = cursor.fetchone()
        self.join_group(cursor, userID,groupID[0])
    
#view user preferences
    def view_preferences(self,cursor, userID):
        cursor.execute("SELECT rank1,rank2,rank3,rank4,rank5 FROM Cuisine_Preferences WHERE userID = ?", (userID,)) 
        print(cursor.fetchone())

#change user preferences
    def change_preferences(cursor, userID, choices):
        cuisine_ids = []
        for choice in choices:
            cursor.execute("SELECT cuisineID FROM Cuisine_List WHERE cuisine_name = (?)", (choice,))
            cuisine_id = cursor.fetchone()
            if cuisine_id:
                cuisine_ids.append(cuisine_id)
            else:
                cuisine_ids.append(None)
        cursor.execute("UPDATE Cuisine_Preferences SET rank1 = ?, rank2 = ?, rank3 = ?, rank4 = ?, rank5 = ? WHERE userID = ?",(cuisine_ids[0][0], cuisine_ids[1][0], cuisine_ids[2][0], cuisine_ids[3][0], cuisine_ids[4][0], userID))
   
#check if username and password match database entries 
def verify_password(cursor, username, password):
    cursor.execute("SELECT password FROM User_Information WHERE username = ?", (username,))
    if password == cursor.fetchone()[0]:
        return True
    else:
        return False

#get userID 
def get_userID(cursor, username):
    cursor.execute("SELECT userID FROM User_Information WHERE username = ?", (username,))
    id = cursor.fetchone()[0]
    if id:
        return(id)
    else:
        print("Could not find userID")
       

        
def change_settings(cursor, userID):
    while True:
        print("User settings Menu")
        print("------------------")
        print("1. Change first name")
        print("2. Change last name")
        print("3. Change email")
        print("4. Change username")
        print("5. Change age")
        print("6. Change address")
        print("7. Change password")
        print("8. Exit")
        print()
        choice = input("Access Setting: ")

        if choice == '1':
            change_firstname(cursor,userID)
            print("First Name changed!")
        elif choice == '2':
            change_lastname(cursor,userID)
            print("Last Name changed!")
        elif choice == '3':
            change_email(cursor,userID)
            print("Email changed!")
        elif choice == '4':
            change_username(cursor,userID)
            print("Username changed!")
        elif choice == '5':
            change_age(cursor,userID)
            print("Age changed!")
        elif choice == '6':
            change_address(cursor,userID)
            print("Address changed!")
        elif choice == '7':
            change_password(cursor,userID)
            print("Password changed!")
        elif choice == '8':
            print("Exiting settings...")
            break
        else:
            print("Invalid choice enter number")


def change_firstname(cursor, userID):
    new_firstname = input("Enter new first name: ")
    cursor.execute("UPDATE User_Information SET first_name = ? WHERE userID = ?",(new_firstname,userID))
    
    
def change_lastname(cursor, userID):
    new_lastname = input("Enter new last name: ")
    cursor.execute("UPDATE User_Information SET last_name = ? WHERE userID = ?",(new_lastname,userID))
    
    
def change_email(cursor, userID):
    new_email = input("Enter new email: ")
    cursor.execute("UPDATE User_Information SET email = ? WHERE userID = ?",(new_email,userID))
    
    
def change_username(cursor, userID):
    new_username = input("Enter new username: ")
    cursor.execute("UPDATE User_Information SET username = ? WHERE userID = ?",(new_username,userID))
    
    
def change_age(cursor, userID):
    new_age = input("Enter new age: ")
    cursor.execute("UPDATE User_Information SET age = ? WHERE userID = ?",(new_age,userID))
    
    
def change_address(cursor, userID):
    new_address = input("Enter new address: ")
    cursor.execute("UPDATE User_Information SET address = ? WHERE userID = ?",(new_address,userID))
    
    
def change_password(cursor, userID):
    while True:
        new_password = input("Enter new password: ")
        check_password = input("Re-enter password: ")
        if new_password == check_password:
            cursor.execute("UPDATE User_Information SET password = ? WHERE userID = ?",(new_password,userID))
            print("Password set")
            break
        else:
            print("Incorrect Password")
    
    