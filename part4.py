import requests
import dateutil.parser
from datetime import timedelta, tzinfo, datetime

#requests the dictionary from API
r = requests.post('http://challenge.code2040.org/api/dating', json= {"token": "c57ff765fcc4bb5c24e8f3a793979a51"})
#assigns the values to each variable
datestamp = r.json()['datestamp']
interval = r.json()['interval']
#parses the string into a datetime python object
date = dateutil.parser.parse(datestamp)
#expresses the duration of seconds
newinterval = timedelta(seconds=interval)
#assigns a variable to the sum of date and newinterval
added = (date + newinterval)
#transforms the value added into the ISO 8601 format
newData = datetime.isoformat(added)
#replaces the miliseconds with the letter Z
newData = newData.replace('+00:00', 'Z')
#sends the resulting date back to the API
requests.post('http://challenge.code2040.org/api/dating/validate', json= {"token": "c57ff765fcc4bb5c24e8f3a793979a51", "datestamp": newData})
