#coding:utf-8
import requests,json,synAttack
import Admin
class Message():
    def __init__(self,setuSymbol=None):
        if setuSymbol!=None: self.setuS='&tag='+setuSymbol
        else: self.setuS=''
        self.Urls={'fanyi':'https://fanyi.youdao.com/','code':'https://ganyucode.rth1.one'}
    def _getSetuUrl(self):
        print("获取setu中...")
        try:
            pic=requests.get("https://api.lolicon.app/setu/v2?r18=0&num=1"+self.setuS,timeout=10)
            url=pic.json()['data'][0]['urls']['original']
            return url
        except requests.exceptions.ConnectionError:
            print("访问过快!!!")
            return "获取失败"
        except:
            return "获取失败"
    def gets(self,message,isAdmin):
        message=message.decode("utf-8")
        print("%s to chiose url"%message)
        if message=="shutdown":
            return False
        elif isAdmin:
            return message
        elif Admin.loginAndCommand(message):
            if Admin.loginAndCommand(message)=="Password Wrong":
                return "密码错误"
            elif Admin.loginAndCommand(message)=='OK':
                return "WhileTCommand"
        elif message=='setu' or message=="涩图": 
            return self._getSetuUrl()
        elif message.split(sep='&')[0]=='syn' or message.split(sep='&')[0]=='synAttack':
            sl=message.split(sep='&')
            if len(sl)==1: return "请输入攻击目标!!"
            sl.pop(0)
            synAttack.main(sl)
            return "对%s攻击开始"%str(sl)
        elif str(message) in self.Urls.keys(): 
            return self.Urls[str(message)]
        else: 
            return "https://ganyucode.rth1.one/404.html"