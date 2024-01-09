def help_command():
    """
    Displays the list of commands.

    :return:    Help message
    """

    return """COMMANDS :
- help      : Displays the list of commands.
- about     : Informs the user of the usefulness of the application.
- license   : Displays the license of the application.
- exit      : Exits the application.
- average   : Used to calculate an average."""


def about_command():
    """
    Informs the user about the application.

    :return:    About message
    """

    return """AvCalculator
This application makes it easy to calculate an average.
For more information, see the documentation on GitHub."""


def license_command():
    """
    Displays the license information.

    :return:    License message
    """

    return "MIT License"


def exit_command():
    """
    Exits the application.

    :return:    None
    """

    exit(0)
