from helium import *
import os
from dotenv import load_dotenv
import json
import functions as func

JSON_FILENAME = "credentials.json"

#load the JSON file
with open(JSON_FILENAME, 'r') as credentials:
    data = json.load(credentials)
    for x in data:
        for cred in x.values():
            pass
        # "cred_format":["username", "password", "dpNumber", "crn", "txn_code", "name"],
        # func.login(cred[0], cred[1], cred[2])
        # func.applyForIPO()
        # func.showCurrentIssue()
        # func.logout()

    credentials.close()

addNewData = input("Do you want to add new meroshare account information? (y/n)")
if(addNewData == "y"):
    func.updateJSON(JSON_FILENAME)



