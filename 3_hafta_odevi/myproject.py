from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "This API allows you to retrieve the latest malicious URLs from URLhaus. Use the endpoint '/malware/<int:n>' to get the most recent 'n' malicious URLs!"})

@app.route("/query")
def query():
    query = request.args.get("q")
    if query in ["url", "host", "payload", "tag"]:
        url = "https://urlhaus-api.abuse.ch/v1/urls/recent/?query=" + query
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": response.text})
    else:
        return jsonify({"message": "Invalid query parameter. Please use one of the following: url, host, payload, tag."})

@app.route("/malware/<int:n>")
def number(n):
    if n > 0:
        response = requests.get("https://urlhaus-api.abuse.ch/v1/urls/recent/")
        if response.status_code == 200:
            data = response.json()
            urls = data['urls']
            last_n_urls = urls[-n:]
            return jsonify(last_n_urls)
        else:
            return jsonify({"error": response.text})
    else:
        return jsonify({"message": "Invalid number parameter. Please use a positive integer for 'n'."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
