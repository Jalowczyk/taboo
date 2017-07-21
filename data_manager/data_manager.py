import csv
from model.events import *
import datetime

class DataManager:

    def import_checkpoints_from_file(self, filename):
        """
        Import checkpoints data from file and creates Checkpoint obj.
        """

        with open(filename, "r") as events_file:
            events = csv.reader(events_file, delimiter = ",")

            for event in events:
                date = self.convert_date(event[0])
                Checkpoint(date)

        events_file.close()

    def import_pm_from_file(self, filename):
        """
        Import private mentoring data from file and creates PrivateMentoring obj.
        """

        with open(filename, "r") as events_file:
            events = csv.reader(events_file, delimiter = ",")

            for event in events:
                date = self.convert_date(event[0])
                mentor = event[1]
                goal = event[2]

                PrivateMentoring(date, mentor, goal)

        events_file.close()

    def export_pm_to_file(self, filename):
        """
        Export private mentorings informations to file.
        """

        with open(filename, "w") as events_file:
            events = csv.writer(events_file, delimiter = ",")

            for private_mentoring in PrivateMentoring.get_events():
                data = [private_mentoring.get_date(), private_mentoring.get_preffered_mentor(), private_mentoring.get_goal()]
                events.writerow(data)

        events_file.close()

    def export_checkpoints_to_file(self, filename):
        """
        Export private mentorings informations to file.
        """

        with open(filename, "w") as events_file:
            events = csv.writer(events_file, delimiter = ",")

            for checkpoint in Checkpoint.get_events():
                events.writerow([checkpoint.get_date()])

        events_file.close()

    @staticmethod
    def convert_date(date):
        """
        Converts string date to Date obj date.
        """
        date_list = date.split("-")
        return datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
