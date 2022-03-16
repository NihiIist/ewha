from http.server import BaseHTTPRequestHandler, HTTPServer


def total(num1, num2):
    return num1 + num2


class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):  # pylint: disable=invalid-name
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes(
                f"""
        <html><head>
        <title>Server</title>
        <meta charset="UTF-8">
        </head>
        <body>
        <h1>실습용 서버입니다.</h1>
        <p>5+10은 {total(5, 10)}입니다</p>
        </body></html>
        """,
                "utf-8",
            )
        )

        val = {
            "asd": 1,             "asd": 2
        }


if __name__ == "__main__":
    webServer = HTTPServer(("0.0.0.0", 8080), SimpleServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
