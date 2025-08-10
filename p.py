months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

calendar = {}

for month in months:
    weeks = {}
    for week_num in range(1, 5):   
        weeks[f"Week {week_num}"] = []
    calendar[month] = weeks

calendar["July"]["Week 2"].append("Summer BBQ party")

print(calendar["July"]["Week 2"])
