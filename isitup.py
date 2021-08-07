import os
import requests

reply = ["y"]

while "running":
    while reply[0] == "y":
        os.system('clear')

        print("Welcome to IsItUp.py!!!")
        print("Please write a URL or URLs you want to check. (separated by comma)")
        user_item = input().lower().split(",")
        user_items = [i.strip() for i in user_item]
        add_http = []
        URLs = []

        for item in user_items:
            if "." in item:
                add_http.append(item)
            else:
                print(f"{item} is not valid URL")

        for word in add_http:
            if "http://" in word:
                URLs.append(word)
            else:
                URLs.append("http://" + word)

        for url in URLs:
            try:
                r_url = requests.get(url)
                code = (r_url.status_code)
            except:
                code = 404
            finally:
                if code == 200:
                    print(f"'{url}' is Up!")
                elif code == 404:
                    print(f"'{url}' is Down!")
                else:
                    print(f"'{url}' is status'{code}'")

        break

    reply = str(input("Do you want start over? (y/n): ")).lower().strip()

    if reply[0] == "n":
        print("Bye~")
        break
    else:
        print("Please answer 'y'or'n'")
        continue
