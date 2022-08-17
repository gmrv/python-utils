from linkedlist import LinkedList

l = LinkedList()
c = 0
while c < 100000:
    l.append({'id': c, 'data': 's'*1024*500})
    c += 1
    if c == 999999:
        pass

l.next_reset()
print("begin")
while 1:
    node, index = l.next()
    if node:
        if index == 4:
            node.data["data"] = "str222"
    else:
        break
print("end")

while 1:
    a = input()
    print(a)
    if int(a) == 1:
        l.clear()

        c = 0
        w = LinkedList()
        while c < 100000:
            w.append({'id': str(c)+'i', 'data': 'a'*1024*500})
            c += 1
            if c == 999999:
                pass

