def get_stop_number():
    stop_number = input("Enter your stop number: ")
    return stop_number

def get_stop_url(stop_number):
    stop_url = f"https://www.emtmadrid.es/PMVVisor/pmv.aspx?stopnum={stop_number}"
    return stop_url



