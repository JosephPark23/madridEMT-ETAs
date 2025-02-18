from get_source import return_soup
from get_url import get_stop_url, get_stop_number



def get_trees(soup):
    bus_line = input("Enter your bus line: ")
    td_tags = (soup.find_all("td"))[4:]
    for td in td_tags:
        if td.string == bus_line:
            eta = td.next_sibling.next_sibling.string
    print("ETA: " + eta)

get_trees(return_soup(get_stop_url(get_stop_number())))