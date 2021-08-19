import os
import requests

def main():
    print("welcome!")
    
print("Enter your login")
login = input("Login: ")
print("Enter password")
password = input("Password: ")

urll = "https://yourfirebaseyrl.firebaseio.com/"
da = urll + "Users/" + login + "/.json"
g = requests.get(da)
if g.text == "null":
    ip = requests.get('https://api.ipify.org').text
    r = requests.put(da, data = "{" + '"Password"' + ":" + '"'+password+'"' + "," + '"ip"' + ":" + '"'+ip+'"' "}")
    main()
else:
    ps = urll + "Users/" + login + "/Password" + "/.json"
    pasw = requests.get(ps).text
    if '"'+password+'"' != pasw:
        print("Wrong password!")
    else:
        main()
