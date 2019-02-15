import itchat
from itchat.content import *

def show_list_friends(list_friends):
    if len(list_friends) == 0 :
        print("朋友列表为空")
    else:
        print("该账号总共有" + str(len(list_friends))+ "个朋友")
        seq = 1
        for friend in list_friends:
            print("第" + str(seq) + "个朋友的username：" + friend.UserName + ",nickname：" + friend.NickName)
            seq += 1

#显示第num个朋友的key值和对应内容
def show_char_friends(list_friends,num):
    if len(list_friends) == 0 :
        print("公众号列表为空")
    else:
        if num > len(list_friends) - 1 or num < 0 :
            print("输入的num不合法！！！")
        else:
            for key in list_friends[num]:
                print(key + ":" + str(list_friends[num][key]))

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    list_friends = itchat.get_friends(update=True)
    show_list_friends(list_friends)
    show_char_friends(list_friends,2)
