# App identifier

This work came out of the work to reduce the data processing time for TBM data. This is a simple stand-alone script that leverages the [GEAR API](https://gsa.github.io/GEAR-Documentation/api-docs/console/) to identify what apps are mentioned in tickets. 

## Setup

Install Python 3.6.5 see [Python documentation](https://www.python.org/downloads/)

install pipenv
```
pip install --user pipenv
```

## Use

Save the file that you want to identify the app. 

To run the script, first activate the environment. (You only have to do this once per session.)
```
pipenv shell 
```

Then you can run the script with the script name and the path to the csv file.
```
python find_names.py path/to_the/file.csv
```
This will create a new file in the same folder as the file is being processed. In the example above, the result would be a file called `path/to_the/file_processed.csv`.

For better results, add key phrases to `phrase_enhancements.csv`.

There is also a quality checking script but that requires a sample with manually coded data.
