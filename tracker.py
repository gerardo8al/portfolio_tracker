from constants import *
import csv
import urllib.request
import json

def send_get_request(url):
    response = urllib.request.urlopen(url)
    json_back = response.read()
    json_back = json.loads(json_back.decode('utf-8'))
    #json_pretty_print(json_back)
    return json_back

def json_pretty_print(parsed):
    print(json.dumps(parsed, indent=4, sort_keys=True))

def main():

    #The request returns a json that contains the info for
    #all the tickers in exchange.
    json_back = send_get_request(URL)

    with open(CSV, 'rt') as f:
        reader=csv.reader(f)

        for row in reader:
            ticker = row[0]
            quantity = row[1]

if __name__ == "__main__":
    main()
