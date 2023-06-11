from api import ScamSearchAPI

apikey = ""
search_term = "1PQdgvRNF4jhX1PfkkcBd8tr9NMpsCvwz8"
search_type
res = ScamSearchAPI(apikey).search_exact_match(search_term, search_type)
length = len(res['result'])
res = json.dumps(res)
res = json.loads(res)


if res['status'] == 'False':
    print("No results, please refine your search paramater")


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
