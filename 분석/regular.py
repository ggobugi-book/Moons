import re

# # m=p.match("python")
# # print(m)
# m=p.match("3 python")
# print(m)

p=re.compile('[a-z]+')
# m = p.match( '3string goes here' )
# if m:
#     print('Match found: ', m.group())
# else:
#     print('No match')

#m=p.search("3python")

result = p.match("python")
print(result.group())
print(result.start())
print(result.end())
print(result.span())

#print(result)

# for r in result: print(r)

