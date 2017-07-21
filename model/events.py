class Event:
    """
    Creates Event obj.

    Class attributes:
        events: list

    Instance attributes:
        date: Date obj
    """

    events = []

    def __init__(self, date):
        """
        Creates Event obj.
        Parameters:
            date: Date object
        """
        self.date = date

    def get_date(self):
        """
        Returns instance attribute date.
        Returns:
            date: Date obj
        """
        return self.date

    def set_date(self, date):
        """
        Set instance attribute date to date.
        Parameters:
            date: Date obj
        """
        self.date = date

    @classmethod
    def sort_events(cls):
        """
        Sorts events on events list by date.
        """
        cls.events = sorted(cls.events, key=lambda event: event.date)

    @classmethod
    def add_event(cls, event):
        """
        Add event to events list and sorts events list after that.
        Parameters:
            event: Event obj
        """
        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        """
        Returns class attribute events.
        Returns:
            events: list
        """
        return cls.events

    @classmethod
    def remove_event(cls, event):
        """
        Remove Event obj from events list.
        Parameters:
            event: Event obj
        """
        cls.events.remove(event)

class Checkpoint(Event):
    """
    Creates Checkpoint obj which inherits from Event class.

    Class attributes:
        events: list
    """
    events = []

    def __init__(self, date):
        """
        Creates Checkpoint obj and add it to events list in Checkpoint and Event classes.

        """
        super().__init__(date)
        Event.add_event(self)
        self.add_event(self)

    def __str__(self):
        """
        Returns string representation of Checkpoint obj.
        """
        return "{} Checkpoint".format(self.date)

class PrivateMentoring(Event):
    """
    Creates PrivateMentoring obj which inherits from Event class.

    Class attributes:
        events: list
        mentors: list

    Instance attibutes:
        preffered_mentor: str
        goal: str
    """

    events = []
    mentors = ["Mateusz Ostafil", "Aga Koszany", "Scoobi"]

    def __init__(self, date, preffered_mentor, goal):
        """
        Creates PrivateMentoring obj and add it to events list in Checkpoint and Event classes.
        Parameters:
            date: Date obj
            preffered_mentor: str
            goal: str
        """
        super().__init__(date)
        self.preffered_mentor = preffered_mentor
        self.goal = goal


        Event.add_event(self)
        self.add_event(self)

    def set_goal(self, goal):
        """
        Set instance attribute goal to goal.
        Parameters:
            goal: str
        """
        self.goal = goal

    def get_goal(self):
        """
        Returns instance attribute goal.
        Returns:
            goal: str
        """
        return self.goal

    @classmethod
    def get_mentors(cls):
        """
        Returns class attribute mentors.
        Returns:
            mentors: list
        """
        return cls.mentors

    def get_preffered_mentor(self):
        """
        Returns instance attribute preffered_mentor.
        Returns:
            preffered_mentor: str
        """
        return self.preffered_mentor

    def __str__(self):
        """
        Returns string representation of PrivateMentoring obj.
        """
        return "{} Private Mentoring with {} about {}".format(self.date, self.preffered_mentor, self.goal)
