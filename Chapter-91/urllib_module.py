# Urllib package is the URL handling module for python. It is used to fetch URLs (Uniform Resource Locators). It uses the urlopen function and is able to fetch URLs using a variety of different protocols.
import urllib.request

# http get
response = urllib.request.urlopen('https://www.geeksforgeeks.org/python-urllib-module/')
print(response) # prints HTTP object

print(response.read())
print(response.code)

# http post