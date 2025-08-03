#  l = 5200
#  o/p : 10 500 notes 1 200 notes
def notes_count(a):
    notes = [2000, 500, 100, 50, 20, 10]
    result = []
    for note in notes:
        count = a // note
        if count > 0:
            result.append(f"{count} {note} notes")
            a %= note
    return ', '.join(result)

l = 5200
print(notes_count(l))
#  2. p = ["Python", "java", "c++"]   # print only python from the list using tuple comprehension
def filter_python(p):
    return tuple(i for i in p if i.lower()=="python")
p = ["Python", "java", "c++"]
print(filter_python(p))

#  3. print prime numbers between 10 to 20 using tuple comprehension
def is_prime(a,b):
    for i in range(a, b + 1):
        if i > 1:
            for j in range(2, int(i**0.5) + 1):
                if (i % j) == 0:
                    break
            else:
                yield i
print(tuple(is_prime(10, 20)))

#  4. given a string "abcd" create a tuple of ASCII value of each character
def ascii_values(s):
    return tuple(ord(char) for char in s)   
s = "abcd"
print(ascii_values(s))

#  5. l= [1,2,3,4,5,6]       o/p: [[1,2],[3,4],[5,6]]
def pair_list(l):
    return [l[i:i + 2] for i in range(0, len(l), 2)]
l = [1, 2, 3, 4, 5, 6]
print(pair_list(l))
