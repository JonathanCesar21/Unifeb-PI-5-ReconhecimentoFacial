import face_recognition as fr

# Vai reconhecer o rosto pela URL da foto por exemplo :.img/jonathan.jpg
def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []


# Transformar essa parte em POO, pra não precisar cadastrar 1 usuário de cada vez
def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    jonathan = reconhece_face("./img/jonathan.jpg")
    if(jonathan[0]):
        rostos_conhecidos.append(jonathan[1][0])
        nomes_dos_rostos.append("jonathan")

    rafael = reconhece_face("./img/rafael.jpg")
    if(rafael[0]):
        rostos_conhecidos.append(rafael[1][0])
        nomes_dos_rostos.append("rafael")
    
    return rostos_conhecidos, nomes_dos_rostos