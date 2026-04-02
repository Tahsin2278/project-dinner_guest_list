host = ""
guest = []
extra_guests = {}


def ask_name():  # This function asks the user for their name and add it to the list.
    global host  # global variable
    while True:
        name = input("Enter your name: ").strip().title()

        if not name:  # Name can't be empty
            print("Name cannot be empty.")
            continue

        if name in guest:  # Prevents double names
            print("Name already exists. Try again.")
        else:
            host = name
            break


""" Reject double names """


def welcome_user():  # It welcomes user, to the dinner party.
    print(f"Hello, {host}. Welcome to the dinner party.")


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
    if not guest_name:  # Name can't be empty
        print("Name cannot be empty.")

    elif guest_name in guest:  # Prevents double name
        print("Guest already exists")
    else:
        guest.append(guest_name)
        extra_guests[guest_name] = 0
        print("Guest added")
        print(f"New guest: {guest_name}")


def modify_guest():
    old_name = input("Enter the name of guest: ").strip().title()

    if old_name in guest:
        new_name = input("Enter the new name: ").strip().title()
        if not new_name:  # Name can't be empty
            print("Name cannot be empty.")
        elif new_name in guest:  # Prevents double name
            print("That name already exists.")
        else:
            index = guest.index(old_name)
            guest[index] = new_name
            # keep extra guest data in sync
            extra_guests[new_name] = extra_guests.pop(old_name, 0)
            print("Guest name modified")
            print(f"New modified name: {new_name}")
    else:
        print("Guest name not found")


def remove_guest():  # It removes a guest from the list, if the guest remains on the list.
    guest_name = input("Enter the name of guest to remove: ").strip().title()
    if guest_name in guest:
        guest.remove(guest_name)
        extra_guests.pop(guest_name, 0)
        print("Guest removed.")
    else:
        print("Guest is not included in the list")


def sort_guest():  # It will sort the guests in alphabetical order.
    guest.sort()
    print("Sorted guests:", guest)


def show_guest():  # It will show the total number of guests.
    main_count = len(guest)
    extra_count = sum(extra_guests.values())
    total = main_count + extra_count

    print(f"Main guests: {main_count}")
    print(f"Extra guests: {extra_count}")
    print(f"Total people attending: {total}")


def show_invitations():  # It will collect information from user and print it as an invitation.
    if not guest:
        print("No guests available.")
        return

    print("Guest list:", guest)
    while True:
        guest_name = (
            input("Select a guest from the list: ").strip().title()
        )  # check if the name exists in the list or not , if not then loop the process

        if guest_name in guest:
            break
        else:
            print("Guest name doesn't exist. Please try again.")
    while True:
        pronoun = input("Enter suitable pronoun (he/him or she/her): ").strip()
        if pronoun in ["he/him", "she/her"]:
            break
        else:
            print("Please enter suitable pronoun")
    allergy = input("Is the person allergic to something? ").strip()
    while True:
        extra_people = (
            input("Are you bringing someone along? (yes or no)").strip().lower()
        )
        if extra_people in ["yes", "no"]:
            break
        else:
            print("Please type yes or no.")

    if extra_people == "yes":
        while True:
            try:
                extra_count = int(input("How many people are there?"))
                break
            except ValueError:
                print("Please type in a number.")
    else:
        extra_count = 0

    # store extra_guests
    extra_guests[guest_name] = extra_count

    print("\n--- Invitation ---")
    print(f"Dear {guest_name},")
    print("You are invited to the dinner party!")
    print(f"Pronouns: {pronoun}")
    print(f"Allergies: {allergy if allergy else 'None'}")

    if extra_count > 0:
        print(f"You are bringing {extra_count} guest(s).")
    else:
        print("No additional guests.")

    print("We look forward to seeing you.")

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
