#Author guo
class CommonUtil:
    #判断一个字符串是否在另一个字符串中

    def is_contain(self,str1,str2):

        flag=None
        if str1 in str2:
            flag=True

        else:
            flag=False

        return flag