import requests
import json

API_URL = "http://127.0.0.1:8000/api/search"


def get_user_input():
    departure = input("Введите город отправления: ")
    arrival = input("Введите город прибытия: ")
    date = input("Введите дату (YYYY-MM-DD): ")

    exclusions = input(
        "Введите исключённые виды транспорта (через запятую, например, train,bus), если нет - оставьте пустым: ").split(
        ",")
    exclusions = [ex.strip() for ex in exclusions if ex.strip()]

    priorities = input("Введите приоритеты транспорта (через запятую, например, plane,bus,train): ").split(",")
    priorities = [p.strip() for p in priorities if p.strip()]

    return {
        "departure": departure,
        "arrival": arrival,
        "date": date,
        "exclusions": exclusions,
        "priorities": priorities
    }


def fetch_routes(request_data):
    response = requests.post(API_URL, json=request_data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
        return None


def main():
    request_data = get_user_input()
    result = fetch_routes(request_data)

    if result:
        print("\n=== Прямые маршруты ===")
        for route in result.get("direct_routes", []):
            print(json.dumps(route, indent=4, ensure_ascii=False))

        print("\n=== Маршруты с отдыхом ===")
        for route in result.get("rest_routes", []):
            print(json.dumps(route, indent=4, ensure_ascii=False))

        print("\n=== Посмотреть окрестности ===")
        for route in result.get("sightseeing_routes", []):
            print(json.dumps(route, indent=4, ensure_ascii=False))
    else:
        print("Маршруты не найдены.")


if __name__ == "__main__":
    main()
