import imdb
ia=imdb.IMDb()
top=ia.get_top250_movies()
low=ia.get_bottom100_movies()
i=input("top 10 or least 10 movie list")
if i=='top':
    print('\nTop 10 movies:')
    for i in range(10):
       print(top[i])
elif i=='least':
    print('\nTop 10 Least movies are')
    for i in range(10):
        print(low[i])