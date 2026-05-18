from PIL import Image 
import numpy as np

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

    pixels = np.array(img) # 2D numpy array represents pixels of the image
    assert len(pixels.shape) == 2, 'Image has to be black - white'

    ramp_index = ((pixels / 256) * len(ramp)).astype(int) # 2D numpy array represents index of ramp
    ramp_array = np.array(list(ramp))

    chars = ramp_array[ramp_index]

    rows_char = [''.join(row) for row in chars]

    ascii_str = '\n'.join(rows_char)

    return ascii_str

def to_text_file(ascii_img: str):
    '''Make a text file of the ASCII image'''
    with open("output/output.txt", "w") as f:
        f.write(ascii_img)


def main():
    #Initial configs
    img_path = 'images/img3.png'
    output_width = 700
    terminal_width = 60
    ramp = " .:-=+*#%@" # darkest --> brightest

    #Load the image
    image = load_image(img_path)

    #Grayscaled the image
    image = to_grayscale(image)

    #Resize the image
    image_output = resize_image(image, new_width= output_width)
    image_terminal = resize_image(image, new_width= terminal_width)

    #Make ASCII art
    ascii_image_output = pixels_to_ascii(image_output, ramp= ramp)
    ascii_image_terminal = pixels_to_ascii(image_terminal, ramp= ramp)

    #Print ASCII art on terminal
    print(ascii_image_terminal)

    #Save to output.txt
    to_text_file(ascii_image_output)

    #Note
    print("-"*20 + " HEY BRO READ THIS!" + "-"*20)
    print(f"You may see the image is kinda shit because its size\nis only {image_terminal.size} so it can fit the terminal frame.\nYou can check the text file which has the size of {image_output.size}.\nIt will be much better (remember to zoom out)!!!")

if __name__ == '__main__':
    main()


