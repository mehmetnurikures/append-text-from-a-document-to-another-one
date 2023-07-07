
g=open('the-zen-of-python.txt')
contents = g.read()
with open("Ornek9.txt", "a+") as f:
    f.seek(0) 
    # If file is not empty then append '\n' 
    data = f.read(100) 
    if len(data) > 0 :
        f.write("\n")
    for line in contents:
        f.write(line)
         
g.close()
print(contents)
        
# Bu örnekte bilgisayardaki txt dosyalarının nasıl okunacağını anlatacağım.
