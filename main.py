import tls_client
session = tls_client.Session(
    client_identifier="safari_15_6_1"
)

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1" # VERY IMPORTANT DO NOT REMOVE OR CHANGE !
}

response = session.get("https://api.bloxflip.com/games/crash", headers=headers)
print(response.status_code)
