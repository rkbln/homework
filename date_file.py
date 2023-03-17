from datetimeerror.error import DateTimeError

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.__eTime(year, month, day)

    def __eTime(self, year, month, day):
        date_list = [year, month, day]
        name_list = ["year", "month", "day"]
        message_list = ["between 0 and 9999", "between 1 and 12", "between 1 and 31"]
        check_num = [9999, 12, 31]
        for i in range(0, len(date_list)):
            if type(date_list[i]) != int:
                raise DateTimeError(name_list[i], date_list[i], "an integer")
            elif date_list[i] < 1 or date_list[i] > check_num[i]:
                raise DateTimeError(name_list[i], date_list[i], message_list[i])

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)