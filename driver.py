from LocalDBcreation import groupdiningDB
from userProfile import user
import userProfile
import cuisines_display
from cuisines_display import cuisines
import groupProfile
from groupProfile import group
import search_location


class GroupDiningApp:
    def __init__(self):
        self.db = groupdiningDB()
        self.cursor = self.db.cursor
        self.db.create(self.cursor)
        self.db.insert_samples(self.cursor)
        
    def start(self):
        print('''
  ________                            ________  .__       .__                
 /  _____/______  ____  __ ________   \______ \ |__| ____ |__| ____    ____  
/   \  __\_  __ \/  _ \|  |  \____ \   |    |  \|  |/    \|  |/    \  / ___\ 
\    \_\  \  | \(  <_> )  |  /  |_> >  |    `   \  |   |  \  |   |  \/ /_/  >
 \______  /__|   \____/|____/|   __/  /_______  /__|___|  /__|___|  /\___  / 
        \/                   |__|             \/        \/        \//_____/ 
      ''')
        print("Welcome to the Group Dining Application!\n"
              "There is a preloaded environment with already existing users and groups to allow you to test out the application.\n"
              "Begin by logging into the demo account")
        print('''
        demo account details:
        username:testuser
        password:testpassword
        ''')

        while True:
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            try:
                if userProfile.verify_password(self.cursor, username, password):
                    self.new_user = user(userProfile.get_userID(self.cursor, username))
                    break
            except:
                print("Invalid Username or Password")

        print()
        print("Choose from a list of cuisines you like: ")
        print("***********************************************************")
        cuisines_display.display_cuisines()
        print()
        print("Enter the number of the cuisine you prefer (Five choices): ")
        print("***********************************************************")

        choices = []
        for _ in range(5):
            while True:
                try:
                    choice = int(input(f"Enter choice {_ + 1}: "))
                    if choice <= len(cuisines):
                        cuisine = cuisines[choice - 1]
                        choices.append(cuisine.lower())
                        break
                    else:
                        print("Invalid number. Enter a valid number.")
                except:
                    print("Invalid input. Enter a number.")

        self.new_user.set_cuisine_preferences(self.cursor, self.new_user.userID, choices)

        while True:
            print("""
*******************
|    Main Menu    |
*******************
| 1. View Groups  |
| 2. Join/Create  |
|    Groups       |
| 3. Change       |
|    Settings     |
| 4. Exit         |
*******************
""")
            choice = input("Enter choice: ")
            print("*****************")

            if choice == '1':
                group_list = groupProfile.view_groups(self.cursor, str(self.new_user.userID))
                group_listID = groupProfile.view_groupID(self.cursor, str(self.new_user.userID))    
                for index, groups in enumerate(group_list, start=1):
                    print(f"{index}. {groups}")
                print()
                while True:
                    choice = input("Select group: ")
                    print()
                    assign_group = group_list[int(choice)-1]
                    assign_groupID = group_listID[int(choice)-1]
                    #using selected group get group id
                    search_group = group(int(assign_groupID))
                    location = search_group.get_coordinates(self.cursor, search_group.groupid)
                    cuisine = search_group.get_pref_cuisine(self.cursor,search_group.groupid)
                    max_price = search_location.set_price()
                    print()
                    print("Recommended places for the " + assign_group + ": ")
                    print("***********************************************************")
                    results = search_location.best_locations(cuisine, location, max_price)
                    #result1 = search_location.best_locations('chinese restuarants', location, 2)
                    break
                
            elif choice == '2':
                print('''
*******************
|   Group Menu    |
*******************
| 1. Join Group   |
| 2. Create Group |
| 3. Exit         |
*******************
''')
                choice = input("Enter choice: ")
                if choice == '1':
                    while True: 
                        groupID = input("Enter group ID(enter e to exit): ")
                        if groupID == 'e':
                            break
                        try: 
                            self.new_user.join_group(self.cursor, self.new_user.userID, groupID)
                            group_name = groupProfile.find_group(self.cursor, groupID)
                            print("Group" + group_name + "joined!")
                            break
                        except:
                            print("Could not find group")
            
                elif choice == '2':
                    while True:
                        group_name = input("Name the group: ")
                        self.new_user.create_group(self.cursor, self.new_user.userID, group_name)
                        print(group_name + " created!")
                        break
                elif choice == '3':
                    break
                else:
                    print("Invalid choice")
                
            elif choice == '3':
                userProfile.change_settings(self.cursor, self.new_user.userID)
                
            elif choice == '4':
                print("Exiting Menu and ending application")
                break
                
            else:
                print("Invalid Choice")

app = GroupDiningApp()
app.start()
