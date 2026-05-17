import datetime

class DateHandler:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
        self.today = datetime.date.today()

    def get_next_tuesday(self):
        """
        Checks today and up to 6 days in the future and returns dateobject of the first Tuesday.
        :return: dateobject
        """
        day = self.today
        if self.days[day.weekday()] == "Tuesday":
            print("Today is Tuesday!")
            return None
        for _ in range(6):
            day += datetime.timedelta(days=1)
            if self.days[day.weekday()] == "Tuesday":
                return day
        return None


# next_tuesday = DateHandler().get_next_tuesday()
# print(f"Next Tuesday: {next_tuesday}")