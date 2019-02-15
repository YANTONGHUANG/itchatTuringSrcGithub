'''
基于itchat和Turing机器人API接口，实现微信自动回复功能
'''

import itchat
from itchat.content import *
import mTuring

itchat.auto_login(hotReload=True)

# 带对象参数注册，对应消息对象将调用该方法
@itchat.msg_register(TEXT, isFriendChat=False, isGroupChat=True, isMpChat=False)
def text_reply(msg):
    # msg.user.send('%s: %s' % (msg.type, msg.text))
    if msg.ActualNickName == "hiker-huang":
        msg.user.send('%s: %s' % ("[饭团]", mTuring.turing_communicate_text(msg.text)))
        # for key in msg:
        #     print(key + ":" + str(msg[key]))
    # print(msg.user.NickName)

itchat.run(True)

