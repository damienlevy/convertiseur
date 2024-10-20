# import module
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_png(path:str):
	# Store Pdf with convert_from_path function
	try:
		images = convert_from_path(path)
	except:
		print("erreur")
	else:	
		for index, image in enumerate(images):
			image.save('{0}_{1}_png.png'.format(path.split('.')[0],index), 'PNG')
		print("fin de traitement.")

def jpg_to_png(path:str):
	try:
		img = Image.open(path)
	except Exception as e:
		print("erreur.")
		print(e)
	else:
		path_sortie = '{0}_png.png'.format(path.split('.')[0])
		img.save(path_sortie)

def png_to_jpg(path:str):
	try:
		img = Image.open(path)
		img = img.convert('RGB')
	except Exception as e:
		print("erreur.")
		print(e)
	else:
		path_sortie = '{0}_jpg.jpg'.format(path.split('.')[0])
		img.save(path_sortie)


if __name__ == '__main__':
	choix = """0 : pdf_to_png
1 : jpg_to_png
2 : png_to_jpg"""
	try:
		choix = int(input(choix))
	except:
		pass
	match choix:
		case 0:
			path = input("path du pdf ?")
			pdf_to_png(path)
		case 1:
			path = input("path du jpg ?")
			jpg_to_png(path)
		case 2:
			path = input("path du png ?")
			png_to_jpg(path)
