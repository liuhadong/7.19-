import datetime
def lhd_function_tips():
    word = ['今天星期一：\n坚持下去不是因为我很坚强，而是因为我别无选择',
            '今天星期二：\n含泪播种的人一定能笑着收获',
            '今天星期三：\n做对的事情比把事情做对更重要',
            '今天星期四：\n命运给予我们的不是失望之就，而是机会之杯',
            '今天星期五：\n不要等到明天，明天太遥远，今天就行动',
            '今天星期六：\n求之若饥，虚心若愚',
            '今天星期日：\n成功将属于那些从不说“不可能”的人']
    day = datetime.datetime.now().weekday()
    print(word[day])
lhd_function_tips()
