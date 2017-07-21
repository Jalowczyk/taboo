import datetime
from view.view import View
from model.events import *
import sys

class Controller:

    def start_menu_action(self):
        """
        Prints menu and reacts depends on user choice.
        """

        options = ["book private mentoring", "book checkpoint", "show all events",
                   "remove an event", "reschedule an event", "exit"]
        View.print_main_menu(options)

        choice = View.get_menu_choice(options)

        if choice == "book private mentoring":
            self.book_private_mentoring_action()
        elif choice == "book checkpoint":
            self.book_checkpoint_action()
        elif choice == "show all events":
            self.print_all_events_action()
        elif choice == "remove an event":
            self.remove_event_action()
        elif choice == "reschedule an event":
            self.reschedule_event_action()
        elif choice == "exit":
            return "exit"

    def print_all_events_action(self):
        """
        Prints all events.
        """
        events = Event.get_events()
        View.print_all_events(events)

    def remove_event_action(self):
        """
        Remove event depend on user's choice.
        """
        events = Event.get_events()

        if events:
            View.print_all_events(events)
            event = View.get_event_choice(events)
            Event.remove_event(event)
            
            if event.__class__.__name__ == "PrivateMentoring":
                PrivateMentoring.remove_event(event)
            else:
                Checkpoint.remove_event(event)

            View.print_message("Event removed.")
        else:
            View.print_message("There are no events!")

    def reschedule_event_action(self):
        """
        Reschedule event depend on user's choice.
        """
        events = Event.get_events()
        if events:
            View.print_all_events(events)
            event = View.get_event_choice(events)
            try:
                date = View.get_event_date()
                date = self.convert_date(date)
            except ValueError:
                View.print_message("Sorry, date like this doesn't exist. Try again.")
            else:
                event.set_date(date)
                View.print_message("Event rescheduled.")
        else:
            View.print_message("There are no events!")

    def book_checkpoint_action(self):
        """
        Creates Checkpoint obj depend on user's input.
        """
        try:
            date = View.get_event_date()
            date = self.convert_date(date)
        except ValueError:
            View.print_message("Sorry, date like this doesn't exist. Try again.")
        else:
            checkpoint = Checkpoint(date)

    def book_private_mentoring_action(self):
        """
        Creates PrivateMentoring obj depend on user's input.
        """
        mentors = PrivateMentoring.get_mentors()

        try:
            date = View.get_event_date()
            date = self.convert_date(date)
        except ValueError:
            View.print_message("Sorry, date like this doesn't exist. Try again.")
        else:
            View.print_mentors(mentors)
            preffered_mentor = View.get_preffered_mentor(mentors)
            goal = View.get_goal()
            private_mentoring = PrivateMentoring(date, preffered_mentor, goal)

    def say_goodbye_action(self):
        """
        Prints goodbye.
        """
        View.print_message("Bye, bye!")

    @staticmethod
    def convert_date(date_str):
        """
        Convert date str to Date obj date.
        """
        date_list = date_str.split("-")

        return datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
