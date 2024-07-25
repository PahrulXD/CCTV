import requests, re , os
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
url = "http://www.insecam.org/en/jsoncountries/"

resp = requests.get(url, headers=headers)
data = resp.json()
countries = data['countries']
for key, value in countries.items():
	print(f'\033[1;97mcode : ({key}) - {value["country"]}')
    


def masuk():
	try:
		country = input("\n\033[1;97m- masukkan code : ")
		print ("")
		res = requests.get(f"http://www.insecam.org/en/bycountry/{country}", headers=headers)
		last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
		for page in range(int(last_page)):
			res = requests.get(f"http://www.insecam.org/en/bycountry/{country}/?page={page}",headers=headers)
			find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
		for ip in find_ip:
			print (ip)
	except:
		pass
	finally:
		print ("")
			
    
masuk()