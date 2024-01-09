from core.managements.commands.average import AverageCommand
from core.managements.commands.default import help_command, about_command, license_command, exit_command

commands = {
    "help": lambda: print(help_command()),
    "about": lambda: print(about_command()),
    "license": lambda: print(license_command()),
    "exit": lambda: exit_command(),
    "average": lambda: AverageCommand().averaging()  # Call the averaging method directly
}
