import statistics

class AverageCommand:
    def __init__(self):
        """
        Average command to calculate an average.

        :return:    Nothing
        """

        self.list_of_numbers = []

    def run(self):
        """
        Run the average calculation.

        :return:    Nothing
        """

        self.get_numbers()
        self.averaging()

    def get_numbers(self):
        """
        Get user input for numbers.

        :return:    Nothing
        """

        print("[?] Please enter all values here spaced by a space.")
        print("[?] Note that the commas will be replaced by a period (\".\")")

        input_numbers = input("\n[>] ")
        if self.checker(input_numbers):
            return

        # If the input is not valid, prompt the user again
        self.get_numbers()

    def checker(self, input_numbers):
        """
        Check and parse user input for valid values.

        :param input_numbers: User input for numbers

        :return:              True if input is valid, False otherwise
        """

        numbers = input_numbers.split()

        try:
            for number in numbers:
                parsed_number = float(number.replace(',', '.'))  # Replace commas with periods
                self.list_of_numbers.append(parsed_number)
            return True
        except ValueError:
            print("[!] Please enter valid numeric values.")
            return False

    def averaging(self):
        """
        Perform averaging and display the result.

        :return:    Nothing
        """

        result = statistics.mean(self.list_of_numbers)
        print(f"[=] {result}")