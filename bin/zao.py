# -*- coding: utf-8 -*-
from qqbot import qqbotsched
@qqbotsched(hour='7',minute='30')
def mymorn(bot):
    gl=bot.List('group','养老专用群')
    gk=bot.List('group','腾讯新闻')
    if gl is not None:
        for group1 in gl:
            bot.SendTo(group1,'起床了懒猪们,小夕要嫌弃你们了!')
    if gk is not None:
        for group2 in gk:
            bot.SendTo(group2,'起床了懒猪们,小夕要嫌弃你们了!')
