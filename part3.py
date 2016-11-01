import requests

#requests the dictionary of strings
r = requests.post('http://challenge.code2040.org/api/prefix', json= {"token": "c57ff765fcc4bb5c24e8f3a793979a51"})
#assigns the variables there given values from the api
prefix = r.json()['prefix']
array = r.json()['array']
#copy of the array that will contain the new array after searching for words with the same prefix
arrayCopy = r.json()['array']
#loops through each of the elements in the distionary 
for el in array:
  #checks if each element inside the array starts with the prefix given
  if el.startswith(prefix):
    #removes the element from the arrayCopy 
    arrayCopy.remove(el)
#sends the arrayCopy containing the array without the strings with the prefix
requests.post('http://challenge.code2040.org/api/prefix/validate', json= {"token": "c57ff765fcc4bb5c24e8f3a793979a51", "array": arrayCopy})
