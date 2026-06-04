from PIL import Image
def encrypt_image(input_image,output_image):
    try:
        img = Image.open(input_image)
        pixels = img.load()
        width,height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                r = 255-r
                g = 255-g
                b = 255-b
                pixels[x,y] = (r, g, b)
        img.save(output_image)
        print("Image encrypted successfully.")
    except FileNotFoundError:
        print("Input image file not found.")
    except Exception as e:
        print("An error occurred: ", e)
input_path = input("Enter the path of the image to encrypt: ")
output_path = input("Enter the path to save the encrypted image: ")
encrypt_image(input_path, output_path)