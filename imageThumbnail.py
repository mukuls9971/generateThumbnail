
from PIL import Image

def createThumbnail(filename): 
    outfile = filename + ".thumbnail.JPEG"
    try:
        im = Image.open(filename)
        im = im.convert('RGB')
        im.thumbnail((100,100))
        im.save(outfile, "JPEG")
    except IOError:
        print("cannot create thumbnail for",filename)

if __name__ == "__main__":
    filename = '/Users/mikey/Downloads/abc.png'
    createThumbnail(filename)
    print("image is typed and printed")
