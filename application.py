from controller.controller import Controller
from data_manager.data_manager import DataManager

class Application:
    """
    Creates Application class
    Instance attributes:
        controller: Controller obj
        data_manager: DataManager obj
        checkpoints_data_path: str
        private_mentorings_data_path: str
        is_running: bool
    """

    def __init__(self):
        """
        Creates Application instance.
        """
        self.controller = Controller()
        self.data_manager = DataManager()
        self.checkpoints_data_path = "resources/checkpoints.csv"
        self.private_mentorings_data_path = "resources/private_mentorings.csv"
        self.is_running = True

    def run(self):
        """
        Handle main menu and import from and export to file.
        """

        self.import_from_file()

        while self.is_running:
            if self.controller.start_menu_action() == "exit":
                self.is_running = False

        self.export_to_file()


    def import_from_file(self):
        """
        Imports from file.
        """
        self.data_manager.import_checkpoints_from_file(self.checkpoints_data_path)
        self.data_manager.import_pm_from_file(self.private_mentorings_data_path)

    def export_to_file(self):
        """
        Exports to file.
        """
        self.data_manager.export_pm_to_file(self.private_mentorings_data_path)
        self.data_manager.export_checkpoints_to_file(self.checkpoints_data_path)
