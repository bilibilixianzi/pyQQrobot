# -*- coding: UTF-8 -*-
from __future__ import division
import re
import os
import time
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request
import requests
def onQQMessage(bot, contact, member, content):

    if bot.isMe(contact, member):
        pass
    else:
        if '@ME' in content:
            if len(content)<=7:
                line=['叫人家干嘛?','小夕正忙没空.','懒得理你!','有什么问题嘛?',
                      '乌拉','别艾特我，有本事艾特群主啊!','略略略','德玛西亚万岁',
                      '需要什么帮助嘛?','www.baidu.com','喵喵喵喵喵?','我被猪艾特了',
                      '(委屈)','(-.-)','嘤嘤嘤','出现了,垃圾怪','群主说过,皮一下可以,皮几万不行!',
                      '一首凉凉送给你呀!','8月10日,爱情公寓','小夕想要个VIP行么?',
                      '小夕想要个SVIP，你能给嘛?','艾特我,暑假长肉5斤',
                      '有空艾特我,还不如去撩妹子.','垃圾垃圾垃圾','小夕想吃肉肉',
                      '摸一下猪','emmmmm','猥琐,哼!','妈呀,有变态!',
                      '八嘎,hentai,无路赛','洗内----','OωO']
                bot.SendTo(contact,'@'+member.name+' '+str(line[random.randint(1,32)]))
            else:
                a={'你是谁':'我是最可爱的小夕呀','出来':'叫我出来我就出来,我不要面子嘛','亲亲抱抱举高高':'嘿嘿嘿',
                   '你好':'你好呀!','乌拉':'嘤嘤嘤','666':'23333','王者':'垃圾游戏','举高高':'小夕想再来一次!',
                   '老司机':'这是个多么牛逼的人啊,你怎么直呼他的名字','农药':'垃圾游戏','嘿嘿':'咕嘿嘿',
                   '可爱':'小夕最最最最可爱啦','脾气':'我觉得还行','LOL':'垃圾游戏','兔子':'炖了吧!','猫咪':'喵呜!',
                   '亲亲':'mua','mua':'吧唧一口','张子涵':'富婆','滚':'gun啊','抱抱':'抱老子','QAQ':'QwQ',
                   '嘤嘤':'小夕一拳一只嘤嘤怪!','富婆':'哪有富婆介绍给小夕一个','上了你':'我小夕今天就要日得你喵喵叫!',
                   '哭唧唧':'不哭不哭,要向小夕一样坚强','机器人':'机器人怎么了,男人都是大猪蹄子呢!','大佬':'傻子',
                   '不行啊':'你怎么能说自己不行呢!','二勇子':'别拿智障吓唬我','猪':'走开啊,我晕猪啊!','傻':'呵呵',
                   '笑一个':'就不笑,小夕凭什么听你的!','钱':'你不如去援交赚钱!','你看':'你傻了吧,小夕是机器人',
                   '再见':'哼,不理你了,亲亲抱抱举高高才能好的那种!','你走':'小夕今天就在这睡了!','么么哒':'爱您 biu-'}
                flag=False
                for i in a:
                    if i in content:
                        bot.SendTo(contact,'@'+member.name+' '+a[i])
                        flag=True
                        break
                if '图片' in content:
                    a=['二次元','请问您今天要来点兔子嘛','Island','从零开始的异世界生活','魔法少女伊莉雅', 
                       '变态王子与不笑猫','杀戮天使','舰队Collection','citrus','slow start',
                       '摇曳百合','轻音少女','紫罗兰永恒花园','就算是哥哥,有爱就没问题了','热诚传说',
                       '干物妹小埋','绯弹亚里亚','灼眼的夏娜','龙之界点','零之使魔','地狱少女',
                       '约会大作战','魔法禁书目录','某科学的超电磁炮','异界少女召唤术','珈百璃的堕落',
                       'P站','妖精的尾巴','魔卡少女樱','狐妖小红娘','工作细胞','游戏人生','我的青春恋爱物语果然有问题',
                       '小林家的龙女仆','猫咪日常','未闻花名','远坂凛','宫内莲华','中二病也要谈恋爱',
                       '凉宫春日的忧郁','埃罗芒阿老师','南小鸟','路人女主的养成方法','urara迷路帖','魔法少女小圆']
                    #keyword='二次元高清壁纸'
                    keyword=a[random.randint(0,44)]+'高清壁纸'
                    x=[]
                    params=[]
                    for i in range(1):
                        params.append({
                            'tn': 'resultjson_com','ipn': 'rj','ct': 201326592,
                            'is': '','fp': 'result',
                            'queryWord': keyword,'cl': 2,
                            'lm': -1,'ie': 'utf-8','oe': 'utf-8',
                            'adpicid': '','st': -1,'z': '',
                            'ic': 0,'word': keyword,'s': '',
                            'se': '','tab': '','width': '',
                            'height': '','face': 0,'istype': 2,
                            'qc': '','nc': 1,'fr': '','pn': i,
                            'rn': 30,'gsm': '3c','1488942260214': ''
                            })
                    url = 'https://image.baidu.com/search/acjson'
                    dataList= []
                    for i in params:
                        dataList.append(requests.get(url,params=i).json().get('data'))
                    bb=0
                    for j in dataList:
                        for i in j:
                            if i.get('thumbURL')!=None:
                                x.append(i.get('thumbURL'))
                                bb+=1
                    bot.SendTo(contact,x[random.randint(0,bb)])
                    flag=True
                if flag==False:
                    bot.SendTo(contact,'@'+member.name+' 小夕听不懂啊(喵的一下就哭了)')
        #elif '新建文件' in content:
        #    file=open("gushi.txt","w")
        #    file.close()
        #elif '我要添加故事' in content:
        #    a=split(' ',1)[1]
        #    file=open("gushi.txt","w")
        #    file.write(a+'\n')
        #    bot.SendTo(contact,'添加成功!')
        #elif '讲个故事' in content:
        #    file=open("gushi.txt","r")
        #    line=file.readlines()
        #    file.close()
        #    a=random.randint(1,20)
        #    bot.SendTo(contact,a+'.'+line[a])
        if '二次元图片搜索' in content:
            a=['二次元','请问您今天要来点兔子嘛','Island','从零开始的异世界生活','魔法少女伊莉雅',
           '变态王子与不笑猫','杀戮天使','舰队Collection','citrus','slow start',
           '摇曳百合','轻音少女','紫罗兰永恒花园','就算是哥哥,有爱就没问题了','热诚传说',
           '干物妹小埋','绯弹亚里亚','灼眼的夏娜','龙之界点','零之使魔','地狱少女',
           '约会大作战','魔法禁书目录','某科学的超电磁炮','异界少女召唤术','珈百璃的堕落',
           'P站','妖精的尾巴','魔卡少女樱','狐妖小红娘','工作细胞','游戏人生','我的青春恋爱物语果然有问题',
           '小林家的龙女仆','猫咪日常','未闻花名','远坂凛','宫内莲华','中二病也要谈恋爱',
           '凉宫春日的忧郁','埃罗芒阿老师','南小鸟','路人女主的养成方法','urara迷路帖','魔法少女小圆']
            #keyword='二次元高清壁纸'
            keyword=a[random.randint(0,44)]+'高清壁纸'
            x=[]
            params=[]
            for i in range(1):
                params.append({
                    'tn': 'resultjson_com','ipn': 'rj','ct': 201326592,
                    'is': '','fp': 'result',
                    'queryWord': keyword,'cl': 2,
                    'lm': -1,'ie': 'utf-8','oe': 'utf-8',
                    'adpicid': '','st': -1,'z': '',
                    'ic': 0,'word': keyword,'s': '',
                    'se': '','tab': '','width': '',
                    'height': '','face': 0,'istype': 2,
                    'qc': '','nc': 1,'fr': '','pn': i,
                    'rn': 30,'gsm': '3c','1488942260214': ''
                    })
            url = 'https://image.baidu.com/search/acjson'
            dataList= []
            for i in params:
                dataList.append(requests.get(url,params=i).json().get('data'))
            bb=0
            for j in dataList:
                for i in j:
                    if i.get('thumbURL')!=None:
                        x.append(i.get('thumbURL'))
                        bb+=1
            bot.SendTo(contact,x[random.randint(0,bb)])
        elif '二勇子 ' in content:
            bot.SendTo(contact,'大傻逼!')
        elif '老司机' in content:
            bot.SendTo(contact,'mua~')
        elif '猪 ' in content:
            bot.SendTo(contact,'摸一下猪!')
        elif '随机选择 'in content:
            a=content.split(' ',1)[1]
            b=a.split(' ')
            c=len(b)-1
            bot.SendTo(contact,b[random.randint(0,c)])
        elif '搜索 ' in content:
            a=content.split(' ',1)[1].split(' ',1)#(修改注意)a=网盘 搜索 not in a
            curl='https://pan.sov5.cn/'#默认网盘
            flag=False
            b={'网盘':'https://pan.sov5.cn/',
               '二次元':'http://2.sov5.cn/',
               '问答':'https://wenda.sov5.cn/',
               '电影':'https://v.sov5.cn/',
               '资源':'https://0.sov5.cn/'}
            for i in b:
                if a[0] in i:
                    curl=b[i]
            if '网盘' in a[0]:
                flag=True
            bb=str(a[1].encode('utf-8'))
            bbb=bb[2:-1].replace('\\x','%')
            url=curl+'search?q='+bbb
            response=request.urlopen(url)
            html=response.read().decode("utf-8")
            if flag==True:
                ze='<a class="s" href=".*?" target="_blank">'
            else:
                ze='<a class="s" target="_blank"\s+href=".*?">'
            cljy=re.findall(ze,html)
            href=[]
            lj=[]
            sss=''
            for i in cljy:
                href.append(re.findall('href=".*?"',i)[0])
            for i in href:
                lj.append(re.findall('".*?"',i)[0].replace('"',''))
            if flag==True:
                c=len(lj)
                for i in range(0,c):
                    if i%2==0:
                        sss=sss+lj[i]+'\n'
            else:
                for i in lj:
                    sss=sss+curl[:-1]+i+'\n'
            bot.SendTo(contact,sss[:-1])
        elif '发送消息' in content:
            a=content.split(' ',1)[1]
            aa=a.split(' ',1)[0]
            b=a.split(' ',1)[1]
            g=bot.List('group',aa)
            for group in g:
                bot.SendTo(group,b)
                    
        elif '删除自定义回复' in content:
            e=content.split(' ',1)
            file=open("huifu.txt","r")
            line=file.readlines()
            file.close()
            y=e[1].split(' ',1)
            u=0
            q=False
            for i in line:
                if i.split(' ',1)[0]==y[0]:
                    q=True
                    break
                u=u+1
            if q==True:
                del line[u]
                file=open("huifu.txt","w")
                file.writelines(line)
                file.close()
                bot.SendTo(contact,' 删除成功!')
            else:
                bot.SendTo(contact,' 删除失败!请检查关键词正确性!')
        elif '添加自定义回复' in content:
            flag=True
            a=content.split(' ',1)
            file=open("huifu.txt","r")
            for i in file.readlines():
                b=a[1].split(' ',1)
                if b[0]==i.split(' ',1)[0]:
                    bot.SendTo(contact,'@'+member.name+' 已有自定义回复，请选择更改!')
                    flag=False
            if flag==True:
                file=open("huifu.txt","a")
                file.write(a[1]+'\n')
                bot.SendTo(contact,'添加回复成功!')
        elif '修改自定义回复' in content:
            g=content.split(' ',1)
            file=open("huifu.txt","r")
            line=file.readlines()
            file.close()
            h=g[1].split(' ',1)
            f=0
            r=False
            for i in line:
                if i.split(' ',1)[0]==h[0]:
                    r=True
                    break
                f=f+1
            if r==True:
                line[f]=h[0]+' '+h[1]+'\n'
                file=open("huifu.txt","w")
                file.writelines(line)
                file.close()
                bot.SendTo(contact,'更改完成!')
            else:
                bot.SendTo(contact,'@'+member.name+' 更改失败,可能不存在此条回复!')
        elif content=='自定义回复查询':
            file=open("huifu.txt","r")
            line=file.readlines()
            file.close()
            ll=''
            for i in line:
                if ' ' in i:
                     ll=ll+i.split(' ',1)[0]+':'+i.split(' ',1)[1]
            bot.SendTo(contact,ll)
        elif '查询群成员列表' in content:
            bot.SendTo(contact,str(bot.List(bot.List('group','养老专用群')[0])))
        elif '查询天气' in content:
            h=content.split(' ',1)
            x=re.findall(u"[\u4e00-\u9fa5]+",h[1])[0]
            file=open("C:/Users/lendo/Desktop/pyQQ/daim.txt","r")
            line=file.readlines()
            file.close()
            flag=False
            for i in line:
                a=re.findall(u"[\u4e00-\u9fa5]+",i)[0]
                if x in a or a in x:
                    b=re.findall(r"\d+",i)
                    flag=True
                    break
            if flag==False:
                bot.SendTo(contact,'查询失败，请确认城市信息是否正确!')
            elif x=='呼伦贝尔':
                bot.SendTo(contact,'http://www.weather.com.cn/weather/101081013.shtml')
            else:
                c='http://www.weather.com.cn/weather/'
                d=c+b[0]+'.shtml'
                resp=urlopen(d)
                soup=BeautifulSoup(resp,'html.parser')
                tagToday=soup.find('p',class_="tem")
                try:
                    temperatureHigh=tagToday.span.string  
                except AttributeError as e:
                    temperatureHigh=tagToday.find_next('p',class_="tem").span.string  
                temperatureLow=tagToday.i.string  
                weather=soup.find('p',class_="wea").string
                if '℃' in str(temperatureHigh):
                    b=''
                else:
                    b='℃'
                mm=x+'地区今天天气信息:\n'+'最低温度:'+ temperatureLow +'\n最高温度:'+ temperatureHigh +b+'\n天气:'+ weather
                bot.SendTo(contact,mm)
        elif '进制转换' in content:
            flag=True
            if '十进制转' in content:
                number =int(re.findall(r"\d+",str(content))[0])
                if '十六进制' in content:
                    aa=hex(number)
                elif '八进制' in content:
                    aa=oct(number)
                elif '二进制' in content:
                    aa=bin(number)
                else:
                    aa='不给算,哼-.-'
            else:
                flag=False
            #elif '转十进制' in content:
            #    string=re.findall(r'[0-9a-zA-Z]+',str(content))[0]
            #    lit=[]
            #    if lit!=re.findall(r'[g-zG-Z]',string):
            #        bot.SendTo(contact,'转换失败,请检查正确性.')
            #        flag=False
            #    else:
            #        if '十六进制' in content:
            #            aa=int(str(string),16)
            #        elif '八进制' in content:
            #            aa=oct(str(string),8)
            #        elif '二进制' in content:
            #            aa=int(str(string),2)
            #        else:
            #            aa='不给算,哼-.-'
            if flag==True:
                bot.SendTo(contact,aa)
        elif '百度' in content:
            aa=content.split(' ',1)[1]
        #    ba=re.findall(u"[\u4e00-\u9fa5]+",aa)[0]
            ba=str(aa)
            keyword=ba
            try:
                kv={'wd':keyword}
                r=requests.get("http://www.baidu.com/s",params=kv)
                bot.SendTo(contact,r.request.url)
            except:
                bot.SendTo(contact,'小夕尽力了,没找到客官要的东西!')
        elif '圆周率' in content and '位' in content:
            time1=time.time()
            flag=True
            number =int(re.findall(r"\d+",str(content))[0])
            if number>35000:
                number=35000
                flag=False
            number1= number+10
            b = 10**number1
            x1 = b*4//5
            x2 = b// -239
            he = x1+x2
            number *= 2
            for i in range(3,number,2):
                x1 //= -25
                x2 //= -57121
                x = (x1+x2) // i
                he += x
            pai = he*4
            pai //= 10**10
            paistring=str(pai)
            result=paistring[0]+str('.')+paistring[1:len(paistring)]
            bot.SendTo(contact,result)
            time2=time.time()
            bot.SendTo(contact,u'总共耗时：'+ str(time2 -time1)+ 's')
            if flag==False:
                bot.SendTo(contact,'数据过大,只显示35000位!')
        #    bot.SendTo(contact,ba)
        #elif '禁言' in content and '过气老群主' in member.name:
        #    x=content.split(' ')
        #    c=re.findall(r"\D+",str(x[2]))
        #    if '分钟' or 'min' in c:
        #        b=60
        #    elif '秒' or 's' or 'S' in c:
        #        b=1
        #    elif '小时' or 'h' or 'H' in c:
        #        b=3600
        #    else:
        #        b=1
        #    d=re.findall(r"\d+",str(x[2]))
        #    e=int(d[0])
        #    g1=bot.List('group','养老专用群')
        #    group=g1[0]
        #    membs=bot.List(group,str(x[1]))
        #    bot.GroupShut(group,membs,e*b)
        #    bot.SendTo(contact,'祝小黑屋中过得愉快!')
        #    print(membs)
        #    print(type(membs))
        #elif '设置管理员' in content and '过气老群主' in member.name:
        #    y=content.split(' ')
        #    g2=bot.List('group','养老专用群')
        #    group=g2[0]
        #    membs=bot.List(group,str(y[1]))
        #    bot.GroupSetAdmin(group,membs,admin=True)
        #    bot.SendTo(contact,'管理员设置成功')
        #elif '取消管理员' in content and '过气老群主' in member.name:
        #    z1=content.split(' ')
        #    g3=bot.List('group','养老专用群')
        #    group=g3[0]
        #    membs=bot.List(group,str(z1[1]))
        #    bot.GroupSetAdmin(group,membs,admin=False)
        #    bot.SendTo(contact,'管理员取消成功')
        #elif '设置名片' in content and '过气老群主' in member.name:
        #    z2=content.split(' ')
        #    g4=bot.List('group','养老专用群')
        #    group=g4[0]
        #    membs=bot.List(group,str(z2[1]))
        #    bot.GroupSetAdmin(group,membs,str(z2[2]))
        #    bot.SendTo(contact,'修改名片成功!')
        else:
            if '媳妇' in content:
                bot.SendTo(contact,'@'+member.name+' 我在QωQ')
            elif '小夕' in content:
                bot.SendTo(contact,'我在OωO')
            else:
                file=open("huifu.txt","r")
                lll=file.readlines()
                file.close()
                flag=False
                for i in lll:
                    if i.split(' ',1)[0]==content:
                        bot.SendTo(contact,i.split(' ',1)[1][:-1])
                        flag=True
                        break
                    
            #elif 'sb' or 'Sb' or 'SB' or 'sB' or '傻逼' or '操' in content:
            #    bot.SendTo(contact,'@'+member.name+' 不许骂人,你个臭居居!')
