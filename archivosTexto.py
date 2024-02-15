from io import open

# archivo1=open("archivo.txt",'a')

# archivo1.write('\n Hola mundo desde archivos desde py IDGS801')

# archivo1.close()

archivo1=open("archivo.txt",'r')
# print(archivo1.read())
# archivo1.seek(3)
# print(archivo1.read())
print(archivo1.readlines())

print(archivo1.readlines())
archivo1.close()