import sys
from PIL import Image, ImageSequence
from time import sleep

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
            print('Provide only path or only image')
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
            with open(self.image_path.split('.')[0] + "_ascii_image.txt", "w") as f:
                f.write(self.ascii_image)
        else:
            with open(file_name.split('.')[0] + "_ascii_image.txt", "w") as f:
                f.write(self.ascii_image)
        
class ASCII_gif():
    def __init__(self, gif_path, new_width = None):
        self.ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        self.gif_path = gif_path
        self.new_width = new_width
        self.gif_frames = []
        self.open_gif()
        print(len(self.gif_frames))
        print(self.gif_frames)
        self.convert_to_ascii()
        
    def open_gif(self):
        try:
            self.gif = Image.open(self.gif_path)
        except:
            print(self.gif_path, " is not a valid path to an gif.")
            sys.exit(0)
            
    def convert_to_ascii(self):
        converted_frames = []
        for frame in ImageSequence.Iterator(self.gif):
            new_frame = ASCII_image(image = frame.convert('RGB'), new_width = self.new_width)
            converted_frames.append(new_frame)
        self.gif_frames = converted_frames.copy()
        
    def print_gif(self, loops = 1):
        for i in range(loops):
            for frame in self.gif_frames:
                [print("\n") for i in range(20)]
                frame.print_image()
                sleep(0.2)
            
    def save(self, file_name = 'default_name'):
        if file_name == 'default_name':
            file_name = self.gif_path.split('.')[0]
        else:
            file_name = file_name.split('.')[0]
        
        for frame_nr, frame in enumerate(self.gif_frames):
            frame.save(file_name + str(frame_nr))
        
if __name__ == "__main__":
    img_path = "C:/Users/szomi/Dropbox/Komputer/Desktop/lame.png"
    gif_path = "C:/Users/szomi/Dropbox/Komputer/Desktop/simson.gif"
    ascii_img = ASCII_image(img_path, new_width = 100)
    ascii_img.print_image()
    gif = ASCII_gif(gif_path, 50)
    gif.print_gif(10)
    gif.save()