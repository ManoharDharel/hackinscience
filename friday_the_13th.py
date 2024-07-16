from datetime import datetime, timedelta


def friday_the_13th():
    today = datetime.today()
    current_date = today

    while True:
        if current_date.weekday() == 4 and current_date.day == 13:
            return current_date.strftime("%Y-%m-%d")

        current_date += timedelta(days=1)


print(friday_the_13th())