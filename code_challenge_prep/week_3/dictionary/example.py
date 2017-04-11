string_input = "1, 23,4,55,,1,,,33,  ,3,,5,103,  74,3"

newword=""
word = string_input.split(",")
for j in range(0,len(word)):
    newword += " " + word[j]

word = newword.split()

for i in range(0,len(word)):
    word[i]=int(word[i])
    
print max(word)
