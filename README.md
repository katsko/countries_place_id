# Countries place ID

Read input json file, get place_id for each country by Google API and write result json to output file.

## Requires


```
Python3
google-api-python-client
```

### Install requires:

Install Python:

```
sudo apt install python3
```

Install lib:

```
pip install google-api-python-client
```

or

```
pip install -r requires.txt
```

## Usage

Set API KEY parameter in script: 

```
4:  GOOGLE_GEO_API_KEY = 'your_api_key'
```

if you want to change input and output filenames:

```
6:  INPUT_FILE_NAME = 'input.json'
7:  OUTPUT_FILE_NAME = 'output.json'
```

and fieldnames:

```
8:  FIELD_NAME = 'en'
9:  FIELD_NAME_RU = 'ru'
10: FIELD_PLACE_ID = 'placeID'
```

Also you can change language for API request:

```
11: LANG = 'en'
```
