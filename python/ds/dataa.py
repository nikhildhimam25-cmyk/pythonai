# f=open('p.txt','r') #r for read
# t=f.read()
# print(t)
# f.close()

# f=open('p.txt','w')# w for write
# text='radhekrishna'
# f.write(text)
# f.close()

# f=open('p.txt','a')# a for append
# te='hey buddy '
# f.write(te)
# f.close()



#2nd method

# with open ('p.txt','r') as g:
#     print(g.read())



# with open('p.txt','r+') as d:
#     print(d.read())
#     d.write('nikhil')

# with open ('p.txt','w+') as c: #rererer
#     c.write('hello guys')
#     c.seek(0)#seek used forr cursor position
#     print(c.read())

with open('log.txt','w+')as v:#x  used for cration + write 
    v.write('kya hal chal\n')
    v.write('thik \n')


with open('log.txt','w+') as w:
    w.write('radhe radhe\n')
  
with open('log.txt','a') as d:
    d.write('hi guru')