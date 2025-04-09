import requests

def send_row(data):
    url = "https://script.google.com/macros/s/AKfycbwQiuDcdFWMix9Qs4ol4twfUoGviI7gF3YwHHozv0wqSbZT71VrsSz9T-Af6ijwM6yXTw/exec"
    response = requests.post(url, json=data)
    print("Ответ:", response.status_code, response.text)

if __name__ == "__main__":
    test_data = {
        "ID": "gpt0001",
        "User ID": "user_001",
        "Тип": "Цель",
        "Название": "Выйти на фриланс",
        "Описание": "Работать с зарубежными заказами через платформы",
        "Родитель": "",
        "Цель": "",
        "Сфера": "Карьера",
        "тип корня": "",
        "Статус": "Активно"
    }
    send_row(test_data)
