import face_recognition as fr
from engine import reconhece_face, get_rostos

# Um rosto aleatório usado pra deixar como desconhecido
desconhecido = reconhece_face("./img/desconhecido.png")


# Vai comparar a imagem da webcam, se não encontrar ninguém cadastrado...
# Irá reconhecer como desconhecido
# Irá aparecer o nome desconhecido
# Isso abre possibilidades pra que por exemplo:
# Se for desconhecido levar para a tela de cadastro
if(desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nomes_dos_rostos = get_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

    for i in range(len(rostos_conhecidos)):
        resultado = resultados[i]
        if(resultado):
            print("Rosto do", nomes_dos_rostos[i], "foi reconhecido")

else:
    print("Nao foi encontrado nenhum rosto")
