# -*- coding: utf-8 -*-

from github import Github

# First create a Github instance:

# # using username and password
# g = Github("goldhan", "hanjin117")

# or using an access token
g = Github("340bff36fbbd10767e0078b5f4a60bd9342f0c35")

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="340bff36fbbd10767e0078b5f4a60bd9342f0c35")

# Then play with your Github objects:
repo = g.get_repo("goldhan/MockJSON")
print(repo)
contents = repo.get_contents("")
while len(contents) > 1:
     file_content = contents.pop(0)
     if file_content.type == "dir":
         contents.extend(repo.get_contents(file_content.path))
     else:
         print(file_content)
