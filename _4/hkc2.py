import requests
import sys

base_url = 'https://hide-my-name.me'
success_url = 'https://hide-my-name.me/demo/success/'

print("|| CRACKED BY LOVEDILKA ❤️‍🔥 ||\n")

session = requests.Session()

try:
    response = session.get(base_url, timeout=10)

    if response.status_code != 200:
        print(f"⚠️ Unable to connect to site. Error code: {response.status_code}")
        sys.exit()

    email = input('Your Email: ').strip()
    if not email:
        print("❌ Email cant be blank")
        sys.exit()

    payload = {"demo_mail": email}
    post_response = session.post(success_url, data=payload, timeout=10)

    if post_response.status_code == 200:
        if 'Ваш код выслан' in post_response.text or 'код уже в пути' in post_response.text.lower():
            print('\n✅ \033[1;32mYour code has been sent!\033[0m Check your mail box.')
        else:
            print('\n❌ \033[1;31mThe email cant be used to get code.\033[0m')
            
            if "alert" in post_response.text:
                print("Message from site: Unable to verify")
    else:
        print(f"\n⚠️ Server returned {post_response.status_code}.")

except requests.RequestException as e:
    print(f"\033[1;31mNetwork error:\033[0m {e}")

sys.exit()
