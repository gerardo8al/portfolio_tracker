import csv
import urllib.request
import json

def main():

    #Read csv file
    with open('portfolio.csv', 'rt') as portfolio:
        reader=csv.reader(portfolio)
        
        #Make API call
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(json.loads(data.decode('utf-8')))

if __name__ == "__main__":
    main()
