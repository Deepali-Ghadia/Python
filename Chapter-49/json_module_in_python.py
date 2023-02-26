# When I named the file as json.py it gave import error. As soon as I changed the name of file, the issue got resolved
# JSON stands for JavaScript Object Notation and is used to store and transfer the data.
# Double quotes are used in json and json file does not have comments
import json

data = '{"name":"Deepali", "email":"deepali@gmail.com"}'
# parsing the string using loads function

#  method can be used to parse a valid JSON string and convert it into a Python Dictionary. It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.
parsed_string = json.loads(data) 
print(parsed_string)
print(parsed_string["name"]) # accessing value using a key
print(parsed_string["email"]) # accessing value using a key


# storing data in a file
data = {
 'name' : 'Deepali',
 'email_id' : 'deepalinghadia1606@gmail.com',
 'mobile_number' : 1111111111,
 'city' : 'Wardha',
 'state' : 'Maharashtra',
}

# json.dump() is used to put data in a JSON file
with open('Chapter-49/person_data', 'w') as f:
 json.dump(data, f)


# retrieving data from a file
# json.load() function =>  takes a file object and returns the json object. It is used to read JSON encoded data from a file and convert it into a Python dictionary and deserialize a file itself i.e. it accepts a file object.
with open('Chapter-49/person_data', 'r') as f:
    retrieved_data = json.load(f)
print(retrieved_data)


# Formatting JSON output 
# by specifying indent size
print(json.dumps(retrieved_data, indent = 2))

# sorting keys alphabetically
print(json.dumps(retrieved_data, indent = 2, sort_keys=True))

# get rid of whitespaces to get compact output
print(json.dumps(retrieved_data, separators=(",", ":")))




# summary of the functions used
# json.load() => parsing the string
# json.loads() => retrieve data from a file
# json.dump() => convert a Python object into a JSON string | used for writing to JSON file.
# json.dumps() => json.dumps() method is used to encodes any Python object into JSON formatted String.