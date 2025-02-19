from return_info import return_info as ri
from os import system, name
from time import sleep


# for cleaning up the screen
def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac
    else:
        _ = system('clear')


def find_eta():
    while True:
        # get necessary data
        stop_number, bus_line, stop_name, soup = ri()

        # search html trees for the desired bus line
        td_tags = (soup.find_all("td"))[4:]
        for td in td_tags:
            if td.string == bus_line:
                eta = td.next_sibling.next_sibling.string
                return bus_line, stop_name, eta
                # error message
        print("\033[93m" + f"Sorry, no estimates are available for bus line {bus_line}." + "\033[0m")
        sleep(3)
        clear()

def print_eta():
    bus_line, stop_name, eta = find_eta()
    print("\033[96m" + "\033[1m" + f"\nBus {bus_line} will arrive in {eta}utes at the {stop_name}." + "\033[0m")

print_eta()
