new_file=open("copy.txt","w")
with open("hello.txt","r")as f:
     new_file.write(f.read())
     
new_file.close()
