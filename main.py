from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os.path
import requests
from oauth2client.service_account import ServiceAccountCredentials

import sys
sys.path.insert(0, 'libs')
import gspread
from flask import Flask, request, redirect


app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):


    # The ID and range of the spreadsheet.
    MASTER_SPREADSHEET_ID = '1ltCHpWBXQfCT1WvzczhJc6LQ760DirG14knqvboYf7M'    

    # define credentials needed to read the trix
    scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    creds = ServiceAccountCredentials.from_json_keyfile_name('secret-key.json', scope)   
    client = gspread.authorize(creds)

    # Open List Sheet 
    sheet = client.open_by_key(MASTER_SPREADSHEET_ID).get_worksheet(0)

    try:
        cell = sheet.find(path)
        the_url = sheet.cell(cell.row, cell.col+1).value
        return redirect(the_url)
    except:  #not found
        return 'Error 404: Could not find ' + path, 404
