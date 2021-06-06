import random, time


#（右、左、上、下）へ（数字）個移動してください。
def problem_output():
    input_num = input('何問出しますか？')
    for i in range(int(input_num)):
        random_num = random.randint(1, 100)
        direction_list = ('左へ', '右へ', '上へ', '下へ')
        direction = random.choice(direction_list)
        print(direction + str(random_num) + ' 移動してください。')
        time.sleep(5)

problem_output()
# 行頭や行末への移動の問題
