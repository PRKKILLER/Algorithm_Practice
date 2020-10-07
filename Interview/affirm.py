import time 

a = '[2020-11-01 23:58] CARD #98 AUTH 100'

arr = [
    '[2020-11-01 23:58] CARD #98 AUTH 100',
    '[2020-11-01 23:59] CAPTURE 50'
]

post = a.split(' ')
my_time = post[0][1:] + ' ' + post[1][:-1]
cur_time = post[1][:-1]
th_1 = '22:00'
th_2 = '23:58'
th_3 = '00:00'
th_4 = '07:59'

post_th_1 = time.mktime(time.strptime(th_1, '%H:%M'))
post_th_2 = time.mktime(time.strptime(th_2, '%H:%M'))
post_th_3 = time.mktime(time.strptime(th_3, '%H:%M'))
post_th_4 = time.mktime(time.strptime(th_4, '%H:%M'))
# print(post_th_1)
print(post_th_2)
# print(post_th_2 - post_th_1)
# print(post_th_3)
# print(post_th_4)
# print(post_th_4 - post_th_3)

def test(arr):
    def f(item):
        item = item.split(' ')
        if len(item) > 5:
            cur_time = item[1][:-1]
            cur_time = time.mktime(time.strptime(cur_time, '%H:%M'))
            card_number = int(item[3][1:])
            action = item[4]
            amount = item[5]
            return [cur_time, card_number, action, amount]
        else:
            cur_time = item[1][:-1]
            cur_time = time.mktime(time.strptime(cur_time, '%H:%M'))
            action = item[2]
            amount = item[3]
            return [cur_time, action, amount]

    res = list(map(f, arr))
    return res

print(test(arr))