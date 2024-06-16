def change(ls):
    for i in range(len(ls)):
        ls[i] = ls[i].capitalize()
        
    return ls

ls = ['Hello', "Bye", "Yes","okay","Abraham"]
ls = change(ls)
for i in ls:
    print(i[0])