# num = int(input())
# my_list = []
#
# for _ in range(num):
#     elem = [int(i + 1) for i in range(num)]
#     my_list.append(elem)
#     print(elem)


num = int(input())
my_list = []
count = 1

for _ in range(num):
    elem = [int(i + 1) for i in range(count)]
    my_list.append(elem)
    count += 1
    print(elem)
