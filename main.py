import Database


def main_menu():
    print("\nConference Management")
    print("------------------------")
    print("\nMENU")
    print("====")
    print("1 - View Speakers & Sessions")
    print("2 - View Attendees by company")
    print("3 - Add New Attendee")
    print("4 - View Connected Attendees")
    print("5 - Add Attendee Connection")
    print("6 - View Rooms")
    print("x - Exit Application")

    return input("Choice: ")


if __name__ == "__main__":

    while True:
        choice = main_menu()

        if choice == "1":
            Database.view_speakers_sessions()

        elif choice == "2":
            Database.view_attendees_by_company()

        elif choice == "3":
            Database.add_new_attendee()

        elif choice == "4":
            Database.view_connected_attendees()

        elif choice == "5":
            Database.add_attendee_connection()

        elif choice == "6":
            Database.view_rooms()

        elif choice.lower() == "x":
            print("See you next time!")
            break

        else:
            print("*** ERROR *** Invalid option")