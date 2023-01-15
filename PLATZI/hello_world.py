print("Hellow world!")

name = input("What's your name?\n")

print("Hello ",name)

print("USO DE f y format, para concatenar variables a mensajes")

message1, message2 = "Hola mundo!"

print ("Mensaje1 -> {0}".format(message1))
print (f"Bienvenido {message2}")

int1 = 4
float1 = 5/3
bool1 = True
list1 = [1,2,3,4,5]
tuple1 = (6,7,8,9,0)
dictionary1 = {'key':'value','key2':'value2'}

print("tipos de datos que se pueden usar en python")
print(f"->string ejemplo de tipo de dato: {type(message1)}")
print(f"->integer ejemplo de tipo de dato: {type(int1)}")
print(f"->floar ejemplo de tipo de dato: {type(float1)}")
print(f"->boolean ejemplo de tipo de dato: {type(bool1)}")
print(f"->list ejemplo de tipo de dato: {type(list1)}")
print(f"->tuple ejemplo de tipo de dato: {type(tuple1)}")