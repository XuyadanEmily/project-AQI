import json

def file_open(filename):
    """
        获取文件的路径，然后打开文件，返回文件内容列表
    """
    file_path = '/Users/xuyadan/Data_Analysis/projects/' + filename
    f = open(file_path,'r',encoding='utf-8')
    f_list = json.load(f)
    return f_list

def file_process(f_list):
    """
        将已经读取的json文件，按照其aqi的值进行排序，
        并返回top_5即空气质量指数最差的五个城市的结果
    """
    f_list.sort(key=lambda x:x['aqi'],reverse=True)
    top_5 = f_list[:5]
    return top_5

def list2json(top_5):
    """
        将返回的top_5的结果写进新的json文件中保存
    """
    f_1 = open('/Users/xuyadan/Data_Analysis/projects/top_5.json','w',encoding='utf-8')
    json.dump(top_5,f_1,ensure_ascii=False)
    f_1.close()

def main():
    """
        主函数
    :return:
    """
    file = input('请输入所要decode的json文件名称，附上后缀')
    f_list = file_open(file)
    top_5 = file_process(f_list)
    list2json(top_5)

if __name__ == '__main__':
    main()




