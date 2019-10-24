#!/usr/bin/env python
import requests
import logging
import os
import json
import sys

powerAIEndpoint = "https://bananaai.mybluemix.net/detectpowerai"
watsonEndpoint = "https://bananaai.mybluemix.net/detectvr"
testimage = "banane.jpg"
errResponse = "Sorry! Something went wrong on my end. My developers must be bad at their job."

### classify_image is the MAIN RUNNING CLASS that sends a POST request and interprets it
### PARAM filedir: String, file to send, relative or absolute path depending on the situation
### PARAM powerAI: Boolean, set to True if using PowerAI Vision, set to False if using Watson Visual Recognition
### PARAM self: Boolean, set to None if using client independent of Pepper, set to self if using on Pepper
### RETURNS String for Pepper to say out loud
def classify_image(filedir, powerAI, self):
    response = ""
    if powerAI:
        response = send_post_request(filedir, powerAIEndpoint)
    else:
        response = send_post_request(filedir, watsonEndpoint)
    if isinstance(response, requests.exceptions.RequestException):
        print("DEBUG: " + str(response))
        if self is not None:
            self.logger.info("DEBUG: " + str(response))
        return errResponse
    if self is not None:
        self.logger.info("DEBUG: the response code is " + str(response.status_code))      # debug purposes
        self.logger.info("DEBUG: the response text is " + str(response.text))                  # debug purposes
    return response


### send_post_request sends POST request to shim with image to classify
### PARAM filedir: String, file to send, relative or absolute path depending on the situation
### PARAM endpoint: String, endpoint to send request to
### RETURNS error OR response string
def send_post_request(filedir, endpoint):
    files = {
        'files': ('img.jpg', open(filedir, 'rb')),
    }
    r = ""
    try:
        r = requests.post(endpoint, headers={'Cache-Control': 'no-cache'}, files=files, timeout=5, verify=False)
        #r = requests.post(endpoint, headers={'Cache-Control': 'no-cache'}, files=files, timeout=5, verify=True, cert=('./certs/publickey.cer', './certs/privatekey.pem'))
    except requests.exceptions.RequestException, e:
        return e
    return interpret_response(r)

### interpret_response takes response object, determines if there is valid JSON to parse or not
### PARAM response: the python response object to interpret, should retrieve from send_post_request
### RETURNS successful classification, "negative", or other string if there was an error
def interpret_response(response):
    print("DEBUG: the response code is " + str(response.status_code))      # debug purposes
    print("DEBUG: the response text is " + response.text)                  # debug purposes
    if response.status_code is 200:
        classification, confidence = response.json()["classified"].items()[0]
        if classification == "negative":
            return "Sorry, I am not sure what that is."
        print("DEBUG: " + classification)
        return "I believe this is a " + classification
    return errResponse

def main():
    print(classify_image(testimage, True, None))

if __name__ == "__main__":
    main()
