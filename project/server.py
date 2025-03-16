from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime
from brew import get_data_strait, get_data_transfer, sort_routes

HOST = "localhost"
PORT = 8080

class RequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """ Разрешение CORS-запросов """
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path == "/search":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode("utf-8"))

            departure = request_data["departure"]
            arrival = request_data["arrival"]
            date = request_data["date"]
            exclusions = request_data.get("exclusions", [])
            priorities = request_data.get("priorities", [])

            # Проверка на прошедшую дату
            if datetime.strptime(date, "%Y-%m-%d") < datetime.today():
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "На эту дату маршрутов нет."}).encode("utf-8"))
                return

            print(f"Получаем данные для {departure} → {arrival} на {date}...")

            # Получаем маршруты, передавая exclusions и priorities
            direct_routes = get_data_strait(departure, arrival, date, exclusions, priorities)
            transfer_routes = get_data_transfer(departure, arrival, date, exclusions, priorities)

            # Проверяем, что данные не `None`
            if direct_routes is None:
                direct_routes = {"segments": []}
            if transfer_routes is None:
                transfer_routes = {"segments": []}

            # Объединяем и сортируем маршруты
            all_routes = direct_routes.get("segments", []) + transfer_routes.get("segments", [])
            sorted_routes = sort_routes(all_routes, sort_by="time", transport_priority=priorities, exclude_transport=exclusions)

            # Проверяем, есть ли маршруты
            if not sorted_routes:
                self.send_response(404)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Маршрутов не найдено."}).encode("utf-8"))
                return

            # Формируем JSON-ответ
            response_data = {
                "departure": departure,
                "arrival": arrival,
                "totalTime": sorted_routes[0]["duration"] if sorted_routes else "Неизвестно",
                "totalPrice": sorted_routes[0]["price"] if sorted_routes and sorted_routes[0]["price"] else "Неизвестно",
                "direct": [r for r in sorted_routes if r["transport_type"] == "plane"],
                "with_rest": [r for r in sorted_routes if r["transport_type"] == "train"],
                "explore": [r for r in sorted_routes if r["transport_type"] == "bus"]
            }

            # Отправляем данные обратно
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode("utf-8"))

def run():
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Сервер запущен на {HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
