import json
from googleplaces import GooglePlaces

GOOGLE_GEO_API_KEY = 'your_api_key'

INPUT_FILE_NAME = 'input.json'
OUTPUT_FILE_NAME = 'output.json'
FIELD_NAME = 'en'
FIELD_NAME_RU = 'ru'
FIELD_PLACE_ID = 'placeID'
LANG = 'en'


'''
Example input file:
[{"ru": "Россия", "en": "Russia"}, {"ru": "Колумбия", "en": "Colombia"}]
'''


def main():
    """
    Read input json file, get place_id for each country by Google API
    and write result json to output file.
    """
    google_places = GooglePlaces(GOOGLE_GEO_API_KEY)
    result = []
    with open(INPUT_FILE_NAME) as json_file:
        data = json.load(json_file)
        for country in data:
            place_id = None
            country_name = country.get(FIELD_NAME)
            print(country_name)
            if country_name:
                country_search = google_places.text_search(
                    query=country_name, language=LANG)
                if country_search and country_search.places:
                    place_id = country_search.places[0].place_id
                    print(place_id)
            result.append({FIELD_NAME_RU: country.get(FIELD_NAME_RU),
                           FIELD_NAME: country_name,
                           FIELD_PLACE_ID: place_id})
    with open(OUTPUT_FILE_NAME, 'w') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
