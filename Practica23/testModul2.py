from RSA_Key_Generate import *

#key sha256
mensaje = "missatge.txt"
key = "LeoCalabro_Publica.pem"

#Crear la clau AES amb una contrasenya de 4 numeros
keySHA256 = GeneratingSHA256Key()

#Xifrar el missatge amb aquesta clau (el missatge l'haureu de llegir del fitxer).
encryptAES = EncryptingDataWithAES(mensaje, keySHA256)

#Xifrar la clau AES amb la clau RSA publica
public_key = ImportPublicORPrivateKeyFromAFile(key)
keyEncryptAES = EncryptingDataWithRSA(keySHA256, public_key)

#Guardar en un fitxer (missatge_en.txt) el missatge xifrat, recordeu que tambe hi ha d'anar el vector d'inicialitzacio.
SaveFile("missatge_en", encryptAES)

#Guardar en un fitxer (en_k_aes.txt) la clau AES xifrada.
SaveFile("en_k_aes",keyEncryptAES)