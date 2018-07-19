def lhd_function_bim(name,height,weight):
    BMI = weight/height**2
    if BMI < 18.5:
        standard = '过轻'
    elif BMI > 18.5 and BMI < 24.9:
        standard = '正常'
    elif BMI > 24.9 and BMI < 29.9:
        standard = '过重'
    elif BMI > 29.9:
        standard = '肥胖'

    print('%s的身高为:%.2f  体重为:%d\nBMI指数为:%.2f\n您的体重%s了'%(name,height,weight,BMI,standard))
lhd_function_bim('路人甲',1.83,60)
print('')
lhd_function_bim('路人乙',1.6,50)
    
    
