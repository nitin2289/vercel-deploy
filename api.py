import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# Hardcoding the student data (as JSON file may not be accessible in serverless environments)
student_marks = {
    "FlU": 4,
    "NdTkFiZ": 6,
    "haOvfcnf": 17,
    "T2GjKIHK": 71,
    "vSSmWR6yRO": 65,
    "KRG2lgv1H": 84,
    "j6BMT9ALK6": 19,
    "9Wa": 28,
    "55": 34,
    "uYtx837Qg": 61,
    "O": 76,
    "5": 45,
    "u": 61,
    "u69qnpG1H": 62,
    "PQOUSqwk": 32,
    "QeRr5NBds": 91,
    "vG9f": 59,
    "wpLwOb": 98,
    "yFTGlxmtBG": 45,
    "7Xtd": 14,
    "6PuvzcpRvL": 27,
    "yxsrF": 9,
    "og": 26,
    "Z5yEjMre": 46,
    "Rrp7R0C": 91,
    "5Iu1zN8": 26,
    "p4FGg9": 18,
    "wM4nnLQZ9": 83,
    "DWqQRIsr": 7,
    "YN8UvGbG": 27,
    "0KrZDjJx": 97,
    "co": 42,
    "U4ik": 76,
    "M5kq": 59,
    "VrWciSr3": 3,
    "wz8CtHjKe": 24,
    "6RvpfJ8": 60,
    "KTH2xwK": 71,
    "jwiDX": 73,
    "85xehXhx": 40,
    "uNSnci0onT": 95,
    "Fyj": 64,
    "uZ55Lfh": 38,
    "ql": 15,
    "x": 44,
    "aGq5i": 62,
    "N1hMUvO": 61,
    "x": 94,
    "4iQrDluE": 66,
    "g9XB": 42,
    "s10tHRF0": 92,
    "zuqJ2BP": 41,
    "KLvr": 13,
    "gjufUJWH": 77,
    "uSotYG2W": 30,
    "dEZoRrjmOH": 33,
    "Cjttwza6J": 61,
    "1tUoqsP": 14,
    "q29": 72,
    "fyRzkO1j8L": 43,
    "iVSW": 46,
    "FHHrCsUrx": 90,
    "9J8z": 92,
    "wZOJucIleg": 40,
    "nuqWfB": 91,
    "rcvl": 71,
    "6wb9INiqhp": 45,
    "t3kArIV": 75,
    "I": 17,
    "8": 4,
    "LoA": 15,
    "5WBuRqnPB": 47,
    "CH6mG": 23,
    "VDZ7NwN": 81,
    "oUQQyM2": 93,
    "g": 5,
    "7W": 61,
    "qSQo": 4,
    "xxybGNl30": 22,
    "xlVzjhC": 23,
    "lUCPge": 31,
    "v": 5,
    "1nFf": 45,
    "MrLFxdP": 75,
    "wgx": 14,
    "Qg": 6,
    "mAZGItwOF": 35,
    "Z42saa5DH": 21,
    "uemP": 66,
    "FEleHM": 94,
    "AbnK": 99,
    "wYWjlo": 43,
    "cNs": 14,
    "mgsCzEu": 92,
    "C": 27,
    "t9eVG5aRkr": 96,
    "A": 86,
    "qGZ": 36,
    "EUBTsTY": 49,
    "VxK7S": 77
}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS by setting headers
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Parse query params to get the names
        query_components = parse_qs(self.path[2:])

        # Extract names and get corresponding marks
        names = query_components.get('name', [])
        if not names:
            self.send_response(400)  # Bad Request if no names are provided
            self.wfile.write(json.dumps({"error": "No names provided"}).encode())
            return
        
        marks = [student_marks.get(name, "Not Found") for name in names]

        # Send the JSON response
        response = json.dumps({"marks": marks})
        self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
