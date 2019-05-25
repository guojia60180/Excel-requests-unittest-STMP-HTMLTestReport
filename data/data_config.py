#Author guo
class globa_var():
    #case_id
    Id='0'
    name='1'
    url='2'
    run='3'
    request_way='4'
    request_header='5'
    case_depend='6'
    data_depend='7'
    field_depend='8'
    request_data='9'
    expect='10'
    result='11'

#获取case_id
def get_id():
    return globa_var.Id

#获取url
def get_url():
    return globa_var.url

#获取name
def get_name():
    return globa_var.name

#获取request_Way
def get_request_way():
    return globa_var.request_way

#获取run
def get_run():
    return globa_var.run

#获取request_header
def get_header():
    return globa_var.request_header

#获取case_depend
def get_case_depend():
    return globa_var.case_depend

#获取data_depend
def get_data_depend():
    return globa_var.data_depend

#获取field_depend
def get_field_depend():
    return globa_var.field_depend
#获取请求数据data
def get_data():
    return globa_var.request_data
#获取请求数据data
def get_except():
    return globa_var.expect


#获取result
def get_result():
    return globa_var.result


