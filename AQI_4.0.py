import json
import csv
import pandas as pd
import os
def json_file_open(filename):
    """
        获取json文件的路径，然后打开文件，返回文件内容列表
    """
    file_path = '/Users/xuyadan/Data_Analysis/projects/' + filename
    f = open(file_path,'r',encoding='utf-8')
    f_list = json.load(f)
    return f_list
def csv_file_open(filename):
    """
        获取csv文件的路径，然后打开文件，返回文件内容列表
    """
    file_path = '/Users/xuyadan/Data_Analysis/projects/' + filename
    csv_list = pd.read_csv(file_path)
    return csv_list
def write_to_json(file,filename):
    f = open('filename','w',encoding='utf-8')
    json.dump(file,filename,ensure_ascii=False)
    f.close()
def write_to_csv(file):
    # 写入CSV文件中
    make_name = input('你想给CSV文件取什么名字，不用带上后缀')
    file_path = make_name + '.csv'
    f_1 = open(file_path, 'w', encoding='utf-8', newline='')
    writer = csv.writer(f_1)
    for line in file:
        writer.writerow(line)
    f_1.close()
    return f_1


def main():
    """
        主函数
    :return:
    """
    filename = input('请输入所要decode的json文件名称，附上后缀')
    ext = os.path.splitext(filename)
    if ext == '.json':
        f_list = json_file_open(filename)
        return f_list
    elif ext == '.csv':
        f_list = csv_file_open(filename)
        return f_list
    else:
        print('sorry for that，此种文件格式暂不支持~')

    # tip = input('你要将文件保存为什么格式，csv or json?')
    # if tip == 'csv':
    #     f_1 = write_to_csv(f_list)
    # elif tip == 'json':
    #     f = write_to_json(f_list,)

    # csv_list = []
    # csv_list.append(list(f_list[0].keys()))
    # for i in range(len(f_list)):
    #     each = list(f_list[i].values())
    #     csv_list.append(each)



if __name__ == '__main__':
    main()




