#Author guo
import json

class OperationJson:

    def __init__(self,file_path):
        self.file_path=file_path
        self.data=self.read_data()

    #读取json文件

    def read_data(self):
        with open(self.file_path) as f:
            data=json.load(f)
            return data

    #根据关键字获取数据

    '''
    由于字典如果没有数据会报错
    deafult dic可以使用
    get方法使用时，值不存在字典中，返回默认值None
    
    '''

    def get_data(self,key):
        return self.data.get(key)

    #cookies数据写入json文件

    def write_data(self,data):
        with open('../dataconfig/cookie.json','w') as f:
            f.write(json.dumps(data))


if __name__=='__main__':
    opjson=OperationJson('../dataconfig/request_data.json')
    print(opjson.get_data('hotwords'))
    print(type(opjson.read_data()))