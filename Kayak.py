import requests, re, sys

def Get_Flight_Data(From, To, YYMMDD):
	headers = {
		'authority': 'www.kayak.com',
		'pragma': 'no-cache',
		'cache-control': 'no-cache',
		'sec-ch-ua': '^\\^',
		'sec-ch-ua-mobile': '?0',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-user': '?1',
		'sec-fetch-dest': 'document',
		'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
	}
	response = requests.get(f'https://www.kayak.com/flights/{From}-{To}/{YYMMDD}', headers=headers)
	parsed_response = re.findall('<div class="price">\W?\W\d\d\d\W?</div>\W<div class="provider-brand">[a-zA-Z\s]+</div>', response.text)
	results = []
	for item in parsed_response:
		price = float(re.findall('[0-9]+', re.findall('<div class="price">\W\W[0-9]+\W</div>', item)[0])[0])
		airline = re.findall(">[a-zA-Z\s]+</", item)[0].replace(">", "").replace("</", "")
		results.append([price, airline])
	print(response)
	print(str(response.text.encode(sys.stdout.encoding, errors='replace')))
	return results
if __name__ == "__main__":
	print(Get_Flight_Data("JAX", "DAL", "2021-06-11"))