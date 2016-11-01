import requests

# requests the string that will be reversed
r = requests.post('http://challenge.code2040.org/api/reverse', json= {"token": "c57ff765fcc4bb5c24e8f3a793979a51"})
# converts the string in reverse order
temp = r.content[::-1]
# sends the reverse string back
r = requests.post('http://challenge.code2040.org/api/reverse/validate', json= {"token": "c57ff765fcc4bb5c24e8f3a793979a51", "string": temp})
