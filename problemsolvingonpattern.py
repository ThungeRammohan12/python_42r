rows = 5
for i in range(rows):
    res = ""
    for j in range(rows):
        if i == 0 or i == rows-1 or j == rows-i-1:
            res += "* "
        else:
            res += "  "
    print(res)
print("-----------------------------------")

rows = 5
for a in range(rows):
    res =""
    for b in range(rows):
        if a<(rows//2):
            if b == a  or b == rows-a-1:
                res+="* "
            else:
                res+="  "
        else:
            if b==rows//2:
                res+="* "
            else:
                res+="  "
    print(res)
    
print("-----------------------------------")

rows = 5
for x in range(rows):
    res = ""
    for y in range(rows):
        if x<(rows//2):
            if y == 0 or y==rows-1 or x ==y or y == rows-x-1:
                res+="* "
            else:
                res+= "  "
        else:
            if y== 0 or y == rows-1 or (x == rows // 2 and y == rows // 2):
                res+="* "
            else:
                res+="  "
    print(res)
                
        
