
import requests
import json
from pprint import pprint

token = "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"

userName = "utpal434"

topic = "web-node-14"

repo_list = []

header = {
    "Authorization": f"token {token}"
}

for repo in requests.get(
        f"https://api.github.com/users/{userName}/repos").json():

    if(topic in repo['topics']):
        print(repo['name'])
        repo_list.append(repo['name'])


data_label = {
    "name": "deploy-to-Int10"
}

for repo_name in repo_list:

    response = requests.post(f"https://api.github.com/repos/{userName}/{repo_name}/labels",
                             data=json.dumps(data_label), headers=header).json()
    pprint(response)

for repo_name in repo_list:
    print("LABELS IN "+repo_name)
    for label in requests.get(
            f"https://api.github.com/repos/{userName}/{repo_name}/labels").json():
        print(label['name'])
