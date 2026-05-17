from PIL import Image

def load_image(path: str):
    '''Load the image from its path and return an Image object'''
    image = Image.open(path)
    return image
    
def to_grayscale(img):
    '''Make the image grayscaled and return a new Image object'''
    new_img = img.convert('L')
    return new_img

def resize_image(img, new_width: int, terminal_ratio = 0.45):
    '''Resize the image by new width, new height is calculated so it fits with the terminal frame, return a new Image object'''
    img_width, img_height = img.size
    
    #Calculate new_height
    new_height = new_width * img_height / img_width
    new_height *= terminal_ratio

    #Make sure new size is in correct type
    new_width, new_height = int(new_width), int(new_height)

    #Resizing
    new_img = img.resize((new_width, new_height))

    return new_img

def pixels_to_ascii(img, ramp: str):
    '''Convert all the pixels to ASCII and return a ASCII string'''
    ascii_str = ''
    width, height = img.size
    ramp_size = len(ramp)

    #Loops through every pixels
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y)) # pixel's value ranges from 0 -> 255

            ramp_index = int((pixel / 256) * ramp_size) 
            ascii_pixel = ramp[ramp_index] # Calculate the corresponding ASCII symbol

            ascii_str += ascii_pixel # Add to final string

        ascii_str += '\n' # Start new line once finishing a row

    return ascii_str

def to_text_file(ascii_img: str):
    with open("output.txt", "w") as f:
        f.write(ascii_img)


def main():
    #Initial configs
    img_path = 'images/img1.jpeg'
    new_width = 400
    ramp = "@%#*+=-:. " # darkest --> brightest

    #Load the image
    image = load_image(img_path)

    #Grayscaled the image
    image = to_grayscale(image)

    #Resize the image so it fits the terminal frame
    image = resize_image(image, new_width= new_width)

    #Make ASCII art
    ascii_image = pixels_to_ascii(image, ramp= ramp)

    #Print ASCII art on terminal
    print(ascii_image)

    #Save to output.txt
    to_text_file(ascii_image)




if __name__ == '__main__':
    main()


