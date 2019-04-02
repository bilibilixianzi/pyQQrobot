# -*- coding: utf-8 -*-
from qqbot import qqbotsched
@qqbotsched(hour='12',minute='00')
def mytask(bot):
    gl=bot.List('group','养老专用群')
    gk=bot.List('group','腾讯新闻')
    if gl is not None:
        for group1 in gl:
            bot.SendTo(group1,'中午啦,该吃饭啦!')
    if gk is not None:
        for group2 in gk:
            bot.SendTo(group2,'中午啦,该吃饭啦!')
