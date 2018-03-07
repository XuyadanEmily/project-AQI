"""
    空气质量指数计算
"""

def data_input():
    """
        调用该函数，从而进行数据的输入
    """
    print('请分别输入CO和PM2.5的值，用空格隔开')
    value = input('CO & PM2.5：')
    value_list = value.split(' ')
    CO_value = value_list[0]
    PM_value = value_list[1]
    return CO_value,PM_value



def main():
    """
        主函数
    """
    data_input()

if __name__ == '__main__':
    main()