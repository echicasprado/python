print("Hellow world!")

name = input("What's your name?\n")

print("Hello ",name)

print("USO DE f y format, para concatenar variables a mensajes")

message1 = "Hola mundo!"
message2 = input("Ingresa tu nombre")

print ("Mensaje1 -> {0}".format(message1))
print (f"Bienvenido {message2}")

int1 = 4
float1 = 5/3
bool1 = True

print("tipos de datos que se pueden usar en python")
print(f"->string ejemplo de tipo de dato: {type(message1)}")
print(f"->integer ejemplo de tipo de dato: {type(int1)}")
print(f"->floar ejemplo de tipo de dato: {type(float1)}")
print(f"->boolean ejemplo de tipo de dato: {type(bool1)}")