# Usiel Figueroa
# Module 9.2 Assignment: API,s
# CSD325-A311 Advanced Python
# December 01, 2024

# References:
# Custer, C. (2024, March 19). Python API Tutorial: Getting Started with APIs. Dataquest. Retrieved December 1, 2024, from https://www.dataquest.io/blog/python-api-tutorial/
# Goodwin, M. (2024, April 9). What is an API (application programming interface)? IBM. Retrieved December 1, 2024, from https://www.ibm.com/topics/api
# Russell, L. (2020, July 8). Just a Simple API: List of APIs with Fun Data for Quick Mock-ups. Stoplight. Retrieved December 1, 2024, from https://blog.stoplight.io/just-a-simple-api

# Testing my own API
# APIs in the Stars Above

import requests

# Send a GET request to the API
response = requests.get("https://swapi.dev/api/people/1/")

# Print the response status code
print(response.status_code)

# Print the raw JSON response
print(response.json())

import json

# Create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Use the custom function to print the formatted JSON
jprint(response.json())


