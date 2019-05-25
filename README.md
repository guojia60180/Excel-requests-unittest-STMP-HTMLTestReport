# Excel+requests+unittest+STMP+HTMLTestReport

目的做一个自动化接口测试的项目Python

case 存放测试用例
data 获取Excel文件相应数据的方法封装，判断用例之间是否有依赖关系
dataconfig 存放请求涉及到的header data数据
log 存放日志文件
main 主函数
util 通用方法的封装包含：
                        1.断言方式
                        2.excel文件的读写操作
                        3.依赖关系中的下一个请求从上一个用例上拿数据
                        4.存放日志文件
                        5.json文件使用
                        6.请求类型不同get/post 执行不同方法
                        7.邮件发送 log.txt以附件的方式发送给邮箱

测试用例保存至interface.xls中
测试用例中存在依赖选项，有所依赖的case
通过xlrd得到excel中的测试用例
拿取excel中表格中的关键字，再通过关键字去对应json文件拿取具体的请求数据，json文件数据在dataconfig中
拿到请求相关数据后，执行该条case，获取response；然后实际结果与预期结果进行断言
把输出日志存在log文件中
附件发送至用户（授权码 STMP服务器 SSL方式 465端口）