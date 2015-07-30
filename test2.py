import shelve
db = shelve.open('class-shelve')

print (db['sue'], db['sue'].pay)