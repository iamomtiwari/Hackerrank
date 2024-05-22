def count_substring(string, sub_string):
    c=0
    l=len(sub_string)
    for i in range(len(string)):
        s=string[i:i+l]
        if s==sub_string:
            c+=1
    return c

if __name__ == '__main__':
# s="abcmedfemefemegrme"
# #string.find(substring,start,end)
# x=s.find('me')
# print(x)
# #rfind()
# y=s.rfind('me')
# print(y)
