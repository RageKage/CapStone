from datetime import datetime, date, time


today = datetime.today()


split_date = today.strftime("%d/%m/%Y").split("/")

print(f"Today the date is the {split_date[0]}th of {split_date[1]} and the year is {split_date[2]}")