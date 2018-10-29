# -*- coding: utf-8 -*-
import git, os, sys, shutil,time
from git import RemoteProgress

filePath = os.path.abspath(sys.argv[0])
filePathArr = filePath.split('/')
del filePathArr[len(filePathArr)-1]
filePath = '/'.join(filePathArr)

# print(filePath)

# # $ git push --force -u https://${Token}@github.com/goldhan/goldhan.github.io.git master:master

# gitUrl = 'https://github.com/goldhan/MockJSON.git'
# gitToken = '340bff36fbbd10767e0078b5f4a60bd9342f0c35'
# filePath = filePath + '/GDWeatherStation'
# isHave = os.path.exists(filePath)
# if isHave:
#     shutil.rmtree(filePath) 
#     # os.rmdir(filePath)

# repo = git.Repo.clone_from('https://' + gitToken + '@github.com/goldhan/MockJSON.git', filePath, branch='master')

# jsonStr = r'{"value1": [["About Me","QQ Group:\n 6XXXXXXXXX \n Welcome to add ......"],["title2","detail2"],["title3","detail3"]]}'

# filePath = filePath + '/GDWeather.json'
# with open(filePath, 'w') as f:
#     f.write(jsonStr)
#     f.close()


# heads = repo.heads
# master = heads.master       # lists can be accessed by name for convenience
# master.commit               # the commit pointed to by head called master
# master.rename('new_name')   # rename heads
# master.rename('master')


class MyProgressPrinter(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")

class UploadWithGit(object):

    def __init__(self, filePath, token, url):
        self.filePath = filePath + '/GDWeatherStation'
        isHave = os.path.exists(self.filePath)
        print(self.filePath)
        if isHave:
            shutil.rmtree(self.filePath) 
            print('删除旧文件，重新Clone新文件')
        self.repo = git.Repo.clone_from('https://' + token + '@github.com/goldhan/MockJSON.git', self.filePath, branch='master')
        self.filePath = self.filePath + '/GDWeather.json'

    def upload(self, jsonStr):
        # self.filePath = self.filePath + '/GDWeather.json'
        with open(self.filePath, 'w') as f:
            f.write(jsonStr)
            f.close()
        index = self.repo.index
        index.add(['GDWeather.json'])
        index.commit('this is GDWeatherStationSever push......')
        self.repo.remote().push()
        print('push successful')


gitToken = '3bcb8832b28539212bc9f3ebffa7dc1848b443f1'
gitUrl = 'https://github.com/goldhan/MockJSON.git'
upGit = UploadWithGit(filePath,gitToken,gitUrl)
num = 1
while 1 :
    num = num + 1
    jsonStr = r'{"value' + str(num) + r'": [["About Me","QQ Group:\n 6XXXXXXXXX \n Welcome to add ......"],["title2","detail2"],["title3","detail3"]]}'
    upGit.upload(jsonStr)
    time.sleep(60)