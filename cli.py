from api import ScamSearchAPI
import json
import os

# function to perform exact search on ScamSearchAPI
def exact_search_scams(search_term, search_type):
    res = ScamSearchAPI().search_exact_match(search_term, search_type)
    res = json.dumps(res)
    res = json.loads(res)

    if res['status'] == 'False':
        return False

    return res

# function to print the results of exact search
def print_exact_search_scams(res):
    length = len(res['result'])
    for item in res['result']:
        print("Bitcoin Address:", item['bitcoin_address'])
        print("Scammer Type:", item['scammertype'])
        print("Scammer Type Other:", item['scammertype_other'])
        print("Scammer Username:", item['scammerusername'])
        print("Scammer Email:", item['scammeremail'])
        print("Scammer Phone:", item['scammerphone'])
        print("Scam Description:", item['scamdescription'])
        print("Created At:", item['created_at'])
        print("----------------------------------------------------------------------")

    print(f'{length} results')
    


if __name__ == '__main__':
    # get the search term and search type from user input
    search_term = input("Enter the search term: ")
    search_type = input("Enter the search type: ")

    # perform exact search and print the results
    res = exact_search_scams(search_term, search_type)
    if False == res: print("No Results, please refine your search parameter")
    print_exact_search_scams(res)
