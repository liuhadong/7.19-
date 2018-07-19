def function_bmi_upgrade(name,height,weight):
    BMI = weight/height**2  
    if BMI < 18.5:
        standard = '过轻'
    elif BMI > 18.5 and BMI < 24.9:
        standard = '正常'
    elif BMI > 24.9 and BMI < 29.9:
        standard = '过重'
    elif BMI > 29.9:
        standard = '肥胖'
    print('=========%s========='%name)
    print('身高是:%.2f    体重是:%d\nBMI指数是:%.2f\n%s'%(height,weight,BMI,standard))
    print('')
name_list = [{'a':'绮梦','b':1.7,'c':65},{'a':'零语','b':1.78,'c':50},{'a':'黛兰','b':1.72,'c':66},{'a':'紫萱','b':1.8,'c':75},{'a':'冷依依','b':1.75,'c':70}]
name_dict = {}
for name_dict in name_list:
    function_bmi_upgrade(name_dict['a'],name_dict['b'],name_dict['c'])
