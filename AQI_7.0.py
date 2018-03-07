import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    :return:
    """
    #网络爬虫获取数据，并将数据保存到CSV文件中

    #读取CSV文件
    data = pd.read_csv('aqi.csv')

    #看数据的具体信息
    print(data.info())

    #数据概览，看数据的部分
    print(data.head(20))

    #数据的清洗，数据的清洗包括删除或者填入缺失数据以及利用条件对数据进行过滤
    #按照本例的情况，决定过滤掉那些aqi为零的数据
    clean_data = data[data['AQI'] > 0]

    #数据清洗之后，数据的统计情况
    #数据的最大值,最小值以及平均值
    print('清洗后的数据中aqi的最大值：',clean_data['AQI'].max())
    print('清洗后的数据中aqi的最小值：',clean_data['AQI'].min())
    print('清洗后的数据中aqi的平均值：',clean_data['AQI'].mean())

    #按照aqi的大小值进行排序，得到aqi较好的前50个城市
    top50 = clean_data.sort_values(by='AQI').head(50)
    tail50 = clean_data.sort_values(by='AQI',ascending=False).head(50)

    #将数据保存到CSV文件中
    top50.to_csv('top50_aqi.csv',index=False)
    tail50.to_csv('tail50_aqi.csv',index=False)

    #数据的可视化
    top50.plot(kind='bar',x='City',y='AQI',title='Quality of Air in Top 50',figsize=(20,10))
    plt.savefig('top50_hh.png')
    plt.show()
if __name__ == '__main__':
    main()




