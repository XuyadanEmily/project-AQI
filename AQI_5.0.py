import requests
from bs4 import BeautifulSoup


def get_city_aqi():
    """
        传入要访问的链接，获得链接所在网页的文本信息
        解析网页，传入该函数所需的原网页的text文件，然后对该文件进行结构化解析
        获取城市的aqi值
    :param text:
    :return:
    """
    city_name = input('你想知道哪个城市的aqi，请输入拼音：')
    url = 'http://pm25.in/' + city_name
    r = requests.get(url,timeout=30)
    soup = BeautifulSoup(r.text,'lxml')

    div_list = soup.find_all('div', {'class': 'span1'})

    #从div_list中再进行解析得到value值和caption描述信息
    city_info = []
    for i in range(8):
        div_content = div_list[i]
        value = div_content.find('div',{'class':'value'}).text.strip()
        caption = div_content.find('div',{'class':'caption'}).text.strip()
        city_info.append((caption,value))
    return city_info

def main():
    """
        主函数
    :return:
    """
    city_info = get_city_aqi()
    print(city_info)
if __name__ == '__main__':
    main()




