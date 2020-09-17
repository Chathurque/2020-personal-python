import json
import os
import argparse

class Run:
    def filedata(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-i', '--init')
        self.parser.add_argument('-u', '--user')
        self.parser.add_argument('-e', '--event')
        self.parser.add_argument('-r', '--repo')

        for (root, dirs, files) in os.walk(path):
            for file in files:
                if file[-5:] == '.json':
                    f = open(path + '\\' + file, 'r', encoding = 'utf-8')
        while True:
            line = f.readline()
            if not line:
                continue
                js = json.loads(line)
                if not js['type'] in ['PushEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent']:
                    continue
                if not js['ine = f.readline()actor']['login'] in self.UserEvent.keys():
                    self.UserEvent[js['actor']['login']] = {'PushEvent':0, 'IssueCommentEvent':0, 'IssuesEvent':0, 'PullRequestEvent':0}
                if not js['repo']['name'] in self.RepoEvent.keys():
                    self.RepoEvent[js['repo']['name']] = {'PushEvent':0, 'IssueCommentEvent':0, 'IssuesEvent':0, 'PullRequestEvent':0}
                if not js['actor']['login'] in self.UserRepo.keys():
                    self.UserRepo[js['actor']['login']] = {}
                    self.UserRepo[js['actor']['login']][js['repo']['name']] = {'PushEvent':0, 'IssueCommentEvent':0, 'IssuesEvent':0, 'PullRequestEvent':0}
                elif not js['repo']['name'] in self.UserRepo[js["actor"]["login"]].keys():
                    self.UserRepo[js['actor']["login"]][js['repo']['name']] = {'PushEvent':0, 'IssueCommentEvent':0, 'IssuesEvent':0, 'PullRequestEvent':0}
                    self.UserEvent[js['actor']['login']][js['type']] += 1
                    self.RepoEvent[js['repo']['name']][js['type']] += 1
                    self.UserRepo[js['actor']["login"]][js['repo']['name']][js['type']] += 1
                else:
                    break
        with open('UserEvent.json', 'w', encoding = 'utf-8') as f:
            json.dump(D.UserEvent, f)
        with open('RepoEvent.json', 'w', encoding = 'utf-8') as f:
            json.dump(D.RepoEvent, f)
        with open('UserRepo.json', 'w', encoding = 'utf-8') as f:
            json.dump(D.UserRepo, f)
        f.close()

    def putoutUser(user, event):
        q = open('UserEvent.json', 'r', encoding = 'utf-8').read()
        f = json.loads(q)
        print(f[user].get(event))

    def putoutRepo(repo, event):
        q = open('RepoEvent.json', 'r', encoding = 'utf-8').read()
        f = json.loads(q)
        print(f[repo].get(event))

    def putoutUserRepo(user, repo, event):
        q = open('UserRepo.json', 'r', encoding = 'utf-8').read()
        f = json.loads(q)
        print(f[user][repo].get(event))
