#encoding = utf-8
import urllib
import urllib2
import cookielib
import sys
import os
import re
import shutil
from hashlib import md5
reload(sys)
sys.setdefaultencoding('utf-8')

class target:
    def __init__(self, url, postUrl):
        self.url = url
        self.postUrl = postUrl
        

def cc98GetLinks(params):
    targets = []
    ## get cookie
    # if cookieFile is not defined, use 'username' and 'password' in config file
    if not params.cookieFile.strip():
        
        cookie = cookielib.MozillaCookieJar('98cookie.txt')
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = {
            'a': 'i',
            'u':params.username,
            'p':md5(params.password.encode()).hexdigest(),
            'userhidden':'2',
            'Agent-User': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48 Safari/537.36',
            'Origin': 'http://www.cc98.org',
            'Referer': 'http://www.cc98.org/index.asp'}
        postdata = urllib.urlencode(postdata)
        result = opener.open(params.loginUrl, postdata)
        print result.read().decode('utf-8')
        cookie.save(ignore_discard=True, ignore_expires=True)
    else:
        cookie = cookielib.MozillaCookieJar()
        cookie.load(filename=params.cookieFile, ignore_discard=True, ignore_expires=True)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # open board url
    for page in range(1, params.nPage+1):
        pageUrl = params.pageFormat % page
        print 'analyzing page ' + str(page)
        resultPage = opener.open(pageUrl)
        contentPage = resultPage.read().decode('utf-8')
        
        #find post
        patternPost = re.compile(params.postReg)
        posts = re.findall(patternPost, contentPage)
        for post in posts:
            postUrl = params.prefix + post[params.postRegIdx]
            targetsPost = getOnePost(opener,postUrl, params)
            if len(targetsPost) > 0:
                targets.append(targetsPost)

    return targets

def getOnePost(opener, postUrl, params):
    resultPost = opener.open(postUrl)
    contentPost = resultPost.read().decode('utf-8')
    patternTarget = re.compile(params.targetReg)
    targetUrls = re.findall(patternTarget, contentPost)
    targetUrlsUnique = []
    targetsPost = []
    for url in targetUrls:
        targetUrlsUnique.append( url[params.targetRegIdx] )
    targetUrlsUnique = set(targetUrlsUnique)
    targetUrlsUnique = list(targetUrlsUnique)
    for url in targetUrlsUnique:
        targetsPost.append(target(url, postUrl))
    return targetsPost
    
def saveData(targets, params):
    nPost = len(targets)
    if not os.path.exists(params.savePath):
        os.makedirs(params.savePath)
    else:
        shutil.rmtree(params.savePath)
        os.makedirs(params.savePath)
        
    k = 0
    fid = open(params.savePath + 'urlinfo.txt', 'w')
    for targetPost in targets:
        for target in targetPost:
            fid.write(str(k) + ' ' + target.postUrl + '\n')
            filename = params.savePath + str(k) + '.jpg'
            urllib.urlretrieve(target.url, filename)
            k = k + 1
    fid.close()
        
        
