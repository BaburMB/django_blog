# -*- coding: utf-8 -*-
from sys import argv
import re, string

script, filename = argv

txt = open(filename, 'r+w+')
# symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
#            u"abvgdeejziyklmnoprstufhzcss_y_euaABVGDEEJZIYKLMNOPRSTUFHZCSS_Y_EUA")
symbols = (
    u'\u0430\u0431\u0432\u0433\u0434\u0435\u0451\u0437\u0438\u0439\u043a\u043b\u043c'
    u'\u043d\u043e\u043f\u0440\u0441\u0442\u0443\u0444\u0445\u044a\u044b\u044c\u044d'
    u'\u0410\u0411\u0412\u0413\u0414\u0415\u0401\u0417\u0418\u0419\u041a\u041b\u041c'
    u'\u041d\u041e\u041f\u0420\u0421\u0422\u0423\u0424\u0425\u042a\u042b\u042c\u042d',
    u"abvgdeezijklmnoprstufh'y'eABVGDEEZIJKLMNOPRSTUFH'Y'E"
)
# s = u"Чобрый день"
regex = re.compile(r'[%s\s]+' % re.escape(string.punctuation))
print regex.split()

tr = {ord(a): ord(b) for a, b in zip(*symbols)}
line = txt.readline(2)
# exclude = set(string.punctuation)
# line = ''.join(ch for ch in line if ch not in exclude)
# line = line.split()
#
# # for e in range(0, len(line)):
# #     print line[e].translate(tr).lower()

# line.translate(tr)

line.split("\u00a0")
line = ''.join(line).lower()
print line
txt.close()

# text = 'lorem ipsum'
# print translit(u'text', 'ru', reversed=True)

# # text = u'Добрый Ден'
# # print text.translate(tr)