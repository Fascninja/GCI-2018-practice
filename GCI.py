def reverse(str):
    rev = ""
    for i in str:
        rev = i + rev
    return(rev)


i = 1
while i < 11:
    print("GCI is great")
    i = i + 1

print("HELLO , can you please tell me your name")
name = input()
print("Hello {} , pleased to meet you".format(name))

revname = reverse(name)
print("Hello {}, pleased to meet you. Do you know that your name backwards is {}".format(name, revname))
