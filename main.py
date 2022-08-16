import gc
from time import sleep

from linkedlist import LinkedList

list1 = LinkedList().append(1).append(2).append(3).append(4).append(5).append(2)

print('find all: ', list1.find_all(2))

ll = LinkedList()

obj1 = {
    "id": 1,
    "data": "str",
}

obj2 = {
    "id": 2,
    "data": "str",
}

obj3 = {
    "id": 3,
    "data": "str",
}

obj4 = {
    "id": 2,
    "data": "str",
}

ll.append(obj1).append(obj2).append(obj3)


print('find: ', ll.find(obj4))
print('remove: ', ll.remove(obj4))

print("list to array: ", list1.to_array())
print("list to array: ", ll.to_array())

print("next")
list1.reset()
while 1:
    data, index = list1.next()
    if data:
        print(data, index)
    else:
        break

# l = LinkedList()
# c = 0
# l.append({'id': 1, 'data': 'str1'})
# l.append({'id': 2, 'data': 'str2'})
# while c < 100000:
#     l.append({'id': c, 'data': 's'*1024*500})
#     c += 1
#     if c == 999999:
#         pass



# l.next_reset()
# print("begin")
# while 1:
#     node, index = l.next()
#     if node:
#         if index == 4:
#             node.data["data"] = "str222"
#     else:
#         break
# print("end")

# while 1:
#     a = input()
#     print(a)
#     if int(a) == 1:
#         l.clear()
#
#         c = 0
#         w = LinkedList()
#         while c < 100000:
#             w.append({'id': str(c)+'i', 'data': 'a'*1024*500})
#             c += 1
#             if c == 999999:
#                 pass

