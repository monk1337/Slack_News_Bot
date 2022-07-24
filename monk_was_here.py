from newsapi.articles import Articles
import requests
import json


url = 'https://hooks.slack.com/services/T8N4B1741/B8NPU0h'


a = Articles(API_KEY="25ea")

payload = {
    "attachments": [
        {
            "title": "The Further Adventures of Slackbot",

            "author_icon": "http://a.slack-edge.com/7f18https://a.slack-edge.com/bfaba/img/api/homepage_custom_integrations-2x.png",
            "image_url": "http://i.imgur.com/OJkaVOI.jpg?1"
        },
        {
            "title": "Headline",
            "text": "After @episod pushed exciting changes to a devious new branch back in Issue 1, Slackbot notifies @don about an unexpected deploy..."
        },
        {
            "fallback": "Read More About it.",
            "title": "Read More About it.",
            "callback_id": "comic_1234_xyz",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "recommend",
                    "text": "Full News",
                    "type": "button",
                    "url": "https://requests.example.com/cancel/r123456",
                    "value": "https://www.google.com"
                },
            ]
        }
    ]
}





result=[]
for i in a.get_by_popular(source="techcrunch")['articles']:
    result.append((i['title'],i['url'],i['urlToImage'],i['description']))

if len(result)<=5:

    for item in result:

        for i in payload['attachments']:
            if "author_icon" in i:
                i['title'] = item[0]
                i['image_url'] = item[2]
            if 'text' in i:
                i['text'] = item[3]

            if 'fallback' in i:

                for j in i['actions']:
                    j['url'] = item[1]

        r = requests.post(url, data=json.dumps(payload))



else:
    print(result[5:])




