from date_file import Date
from datetimeerror.error import DateTimeError

class DateTime(Date):
    def __init__(self, year, month, day, hours, minutes, seconds):
        super(DateTime, self).__init__(year, month, day)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.__eTime(hours, minutes, seconds)

    def __eTime(self, hours, minutes, seconds):
        # super(DateTime, self).__eTime()
        time_list = [hours, minutes, seconds]
        name_list = ["hours", "minutes", "seconds"]
        message_list = ["between 0 and 23", "between 0 and 59", "between 0 and 59"]
        check_num = [23, 59, 59]
        for i in range(0, len(time_list)):
            if type(time_list[i]) != int:
                raise DateTimeError(name_list[i], time_list[i], "an integer")
            elif time_list[i] < 0 or time_list[i] > check_num[i]:
                raise DateTimeError(name_list[i], time_list[i], message_list[i])

    def __str__(self):
        return super(DateTime, self).__str__() + "\n{}:{}:{}".format(self.hours, self.minutes, self.seconds)

# try:
#     date1 = Date(1996, 11, 15)
#     print(date1)
# except DateTimeError as e:
#     print(e)

try:
    datetime = DateTime(2023, 12, 16, 15, 32, 59)
    print(datetime)
except DateTimeError as e:
    print(e)