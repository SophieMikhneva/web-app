from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8080

class RequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """ Обработка CORS-запросов """
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

            response_data = {
                "departure": request_data["departure"],
                "arrival": request_data["arrival"],
                "totalTime": "1 день 23 часа",
                "totalPrice": "20000",
                "steps": [
                    {"departureTime": "01:59", "departureStation": "Павелецкий вокзал", "departureCity": "Москва", "transport": "Поезд", "arrivalTime": "11:22", "arrivalStation": "Придача", "arrivalCity": "Воронеж", "transferDuration": 13},
                    {"departureTime": "00:53", "departureStation": "Придача", "departureCity": "Воронеж", "transport": "Поезд", "arrivalTime": "12:28", "arrivalStation": "Ростов Главный", "arrivalCity": "Ростов-на-Дону", "transferDuration": 2.5},
                    {"departureTime": "15:00", "departureStation": "Ростов Главный", "departureCity": "Ростов-на-Дону", "transport": "Поезд", "arrivalTime": "01:46", "arrivalStation": "Волгоград-1", "arrivalCity": "Волгоград"}
                ]
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))

def run():
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Сервер запущен на {HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
