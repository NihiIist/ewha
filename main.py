"""
간단한 서버 코드입니다.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer


def total(num1, num2):
    """
    num1과 num2 더하기
    """
    return num1 + num2


class SimpleServer(BaseHTTPRequestHandler):
    """
    Server class
    """

    def do_GET(self):  # pylint: disable=invalid-name
        """
        GET 요청 처리 함수입니다.
        """
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
        <h1>우성의 실습용 서버입니다.</h1>
        <p>5+10은 {total(5, 10)}입니다</p>
        </body></html>
        """,
                "utf-8",
            )
        )


if __name__ == "__main__":
    webServer = HTTPServer(("0.0.0.0", 8080), SimpleServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
