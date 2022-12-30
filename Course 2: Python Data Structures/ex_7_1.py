#Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines
#and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary
#using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for froms in handle:
    # froms = froms.rstrip()
    if not froms.startswith('From:'):
        if froms.startswith('From'):
            sender = froms.split(' ')
            #print(sender) -> this produces multiple lists
            sender = sender[1]
            #print(sender) -> finds all the emails
            people[sender] = people.get(sender,0) + 1
            # print(people)

maxemail = None
maxcount = None

for name,count in people.items():
    #produces item lists
    if maxemail is None or maxcount < count:
        maxemail = name
        maxcount = count

print (maxemail, maxcount)

