from github import Github


token = "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"

g = Github(token)


topic = input()

repo_list = []

user = g.get_user()

repo_list = user.get_repos()


for repo in repo_list:

    if (topic in repo.get_topics()) and not(repo.archived):

        repo.create_label("deploy-to-Int12", color="f29513")

        print("LABELS IN "+repo.name)
        for label in repo.get_labels():
            print(label)

    elif (topic in repo.get_topics()) and (repo.archived):
        print(repo.name+" is archived repository can't create labels")
