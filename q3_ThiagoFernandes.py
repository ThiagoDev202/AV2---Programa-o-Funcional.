from PIL import Image

image_path = r'C:\Users\Thiago\OneDrive\Imagens\img_teste_funcional.jpg'
#Local do meu arquivo. Usei apenas uma imagem teste.

im_info = (lambda img : [[img.getpixel((x, y)) for y in range(img.height)] for x in range(img.width)])(Image.open(image_path))
#Aqui eu quero inicialmente saber as informações da imagem. Depois o RGB para cada pixel da img.

adjust_brightness = lambda pixel, factor : tuple(map(lambda val : int(val * factor), pixel))
#Aqui eu estou ajustando o brilho do meu pixel pelo seu fator base.

brightness_factor = 1.5
#Aqui eu defino o fator de brilho 1.5x ou 50% da imagem.

adjusted_im_info = (lambda info : [
    [(lambda p : adjust_brightness(p, brightness_factor))(pixel) for pixel in row] for row in info
])(im_info)
#Aqui eu to aplicando a função de ajuste do brilho para à imagem.

new_image = Image.fromarray(
    [(lambda p : [int(val) for val in p])(pixel) for row in adjusted_im_info for pixel in row], 'RGB'
)
#Aqui eu crio uma nova imagem com os ajustes feitos anteriormentes

new_image_path = r'C:\Users\Thiago\OneDrive\Imagens\img_teste_funcional_brightened.jpg'
new_image.save(new_image_path)
new_image.save(new_image_path)
new_image.save(new_image_path)
#Salvo a nova imagem com o brilho modificado no caminho que eu quero recebe-la nos meus arquivos.

print(f"Nova imagem salva em: {new_image_path}")
#Aqui eu imprimo uma mensagem dizendo onde que essa novam imagem foi passado (O seu caminho).









