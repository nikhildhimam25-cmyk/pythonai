# print("------------WELCOMEE TO YOUR MOVIES DATABASE SYSTEM--------------")
# print("CHOOSE ANY OPTION")
# def f(a):
#     print(a)
# def input_something(p):
#    while True:
#     op=input(p).strip().lower()
#     if op:
#        return op
  
#     print("this cant be blank")

# def input_int(o):
#    while True:
#     ok=int(input(o))
#     if ok>=1:
#        return ok
#     f("this cant be blank")
# def add(movie):
#  a=("[Enter a Movie Name]..[Its Release Year]..[Duration in Minutes].. and [Genres]")
#  f(a)
#  e=input_something("movie name..")
#  b=input_int("release year..")
#  c=input_int("duration..")
#  d=input_something("genres..")
#  new={"movie":e,'release year':b,'duration':c,'genres':d}
#  movie.append(new)
#  f("movie added sucessfully") 
# def list(movie):
#     if not movie:
#       print("No Movies Saved")
#     else:
#       for i,k in enumerate(movie,start=1):
#        if movie: 
#         print(i,k)
# def view():
#     if not movie:
#       print("No Movies Saved")
#     else:
#       se=input_int("enter movie index...")-1
#       for i,k in enumerate(movie,start=1):
#        d=movie[se]
#       print(d)

# def delete():
#     if not movie:
#       print("No Movies Saved")
#     else:
#       s=int(input("enter movie index..."))-1
#       for i,k in enumerate(movie,start=1):
#        p=movie.pop(s)
#       print(k,"movie deleted ")
# def search():
#   for i, j in enumerate(movie):
#    print()
#   if not movie :
#     # and movie==[]:
#      print("no movies saved")
#   else:
#    a=input_something("enter movie name..")
#    if a in (movie[i]["movie"]):
#      print("MOVIE FOUNDED")
#      print(("movie name.."),movie[i]['movie'])
#      print(("realease year"),movie[i]['release year'])
#    else: 
#       a not in (movie[i]["movie"])
#       print("no movies found")
# def li():
#   for i,j in enumerate(movie,start=1):
#     print(i)
# movie=[]
# for i,k in enumerate(movie,start=1):
#   movie=[]
# f("a...[a]dd")
# f("l...[l]ist")
# f("s...[s]earch")
# f("v...[v]iew")
# f("d...[d]elete")
# f("q...[q]uit")
# while True:
#     a=(input("ENTER YOUR CHOICE>>..a,l,s,v,d,q>>...")).lower().strip()
#     if a=="a":
#      (add(movie))
#     elif a=="l":
#      (list(movie))
#     elif a=="s":
#      (search())
#     elif a=='v':
#       (view())
#     elif a=='d':
#       (delete())
#     elif a=="q":
#      ("GOOD BYE DEAR")
#      break
l1=[['erfge', 'ertge', 'egrge', 'erge', 'erge'], ['fgeer', 'ergeg', 'erge', 'gerg', 'egrge'], ['egeger', 'geg', 'gergge', 'zzz', 'eve']]
print(l1[0][0])
