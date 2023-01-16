#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX POST -d "email=test@gamil.com&subject=I will always be here for PLD" "$1"
