from core.managements.manager import commands
from core.managements.commands.average import AverageCommand


class CommandManagements:
    def __init__(self):
        self.prompt = None

        self.call_command()

    def call_command(self):
        try:
            while True:
                self.prompt = input("\n[>] ")
                self.get_commands()
        except KeyboardInterrupt:
            return exit(1)

    def get_commands(self):
        """
        Execute the selected command if it exists.

        :return: None
        """

        if self.prompt in commands:
            commands[self.prompt]()
        else:
            print("[!] Invalid command. Type 'help' for a list of commands.")

