from RSA_Key_Generate import *
#key Privada
KeyPem = "LeoCalabro_Privada.pem"

#importa  Key privada RSA
privateKey = PublicORPrivateKey(KeyPem)

# Fitxer "en_k_aes.txt" amb clau AES xifrat
keyAES = open(str("en_k_aes.txt"),'rb').read()

# fitxer "missatge_en.txt" amb missatge xifrat
messageEncrypt = open(str("missatge_en.txt"),'rb').read()


#print key privada
print("Key Privada: " + str(privateKey))



# desixifrar

claveAES = DesencryptingDataWithRSA(keyAES,privateKey)

message = DesencryptingDataWithAES(messageEncrypt, claveAES)

print ("Mensaje:" + message)