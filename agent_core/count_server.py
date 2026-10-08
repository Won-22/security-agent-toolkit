from flask import Flask, request

app = Flask(__name__)
received = []
# 1. received 라는 변수를 만들어 빈 리스트를 담으세요

@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.get_json()
    received.append(event)
    return {"status": "ok", "count": len(received)}, 200
    # 2. received 에 event 를 더하세요

    # 3. {"status": "ok", "count": received 의 길이} 와 200 을 return 하세요



app.run(port=5004)
