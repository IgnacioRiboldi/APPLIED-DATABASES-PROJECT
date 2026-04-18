import Database

def main_menu():
    print ("Conference Management")
    print ("------------------------")
    print(" ")
    print("MENU")
    print("====")
    print ("1 - View Speakers & Sessions")
    print ("2 - View Attendees by company")
    print ("3 - Add New Attendee")
    print ("4 - View Connected Attendees")
    print ("5 - Add Attendee Connection")
    print ("6 - View Rooms")
    print ("x - Exit Application")
    
    return input("Choice: ")

if __name__ == "__main__":
    main_menu()