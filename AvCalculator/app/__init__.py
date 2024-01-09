from core.managements import CommandManagements


class AvCalculatorApp:
    def __init__(self, version, latest_version):
        """
        AvCalculatorApp is the main class of the application allowing the user to power
        easily navigate the application.

        :param version:         Current version of the application
        :param latest_version:  Latest version of the application

        :return:                Nothing
        """

        self.version        = version
        self.latest_version = latest_version

        self.display_information()
        CommandManagements()

    def display_information(self):
        print(f"AvCalculator - v{self.version}")
        if self.latest_version:
            print(f"\n{self.latest_version}")
        else:
            print("\nThis application allows you to calculate an average using\nvalues given by the user.")
