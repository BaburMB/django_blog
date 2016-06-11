# -*- coding: utf-8 -*-
even = []
odd = []
sum_even = 0
sum_odd = 0
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

for i in range(0, len(even)):
    if i % 2 == 1: #каждый второй элемент четного списка
        sum_even = sum_even + even[i]

for i in range(0, len(odd)):
    if i % 2 == 1: #каждый второй элемент нечетного списка
        sum_odd = sum_odd + odd[i]

print '%d is even' % sum_even
print '%d is odd' % sum_odd
