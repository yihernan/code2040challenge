import requests
#requests the dictionary of strings
r = requests.post('http://challenge.code2040.org/api/haystack', json= {"token": "c57ff765fcc4bb5c24e8f3a793979a51"})
#assigns values to variables 
haystack= r.json()['haystack']
needle= r.json()['needle']
#loops through the length of the array of strings
for i in xrange(len(haystack)):
  #checks if the index of haystack matches the string needle
  if haystack[i] == needle:
    break
#sends the postion of the needle string 
r = requests.post('http://challenge.code2040.org/api/haystack/validate', json= {"token": "c57ff765fcc4bb5c24e8f3a793979a51", "needle": i})
