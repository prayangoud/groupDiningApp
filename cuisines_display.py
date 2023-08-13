cuisines = ["Indian", "Chinese", "Japanese", "Indonesiann", "Thai", "Korean", "Filipino", "Taiwanese", "Cantonese", 
                            "Malayasian", "Bangladeshi", "Cambodian", "Vietnamese", "Egyptian", "Sudanese", "Tunisian", "Ghananian",
                            "Guinean", "Liberian", "Nigerian", "Libyan", "Moroccan", "Senegalese", "Gambian", "Mexican", "Brazilian", 
                            "Argentinian", "Ecuadorian", "Columbian", "Chilean", "Peruvian", "Venezuelan", "Uruguayan", "Paraguayan", 
                            "Bahamian", "Bermudian", "Dominican Republic", "Guyanese", "Jamaican", "Puerto Rican", "Haitian", "Austrian",
                            "Czech", "Hungarian", "German", "Russian", "Romanian", "Bulgarian", "Moldovan", "Baltic", "British", "Danish", "Finnish", 
                            "French", "Norwegian", "Swedish", "Albanian", "Greek", "Italian", "Portuguese", "Spanish", "Belgian", "Dutch",
                            "American", "Turkish", "Jordinian", "Iraqi", "Arabic"]
def display_cuisines():
    columns = round(len(cuisines)/2)
    for i in range(columns):
        left_item = cuisines[i]
        right_item = cuisines[i + columns] if i + columns < len(cuisines) else ""
        print(f"{i + 1:2}. {left_item:20} | {i + 1 + columns:2}. {right_item:20}")
    for i in range(columns * 2, len(cuisines)):
        print(f"{i + 1:2}. {cuisines[i]:20}")
        
