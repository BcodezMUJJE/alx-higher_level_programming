#!/usr/bin/python3

"""
This script takes two arguments: the repository name and the owner name.
It uses the GitHub API to list 10 commits (from most recent to oldest)
of the specified repository by the given owner.
"""

import requests
import sys

def list_commits(repo, owner):
    """
    Lists 10 commits of the specified repository by the given owner.

    :param repo: The repository name.
    :param owner: The owner name.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'per_page': 10}
    
    try:
        response = requests.get(url, params=params)
        commits = response.json()

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repository_name, owner_name)
