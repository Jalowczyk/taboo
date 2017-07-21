import re
class View:

    @staticmethod
    def print_all_events(events):
        """
        Prints all events.
        Parameters:
            events: list
        """
        print("\nEVENTS:")
        for index, event in enumerate(events):
            print("{}. {}".format(index + 1, event))

    @staticmethod
    def print_main_menu(options):
        """
        Prints menu options.
        Parameters:
            options: list
        """

        print("\nMAIN MENU:")
        for index, option in enumerate(options):
            print("{}. {}".format(index + 1, option))

    @staticmethod
    def print_mentors(mentors):
        """
        Prints mentors fullnames.
        Parameters:
            mentors: list
        """
        print("\nMENTORS:")
        for index, mentor in enumerate(mentors):
            print("{}. {}".format(index + 1, mentor))

    @staticmethod
    def print_message(message):
        """
        Prints message.
        """
        print("\n" + message)

    @staticmethod
    def get_menu_choice(options):
        """
        Get numeric input from the user and convert it to str menu option.
        Parameters:
            options: list
        Returns:
            user_string_choice: str
        """

        user_number_choice = input("\nEnter menu option: ")
        while not user_number_choice.isnumeric() or int(user_number_choice) not in range(1, len(options) + 1):
            user_number_choice = input("\nInvalid menu option. Enter menu option again: ")

        user_string_choice = options[int(user_number_choice) - 1]
        return user_string_choice

    @staticmethod
    def get_event_choice(events):
        """
        Get numeric input from the user and based on pick appropriate obj.
        Parameters:
            events: list
        Returns:
            user_obj_choice: Event obj
        """

        user_event_choice = input("\nEnter choosen event: ")
        while not user_event_choice.isnumeric() or int(user_event_choice) not in range(1, len(events) + 1):
            user_event_choice = input("\nInvalid choice. Enter choosen event again: ")

        user_obj_choice = events[int(user_event_choice) - 1]
        return user_obj_choice



    @staticmethod
    def get_event_date():
        """
        Get string input from the user and returns is.
        Returns:
            user_input_date: str
        """
        user_input_date = input("Enter the date yyyy-mm-dd: ")

        while not re.search(r"\d{4}-((0[1-9]|1[0-2])){1}-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$", user_input_date):
            user_input_date = input("Invalid date. Enter the date yyyy-mm-dd again: ")

        return user_input_date


    @staticmethod
    def get_preffered_mentor(mentors):
        """
        Get numeric input from the user and based on pick appropriate obj.
        Parameters:
            events: list
        Returns:
            user_string_choice: str
        """

        user_mentor_choice = input("\nEnter preffered mentor's number: ")
        while not user_mentor_choice.isnumeric() or int(user_mentor_choice) not in range(1, len(mentors) + 1):
            user_mentor_choice = input("\nInvalid mentor's number. Enter preffered mentor's number again: ")

        user_string_choice = mentors[int(user_mentor_choice) - 1]
        return user_string_choice


    @staticmethod
    def get_goal():
        """
        Get string input from the user and returns it.
        """

        return input("Enter you goal: ")
