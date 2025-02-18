import get_url as gu
from get_source import return_soup
from get_url import get_stop_number


def get_stop_name(url):
    soup = return_soup(url)
    name = soup.h2.string
    return name.split(' ', 1)[1]

def get_bus_line():
    bus_line = input("Enter your bus line: ")
    return bus_line

