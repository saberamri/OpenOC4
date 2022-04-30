from datetime import date, timedelta

v = date(2020-04-23)
age = (date.today() - v) // timedelta(days=365.2425)
print(age)