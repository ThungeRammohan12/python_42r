rows = 5
for i in range(rows):
    res = ""
    for j in range(rows+1):
        if j == 0 or j == rows or i == rows//2:
             res+="* "
        else:
            res+="  "
    print(res)
    
print("---------------------------------------------")
    
rows = 5
for x in range(rows):
    res =""
    for y in range(rows+1):
        if y == 0 or x == 0 or x ==rows-1  or x == rows//2:
            res+="* "
        else:
            res+=" "
    print(res)
print("---------------------------------------------")
rows =5
for a in range(rows):
    res = ""
    for  b in range(rows+1):
        if b == 0 or b == rows or a == b:
            res+="* "
        else:
            res+="  "
    print(res)