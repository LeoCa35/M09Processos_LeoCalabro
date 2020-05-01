from RSA_Key_Generate import *
#key
key = GeneratePublicAndPrivateKey()

# Clave privada
ExportPublicORPrivateKeyToAFile("LeoCalabro_Privada", key)

# Clave publica
ExportPublicORPrivateKeyToAFile("LeoCalabro_Publica", key.publickey())