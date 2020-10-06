import os, logging, json
from requests import post
from py_random_words import RandomWords


accessToken = os.environ['ACCESS_TOKEN']

def replyText(message):
    rnd_word = RandomWords()
    return " ".join([rnd_word.get_word() for _ in range (10)])

def reply(accessToken, token, message):
    url = 'https://api.line.me/v2/bot/message/reply'
    headers = {'Authorization': 'Bearer ' + accessToken }
    data = {
        "replyToken": token,
        "messages":[{
            "type":"text",
            "text": replyText(message)
        }]
    }
    return post(url, headers=headers, json=data)



def answer(event, context):
    body = json.loads(event['body'])

    event = body['events'][0]
    token = event['replyToken']
    text = event['message']['text']
    postResult = reply(accessToken, token, text)
    print(postResult.json())


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": postResult.json()
        }),
    }
