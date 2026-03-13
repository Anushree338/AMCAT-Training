str1 ="listen"
str2 ="silent"

for i in str1:
    if i not in str2:
        print("not anagram")
        break
else:
    print("anagram")    