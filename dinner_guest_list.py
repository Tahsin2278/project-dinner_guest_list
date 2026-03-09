guest = []


def ask_name():
    try:
        name = input("Enter your name: ").strip().title()
    except ValueError:
        print("Invalid name. Please enter a valid name.")
    guest.append(name)


""" Reject double names """


def welcome_user():
    print(f"Hello, {guest}. Welcome to the dinner.")


def add_guest():
    guest_name = input("Enter the name of guest: ").strip().title()
    guest.append(guest_name)


def modify_guest():
    guest_name = input("Enter the correct guest name: ").strip().title()
    guest.append(guest_name)


def remove_guest():
    guest_name = input("Enter the name of guest to remove: ").strip().title()
    if guest_name in guest:
        guest.remove(guest_name)
    if not guest:
        print("Guest is not included in the list")


def sort_guest(guest: list, name: str):
    if name in guest.isalpha():
        guest.sort


def main():
    # ask the user for his name
    ask_name()
    # welcome the user to the dinner.
    welcome_user()
    # ask the user to choose from the options
    choice = input("Choose from the options below.")
    print(choice)
    # based on the choice the user made run features
    """Runs based on the choice user made."""
    # features
    print("\n1 - Add guest")
    print("2 - Modify guest")
    print("3 - Remove guest")
    print("4 - Sort guests")
    print("5 - Show number of guests")
    print("6 - Show invitations")
    print("0 - Exit")
    # Add guests
    while True:
        if choice == "1":
            add_guest()
        # Modify guest.
        elif choice == "2":
            modify_guest()
        # Remove guest.
        elif choice == "3":
            remove_guest()
        # Sort guests.
        elif choice == "4":
            sort_guest()
        # Show number of guests.
        elif choice == "5":
            show_guest()
        # Show invitations.
        elif choice == "6":
            show_invitations()
        # exit
        elif choice == "0":
            break
        else:
            print("Please enter a number according to the features.")

    if __name__ == "__main__":
        main()
