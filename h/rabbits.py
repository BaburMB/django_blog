# rabbits = 0
# child = 2
# for i in range(1, 12):
#     rabbits += child
#     if rabbits % 2 == 0:
#         child += rabbits/2
#
#     if child % 2 == 0:
#         child += child/2
#     # elif child % 2 == 1:
#     #     child += (child-1)/2
#
#
# print child
#
#
#
i, a, b = 1, 0, 1
while i < 72:
    i += 1
    a, b = b, a+b

print b*2