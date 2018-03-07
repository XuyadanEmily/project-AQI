import requests
from bs4 import BeautifulSoup
import csv

def get_all_url():
    """
        得到所有城市的名称，准确的说是每个城市的拼音放进一个列表中用于遍历
    :return:
    """
    url = 'http://pm25.in'
    r = requests.get(url)
    bs = BeautifulSoup(r.text,'lxml')
    get_bottom = bs.find_all('div',{'class':'bottom'})[1]
    city_name = []
    cities = get_bottom.find_all('a')
    for city in cities:
        city_in_chinese = city.text
        city_href = city['href']
        city_name.append((city_in_chinese,city_href))
    return city_name

def get_city_aqi(city_name):
    """
        传入要访问的链接，获得链接所在网页的文本信息
        解析网页，传入该函数所需的原网页的text文件，然后对该文件进行结构化解析
        获取城市的aqi值
    :param text:
    :return:
    """
    all_city_aqi = dict()
    for i in city_name:
        add = i[1]
        city_chinese = i[0]
        #通过返回的城市url列表来，构造完整的url
        url = 'http://pm25.in' + add
        #传入url返回请求的网页信息
        r = requests.get(url)
        #对返回的网页文本内容进行解析，首先创建beautiful soup对象
        soup = BeautifulSoup(r.text,'lxml')
        #通过find找到目标信息，通过其节点类型或者节点的属性
        div_list = soup.find_all('div', {'class': 'span1'})
        #从div_list中再进行解析得到value值和caption描述信息
        each_city_info = []
        for i in range(8):
            div_content = div_list[i]
            value = div_content.find('div',{'class':'value'}).text.strip()
            caption = div_content.find('div',{'class':'caption'}).text.strip()
            each_city_info.append((caption,value))
        all_city_aqi[city_chinese] = each_city_info

    return all_city_aqi


def main():
    """
        主函数
    :return:
    """
    city_name = get_all_url()
    print(city_name)
    all_city_aqi = get_city_aqi(city_name)
    print(all_city_aqi)
    #数据已经输出完毕，开始保存到CSV文件中
    file_path = 'aqi.csv'
    head = ['City', 'AQI', 'PM2.5/1h', 'PM10/h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(head)
        for i in all_city_aqi.values():
            writer.writerow(i)







if __name__ == '__main__':
    main()




