class DateTimeError(Exception):
    def __init__(self, component_name, incorrect_value, message):
        self.component_name = component_name
        self.incorrect_value = incorrect_value
        self.message = message

    def __str__(self):
        return f"Invalid value: {self.incorrect_value} for {self.component_name}. It should be {self.message}"