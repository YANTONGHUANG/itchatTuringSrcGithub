import itchat
from itchat.content import *

#显示所有公众号列表内容
def show_list_mps(list_mps):
    if len(list_mps) == 0 :
        print("公众号列表为空")
    else:
        print("该账号总共关注了" + str(len(list_mps))+ "个公众号")
        seq = 1
        for mps in list_mps:
            print("第" + str(seq) + "个公众号的username：" + mps.UserName + ",nickname：" + mps.NickName)
            seq += 1

#显示第num个公众号的key值和对应内容
def show_char_mps(list_mps,num):
    if len(list_mps) == 0 :
        print("公众号列表为空")
    else:
        if num > len(list_mps) - 1 or num < 0 :
            print("输入的num不合法！！！")
        else:
            for key in list_mps[num]:
                print(key + ":" + str(list_mps[num][key]))

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    list_mps = itchat.get_mps(update=True)
    show_list_mps(list_mps)
    show_char_mps(list_mps,2)
