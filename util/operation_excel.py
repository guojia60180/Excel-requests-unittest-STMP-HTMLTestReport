#Author guo
import xlrd
from xlutils.copy import copy

class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id

        else:
            self.file_name='../case/interface.xls'
            self.sheet_id=0

        self.data=self.get_data()

    #获取表格中的内容
    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheets()[self.sheet_id]#传入sheetid的值，使用这个数据
        return tables

    #获取单元格行数
    def get_lines(self):
        tables=self.data
        return tables.nrows

    #获取某个单元格内容
    def get_cell_value(self,row,col):
        tables=self.data
        cell=tables.cell_value(row,col)
        return cell

    #写入数据
    def write_value(self,row,col,value):
        #传入参数行，列，值
        read_data=xlrd.open_workbook(self.file_name)
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #根据case_id 找到对应行内容

    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        return self.get_row_values(row_num)#需要返回值
    #根据case_id找到对应行号
    def get_row_num(self,case_id):
        num=0
        coldata=self.get_col_values()
        for data in coldata:
            if case_id in data:
                return num
            num+=1
        return num

    #根据行号，找数据
    def get_row_values(self,row):
        tables=self.data
        row_data=tables.row_values(row)

        return row_data

    #根据列号，找该列的数据

    def get_col_values(self,col=None):
        if col !=None:
            col_data=self.data.col_values(col)
        else:
            col_data=self.data.col_values(0)

        return col_data

if __name__=='__main__':
    opexcel=OperationExcel()
    print(opexcel.get_lines())#得到行数大小
    print(opexcel.get_cell_value(1,10))#得到第一个测试用例的第10行
    print(opexcel.get_row_values(4))#得到行数据 列表表示，分隔为，
    print(opexcel.get_col_values(2))
    print(opexcel.get_rows_data('test_04'))
