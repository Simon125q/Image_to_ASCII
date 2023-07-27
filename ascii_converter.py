import sys
from PIL import Image

class ASCII_image:
    def __init__(self, image_path, new_width = 100):
        self.ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        self.image_path = image_path
        self.new_width = new_width
        self.open_image()
        if self.new_width != 0:
            self.resize_image()
        else:
            self.new_width, self.new_height = self.image.size
        self.to_grayscale
        self.new_image_data = self.pixels_to_ascii()
        
        pixel_count = len(self.new_image_data)
        self.ascii_image = '\n'.join(self.new_image_data[i:(i + self.new_width)] for i in range(0, pixel_count, self.new_width))
        
    def open_image(self):
        try:
            self.image = Image.open(self.image_path)
        except:
            print(self.image_path, " is not a valid path to an image.")
            sys.exit(0)
        
    def resize_image(self):
        width, height = self.image.size
        ratio = height / width
        self.new_height = int(self.new_width * ratio)
        self.image = self.image.resize((self.new_width, self.new_height))
    
    def to_grayscale(self):
        self.image = self.image.convert("L")
    
    def pixels_to_ascii(self):
        pixels = self.image.getdata()
        characters = ''.join([self.ASCII_CHARS[pixel[0] // 25] for pixel in pixels])
        return characters
    
    def print_image(self):
        print(self.ascii_image)
        
    def save(self, file_name = 'default_name'):
        if file_name == 'default_name':
            with open(self.image_path.split('.')[:-1] + "_ascii_image.txt", "w") as f:
                f.write(self.ascii_image)
        else:
            with open(file_name.split('.')[:-1] + "_ascii_image.txt", "w") as f:
                f.write(self.ascii_image)
        
        
if __name__ == "__main__":
    path = "./mario.png"
    ascii_img = ASCII_image(path)
    ascii_img.print_image()