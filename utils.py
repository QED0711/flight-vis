import requests
from bs4 import BeautifulSoup


def parse_table(soup):
    table = soup.find_all("table", class_="prettyTable")[0]
    rows = table.find_all("tr", class_="smallrow1")
    data = []

    for row in rows:
        info = {}
        spans = row.find_all("span")
        try:
            info['time'] = spans[0].text
            info['latitude'] = float(spans[2].text)
            info['longitude'] = float(spans[4].text)
            info['feet'] = int(spans[8].text)
        except:
            continue

        data.append(info)

    return data

def get_data_from(url):
    if not url.split("/")[-1] == 'tracklog':
        url += "/tracklog"
        
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, features='lxml')
    
    return parse_table(soup)


if __name__ == "__main__":
    print(get_data_from("https://flightaware.com/live/flight/DAL1529/history/20191005/1110Z/KJFK/KLAX/tracklog"))
