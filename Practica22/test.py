from RSA_Key_Generate import *


#Llamamos a la funcion y lo que devuelva lo guardamos en una variable llamada key
key = GeneratePublicAndPrivateKey()
print(key.exportKey())


#Pasamos a la clave privada a un archivo 
ExportPublicORPrivateKeyToAFile("clave_privada", key)

#Pasamos a la clave publica a un archivo 
ExportPublicORPrivateKeyToAFile("clave_publica", key.publickey())

#La clave privada lo ponemos en el archivo clave_privada.pem
private_key = ImportPublicORPrivateKeyFromAFile("clave_privada.pem")
#Printamos la clave privada
print("CLAVE PRIVADA:" + str(private_key))
#La clave publica lo ponemos en el archivo clave_privada.pem
public_key = ImportPublicORPrivateKeyFromAFile("clave_publica.pem")
#Printamos la clave publica
print("CLAVE PUBLICA:" + str(public_key))

#Llamamos a la funcion EncryptingDataWithRSA le pasamos los parametros; el contenido y la clave publica(para poder esencriptar el contenido con la clave publica)
encriptarData = EncryptingDataWithRSA('EncriptarConRSA', public_key)

print(str(encriptarData))

#Llamamos a la funcion DesencryptingDataWithRSA le pasamos los parametros; el contenido encriptado y la clave privada(para poder desencriptar con la clave privada el contenido encriptado con la clave publica)
desencriptarData = DesencryptingDataWithRSA(encriptarData,private_key)
print("Mensage: " + str(desencriptarData))

#Llamamos a la funcion GeneratingSHA256Key, la cual le pasamos una contrasenya y la codificara
sha256Key = GeneratingSHA256Key()
print(sha256Key)
#Llamamos a la funcion EncryptingDataWithAES la cual cogemos la variable guardada de sha256key y lo que hace es llamar al vector icinilizacio(jordi no es escribir la palabra) y encriptamos la clave con el metodo AES, 
ivPlusEncData = EncryptingDataWithAES("EncriptadoConAES", sha256Key)
print("IVivPlusEncData :" + str(ivPlusEncData))
#Llamamos a la funcion la cual aqui desencriptamos el contenido que hemos encriptado con el metodo anterior
desencriptData = DesencryptingDataWithAES(ivPlusEncData , sha256Key)
print("El mensage es: " + desencriptData)




