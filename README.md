# golinks-sheets

With thanks to Alfred Biehler who wrote [this article](https://www.linkedin.com/pulse/sheets-powered-go-links-app-engine-alfred-biehler/) and shared it with me. 

This service is a simple Python URL shortner / redirection service using App Engine and Google Sheets.

## How it works

1. Create a domain / subdomain with your domain provider
2. Create a Google App Engine app and configure [a custom domain mapping](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains)
3. Configure your domain to point to this custom mapping
4. Create a Google Sheet, and grab the sheet ID from the URL. Add this to your Python code
5. Enable the Google Sheets API in your GCP project
6. Create a service account credential, and download the JSON file with the token. 
7. Share your spreadsheet with the service account, with Viewer permissions
8. Deploy the app

## Libraries

I needed to package gspread and Flask with my service for it to deploy successfully. 
