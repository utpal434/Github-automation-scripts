from github import Github


token = "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"

g = Github(token)


topic = "web-node-14"

repo_list = []

user = g.get_user()

repo_list = user.get_repos()

for repo in repo_list:

    if(topic in repo.get_topics()):
        repo.create_label("deploy-to-Int9", color="f29513")

        for label in repo.get_labels():
            print(label)
