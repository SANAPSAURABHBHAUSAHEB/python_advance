import datetime

s= datetime.datetime.now()
print(s.strftime("%X"))
print(s.year)
d= datetime.date.today()
print(d)
# count function to count age
def count_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
# birth date
birth_date = datetime.date(1997, 1, 1)
# calling count_age function
print(count_age(birth_date))

