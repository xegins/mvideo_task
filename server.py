from recommendation import Recommendation
from handler import get_recommends, parse_url

from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        sku, accuracy = parse_url(self.path)
        global recommendation
        recommends = get_recommends(recommendation, sku, accuracy)
        self._create_response(sku, recommends)

    def _create_response(self, sku, recommends):
        self.wfile.write(
            b'<html><head><link rel="icon" href="data:,">'
            b'<title>Recommendation</title></head>'
        )
        self.wfile.write(
            f'<body><p>List of recommendation for sku "{sku}":</p>'.encode()
        )
        self.wfile.write(f"<p>{recommends}</p>".encode())
        self.wfile.write(b"</body></html>")


def run_server(recommends_path: str = "recommends.csv",
               host: str = "localhost",
               port: int = 80) -> None:
    server_address = (host, int(port))
    globals()["recommendation"] = Recommendation(recommends_path)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Starting server on '{host}:{port}'")
    httpd.serve_forever()

