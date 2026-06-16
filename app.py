from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/proxy")
def proxy():
    url = request.args.get("url")
    if not url:
        return "Missing url", 400

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "",
    }

    r = requests.get(url, headers=headers, stream=True)

    return Response(
        r.iter_content(chunk_size=1024),
        content_type=r.headers.get("Content-Type", "application/octet-stream")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
