import itchat
from itchat.content import *

def show_chatrooms(list_chatrooms):
    if len(list_chatrooms) == 0 :
        print("群聊列表为空")
    else:
        print("该账号总共有" + str(len(list_chatrooms))+ "个群聊")
        seq = 1
        for chatroom in list_chatrooms:
            print("第" + str(seq) + "个朋友的username：" + chatroom.UserName + ",nickname：" + chatroom.NickName)
            seq += 1

#显示第num个群聊的key值和对应内容
def show_char_chatrooms(list_chatrooms,num):
    if len(list_chatrooms) == 0 :
        print("群聊列表为空")
    else:
        if num > len(list_chatrooms) - 1 or num < 0 :
            print("输入的num不合法！！！")
        else:
            for key in list_chatrooms[num]:
                print(key + ":" + str(list_chatrooms[num][key]))

#获取第num个群聊中所有群友的信息
def show_member_chatrooms(list_chatrooms,num):
    if len(list_chatrooms) == 0 :
        print("群聊列表为空")
    else:
        if num > len(list_chatrooms) - 1 or num < 0 :
            print("输入的num不合法！！！")
        else:
            chatUsername = list_chatrooms[num].UserName
            # print(chatUsername)
            memberList = itchat.update_chatroom(chatUsername,detailedMember=True)
            # print(memberList.MemberList[0].NickName)
            for member in memberList.MemberList:
                for key in member:
                    print(key + ":" + str(member[key]))

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    list_chatrooms = itchat.get_chatrooms(update=True)
    # show_chatrooms(list_chatrooms)
    # show_char_chatrooms(list_chatrooms,0)
    show_member_chatrooms(list_chatrooms,0)
    itchat.dump_login_status()
