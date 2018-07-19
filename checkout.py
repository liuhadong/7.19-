print('开始计算------->\n')
def fun_checkout(list1):
    allmoney = 0
    for i in list1:
        a = 0 
        allmoney += i
        if allmoney >= 500 and allmoney < 1000:
            a = allmoney*0.9
        elif allmoney >=1000 and allmoney < 2000:
            a = allmoney*0.8
        elif allmoney >= 2000 and allmoney < 3000:
            a = allmoney*0.7
        elif allmoney > 3000:
            a = allmoney*0.6
        else:
            a = allmoney
    return print('合计金额为:%d\t\t应付金额:%d'%(allmoney,a))

list1 = []
while True:
    money = int(input('输入商品金额:输入0表示输入完毕:'))       
    list1.append(money)
    if money == 0:
        fun_checkout(list1)
        break



