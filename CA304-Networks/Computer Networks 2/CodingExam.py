import urllib.request
import json
import itertools
import requests


f = urllib.request.urlopen("https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=02c9f68307b5df6e4d0a0e5a419b").read()

jsonResponse = json.loads(f.decode('utf-8'))


#countries = ()
#for country in jsonResponse("country"):
#countries = countries + list("country")
# tried sorting by country

datelist = []
for partner in jsonResponse["partners"]:
datelist = datelist + list(partner["availableDates"])


possible_dates = (list(set(datelist)))
possible_dates = dict.fromkeys(possible_dates, 0)


#print(possible_dates)
for date in datelist:
if date in possible_dates:
possible_dates[date] += 1

new_dict = dict(sorted(possible_dates.items(), key=lambda item: item[1])) #sorted by number of partners available
key_dict = dict(sorted(possible_dates.items(), key=lambda item: item[0])) #sorted by months

print(key_dict), print("Sorted by dates")
print(new_dict), print("Sorted by numbers available on each Date")


r = requests.post("https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=02c9f68307b5df6e4d0a0e5a419b", json={"key": "value"})
r.status_code
#POST json body hubteam site


#couldn't sort by country 