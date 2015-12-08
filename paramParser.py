import ConfigParser

class params:
    def __init__(self):
        self.form_user = ''
        self.form_pwd = ''
        self.username = ''
        self.password = ''
        self.cookieFile = ''
        self.loginUrl = ''
        self.pageFormat  = ''
        self.prefix = ''
        self.nPage = 0
        self.postReg = ''
        self.postRegIdx  = 0
        self.targetReg = ''
        self.targetRegIdx = 1
        self.savePath = ''


def paramParser(configFile):
    cf = ConfigParser.ConfigParser()
    flag = cf.read(configFile)
    if flag[0]==False:
        print 'Config file error!'
        exit(0)
    p = params()
    p.form_user = cf.get('login','form_user')
    p.form_pwd = cf.get('login','form_pwd')
    p.username = cf.get('login','username')
    p.password = cf.get('login','password')
    p.cookieFile = cf.get('login','cookieFile')
    p.loginUrl = cf.get('login','loginUrl')
    p.pageFormat  = cf.get('boardInfo','pageFormat')
    p.prefix = cf.get('boardInfo','prefix')
    p.nPage = cf.getint('boardInfo','nPage')
    p.postReg = cf.get('regularExp','postReg')
    p.postRegIdx = cf.getint('regularExp', 'postRegIdx')
    p.targetReg = cf.get('regularExp','targetReg')
    p.targetRegIdx = cf.getint('regularExp', 'targetRegIdx')
    p.savePath = cf.get('save','savePath')

    return p

if __name__ == '__main__':
    params = paramParser('config.ini')
    print params.form_user
    print params.nPage