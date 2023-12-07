import json
keep_list = ["id", "category", "merchants", "valid_to"]

def add_date (year, month, day):
    day_in_month = 
    day = day + 5

with open('input.json') as f:
    data = json.load(f)
    baka = data
    for a in baka['offers']:
        for key in a.copy():
            if key not in keep_list:
                a.pop (key, None)
        #a.pop ('title', None)
        #a.pop ('description', None)
    
