""" run with the following command, replace the values in angle brackets:
python find_names.py <path_to_file>  
"""
import sys
import json

import requests
import pandas as pd

input_file = sys.argv[1]

apps = {}
# call the GEAR API to get a list of apps
gear_data = requests.get('https://ea.gsa.gov/api/v0/applications', verify=False).json()

# create a list were the long version and short version of the names are in a dictionary with the long gear name as the value
for app in gear_data:
    # only include current apps
    if app['Status'] == 'Production':
       # if the name is something like "LDS - Labor Distribution System", it will look for "LDS" and "Labor Distribution System" separately
       for name in  app['Name'].split(' - '):
            apps[name] = app['Name'] 
       # add any name aliases
       if app['Alias']:
           for alias in app['Alias'].split(','):
                apps[alias] = app['Name'] 

# add some extra matches from the phrase_enhancements.csv file
extra_apps = {}
phrase_df = pd.read_csv('phrase_enhancements.csv', header = 0)
for row in phrase_df:
  extra_apps[row[0]] = row[1]

# combine the GEAR dictionary with the phrase dictionary
apps.update(extra_apps)

# reads the file that needs to be categorized
df = pd.read_csv(input_file, header = 0)

# looks at each row in key fields where the app name or key phrase might appear
def look_4_name(row):
    text = str(row['short_description']) + str(row['u_category']) + str(row['u_subcategory']) + str(row['u_item'])
    # looks to match the longest words first
    for key in sorted(apps, key=len, reverse=True):
        if key in str(text):
            return apps[key] 
    # no matches in GEAR
    return 'Allocate according to Apptio "Incident Category Crosswalk"'

df['name_prediction'] = df.apply(lambda row: look_4_name(row), axis=1)

# write results to a file
new_file_name = input_file[:-4] + "_processed.csv"
df.to_csv(new_file_name)
