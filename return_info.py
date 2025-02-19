import requests
from bs4 import BeautifulSoup

def get_stop_number():
    try:
        stop_number = int(input("Enter your stop number: "))
    except ValueError:
        print("The stop number must be a number.")

    return stop_number

def get_stop_url():
    stop_number = get_stop_number()
    stop_url = f"https://www.emtmadrid.es/PMVVisor/pmv.aspx?stopnum={stop_number}"
    return stop_url

# retrieves the EMT data
def return_soup(url):
    try:
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except ExceptionGroup:
        print("Something went wrong.")
        quit()

def get_bus_line():
    while True:
        try:
            bus_line = int(input("Enter your bus line: "))
        except ValueError:
            print("The bus line must be an integer.")
        else:
            return bus_line


def return_info():
    stop_number = get_stop_number()
    soup = return_soup(get_stop_url())
    stop_name = soup.h2.string.split(' ', 1)[1] # formats the stop name
    bus_line = get_bus_line()

    return stop_number, bus_line, stop_name, soup
