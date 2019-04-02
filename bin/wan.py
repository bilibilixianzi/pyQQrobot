# -*- coding: utf-8 -*-
from qqbot import qqbotsched
@qqbotsched(hour='22',minute='30')
def mynite(bot):
    gl=bot.List('group','养老专用群')
    gk=bot.List('group','腾讯新闻')
    if gl is not None:
        for group1 in gl:
            bot.SendTo(group1,'晚安啦,小可爱们!')
    if gk is not None:
        for group2 in gk:
            bot.SendTo(group2,'晚安啦,小可爱们!')
