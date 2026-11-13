from datetime import date

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = date(year, month, day)

formatted_date = event_date.strftime("%B %d, %Y")
weekday = event_date.strftime("%A")

print("\nFormatted Output:")
print("Event:", event_title.upper())
print("Date:", formatted_date)
print("Year:", year)
print("Month:", event_date.strftime("%B"))
print("Day:", day)
print("Weekday:", weekday)
