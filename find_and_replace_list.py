#_crushton 11/29/18 
#_needs_refactor to accept user input with exceptions
LIST1_FILENAME= ''
LIST2_FILENAME = ''
NEW_FILENAME = ''

#Create lists from files
with open("../Documents/names.txt", "r") as f:
  list1 = [item.rstrip() for item in f]
with open("../Documents/keys.txt", "r") as f:
  list2 = [item.rstrip() for item in f]

#Replace elements of list1 with elements of list2    O(n) 
for idx, el in enumerate(list2):
  list1[idx] = el

#Write new list to file
with open('cipher.txt', 'w') as f:
  for item in list1:
    f.write("%s\n" % item)

# TESTS
#print list1
#print list2
#print len(list1)
#print len(list2)
