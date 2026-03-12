guest = []


def ask_name():  # This function asks the user for their name and add it to the list.
    name = input("Enter your name: ").strip().title()
    guest.append(name)


""" Reject double names """


def welcome_user():  # It welcomes user, to the dinner party.
    print(f"Hello, {guest [-1]}. Welcome to the dinner party.")


def features():  # This function shows all the features from which the user can choose one.
    print("\n1 - Add guest")
    print("2 - Modify guest")
    print("3 - Remove guest")
    print("4 - Sort guests")
    print("5 - Show number of guests")
    print("6 - Show invitations")
    print("0 - Exit")


def add_guest():  # It adds a user to the list
    guest_name = input("Enter the name of guest: ").strip().title()
    guest.append(guest_name)
    print("Guest added")
    print(f"New guest: {guest_name}")


def modify_guest():  # It modifies the user name, if it belongs in the list
    old_name = input("Enter the name of guest: ").strip().title()
    if old_name in guest:
        new_name = input("Enter the new name: ").strip().title()
        index = guest.index(old_name)
        guest[index] = new_name
        print("Guest name modified")
        print(f"New modified name: {new_name} ")


def remove_guest():  # It removes a guest from the list, if the guest remains on the list.
    guest_name = input("Enter the name of guest to remove: ").strip().title()
    if guest_name in guest:
        guest.remove(guest_name)
        print("Guest removed.")
    if not guest_name in guest:
        print("Guest is not included in the list.")


def sort_guest():  # It will sort the guests in alphabetical order.
    guest.sort()
    print("Guest sorted.")


def show_guest():  # It will show the total number of guests.
    number = len(guest)
    print(f" Total number of guests in the list are: {number}.")


def show_invitations():  # It will collect information from user and print it as an invitation.
    guest_name = input(
        "Enter your name: "
    )  # check if the name exists in the list or not , if not then loop the process
    print(guest_name)
    while True:
        if guest_name not in guest:
            return (
                input("Guest name doesn't exist in the list. Enter a new name: ")
                .strip()
                .title()
            )
        break
    pronoun = input("Enter suitable pronoun (he/him or she/her): ")
    print(f"You are {pronoun}")
    allergy = input("Is the person allergic to something?")
    print("Allergy info: ", allergy)

    extra_people = print(input("Are you bringing someone along? (yes or no)"))
    if extra_people == "yes":
        try:
            print(int(input("How many people are there?")))
        except ValueError:
            print("Please type in a number.")
    elif extra_people == "no":
        print("Thanks for your information.")
    else:
        print("Please type in yes or no.")

    # makes  new invitation if they are bringing someone
    """ additional information """


def main():
    """The program will ask the user for their name, give them access to multiple options, by which they can add guest, modify guest, sort guest, remove guest, see number of guests and print the invitation."""

    # ask the user for his name
    ask_name()
    # welcome the user to the dinner.
    welcome_user()
    # ask the user to choose from the options

    # based on the choice the user made run features
    """Runs based on the choice user made."""
    # features

    # Add guests
    while True:
        features()
        choice = input("Choose from the options above.").strip()
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
            print("Goodbye! Have a great day.")
            break
        else:
            print("Please enter a number according to the features.")


if __name__ == "__main__":
    main()
