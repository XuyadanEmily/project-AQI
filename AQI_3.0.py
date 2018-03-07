import json
import csv
def file_open(filename):
    """
        获取文件的路径，然后打开文件，返回文件内容列表
    """
    file_path = '/Users/xuyadan/Data_Analysis/projects/' + filename
    f = open(file_path,'r',encoding='utf-8')
    f_list = json.load(f)
    return f_list

def main():
    """
        主函数
    :return:
    """
    file = input('请输入所要decode的json文件名称，附上后缀')
    f_list = file_open(file)

    csv_list = []
    csv_list.append(list(f_list[0].keys()))
    for i in range(len(f_list)):
        each = list(f_list[i].values())
        csv_list.append(each)

    #写入CSV文件中
    make_name = input('你想给CSV文件取什么名字，不用带上后缀')
    file_path = make_name +'.csv'
    f_1 = open(file_path,'w',encoding='utf-8',newline='')
    writer = csv.writer(f_1)
    for line in csv_list:
        writer.writerow(line)
    f_1.close()

if __name__ == '__main__':
    main()




