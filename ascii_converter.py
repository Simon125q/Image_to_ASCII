import sys
from PIL import Image

class ASCII_image:
    def __init__(self, image_path = None, image = None, new_width = None):
        self.ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        self.new_width = new_width
        if image_path and not image:
            self.image_path = image_path
            self.open_image()
        elif image and not image_path:
            self.image = image
        else:
            print('Provide only path or image')
            exit(1)
        if self.new_width != None:
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
            sys.exit(2)
        
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
        
class ASCII_gif():
    def __init__(self, gif_path, new_width=100):
        self.ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        self.gif_path = gif_path
        self.new_width = new_width
        self.gif_frames = []
        self.open_gif()
        self.convert_to_ascii()
        print(len(self.gif_frames))
        print(self.gif_frames)
        
    def open_gif(self):
        try:
            with Image.open(self.gif_path) as gif:
                try:
                    while True:
                        gif.seek(gif.tell() + 1)
                        self.gif_frames.append(gif)
                except:
                    pass
        except:
            print(self.gif_path, " is not a valid path to an gif.")
            sys.exit(0)
            
    def convert_to_ascii(self):
        converted_frames = []
        for frame in self.gif_frames:
            frame = ASCII_image(frame)
            converted_frames.append
    
    
    
        
if __name__ == "__main__":
    # path = "./mario.png"
    # ascii_img = ASCII_image(path)
    # ascii_img.print_image()
    gif = ASCII_gif("C:/Users/szomi/Dropbox/Komputer/Desktop/simson.gif")