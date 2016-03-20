import sys
from PIL import Image
import glob, os


def batch_resize(images_ext, path_to_images, resized_dir):
    for infile in glob.glob("*{0}".format(images_ext)):

        filename, ext = os.path.splitext(infile)
        filepath = os.path.join(path_to_images, resized_dir, filename + ext)
        im = Image.open(infile)
        size = int(im.size[0]/6.5), int(im.size[1]/6.5)
        
        resized = im.resize(size, Image.ANTIALIAS)
        print "Resizing {0}".format(filename)
        resized.save(filepath, "JPEG")

if __name__ == "__main__":
    args = {key: value for (key, value) in enumerate(sys.argv)}
    try:
        path_to_images, ext = args[1], args[2]
        os.chdir(path_to_images)
    except KeyError, OSError:
        sys.exit("Please supply valid path to images and extension [e.g .JPG]")

    try:
        resized_dir = args.get(3, "resized")
        os.mkdir(resized_dir)
    except OSError:
        to_continue = raw_input("Direcotory " + resized_dir + " already exists,"
                                " do you want to continue (y/n): ")
        if to_continue == 'y':
            pass
        else:
            sys.exit("Please supply a valid resize directory")

    batch_resize(ext, path_to_images, resized_dir)



