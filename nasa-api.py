#!/usr/bin/python3

import requests
import pprint

URL = "http://api.open-notify.org/astros.json"

def main():
    response = requests.get(URL)
    print(type(response))
    print(dir(response))
    astros = response.json()
    print(type(astros))
    print(astros.keys())
    astrosnum = astros["number"]
    print("People in Space:", astrosnum)
    
    for astro in astros["people"]:
        astroname = astro["name"]
        astrocraft = astro["craft"]
        print(f"{astroname} is on the {astrocraft}")
main()
