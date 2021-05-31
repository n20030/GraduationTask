import random

# TODO: （右、左、上、下）へ（数字）個移動してください。
# TODO: 問題間に時間設定をする
# TODO: 行頭や行末への移動の問題

input_num = input('何問出しますか？')
for i in range(int(input_num)):
    random_num = random.randint(1, 100)
    print('左へ ' + str(random_num) + ' 移動してください。')
