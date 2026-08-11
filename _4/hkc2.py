import requests
import sys

# URL зеркала сервиса
base_url = 'https://hide-my-name.me'
success_url = 'https://hide-my-name.me/demo/success/'

print("|| CRACKED BY LOVEDILKA ❤️‍🔥 ||\n")

# Используем сессию для автоматической поддержки cookies
session = requests.Session()

try:
    # 1. Запрашиваем главную страницу демо-периода
    response = session.get(base_url, timeout=10)

    if response.status_code != 200:
        print(f"⚠️ Ошибка доступа к сайту. Код ответа: {response.status_code}")
        print("Возможно, ваш IP заблокирован или требуется запустить VPN.")
        sys.exit()

    # Запрашиваем email у пользователя
    email = input('Ваш Email: ').strip()
    if not email:
        print("❌ Email не может быть пустым.")
        sys.exit()

    # 2. Отправляем POST-запрос для получения кода
    payload = {"demo_mail": email}
    post_response = session.post(success_url, data=payload, timeout=10)

    # Анализируем ответ сервера
    if post_response.status_code == 200:
        if 'Ваш код выслан' in post_response.text or 'код уже в пути' in post_response.text.lower():
            print('\n✅ \033[1;32mВаш код уже в пути!\033[0m Проверьте свой почтовый ящик.')
        else:
            print('\n❌ \033[1;31mУказанная почта не подходит, либо лимит тестовых периодов исчерпан.\033[0m')
            # Выводим часть ответа сервера для диагностики, если что-то пошло не так
            if "alert" in post_response.text:
                print("Сообщение от сайта: Ошибка верификации формы.")
    else:
        print(f"\n⚠️ Сервер ответил ошибкой {post_response.status_code} при отправке формы.")

except requests.RequestException as e:
    print(f"\033[1;31mОшибка сети или таймаута:\033[0m {e}")

sys.exit()
