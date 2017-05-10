from flask import Flask, request
import requests, json

app = Flask(__name__)

key=json.load(open("database/key","r"))
ACCESS_TOKEN = key.get('momocoFB','')


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    aaa = open('database/testing','r')
    bbb = json.load(aaa)
    bbb.update( {tool.date(1,''):data})
    aaa = open('database/testing','w')
    json.dump(bbb,aaa)
    aaa.close()
    
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message+' '+message)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
