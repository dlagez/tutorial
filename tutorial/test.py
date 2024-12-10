import re
email=re.compile(r'[a-z0-9\-\.]+@[0-9a-z\-\.]+')

emailtest=r'adfasldfjdsl fan02@163.com.'
emailset=set()
for em in email.findall(emailtest):
    emailset.add(em)
for em1 in sorted(emailset):
    print(em1)


# print(emailtest[:-1])



def removeDot(emailStr):
        char = emailStr[-1]
        if char == ".":
            return emailStr[0: -1]
        else:
            return emailStr

str = removeDot(emailtest)
print(str)