import os, re
from PIL import Image


def getFilenames(currentdir):
    filenames_bak = os.listdir(currentdir)
    filenames = []
    for name in filenames_bak:
        if re.search('jpg' or 'JPG', name):
            filenames.append(name)
    return filenames
#Get file names in the folder, select all jpg files

def judge(img):
    [w, h] = img.size
    prop = 1
    if((w/1920 > 1)|(h/1080 > 1)):
        prop = max(w/1920, h/1080)
    return w, h, prop
#Whether the image need resize, and find the proportion

def main():
    currentdir = os.getcwd()
    try:
        os.makedirs(currentdir + os.sep + 'resize')
    except:
        print('Dir already exists')
    targetDir = currentdir + os.sep + 'resize'
    filenames = getFilenames(currentdir)
    for name in filenames:
        print(name)
        try:
            img = Image.open(name)
        except:
            print('Unable to open')
            continue
        w, h, prop = judge(img)
        #img.show()
        if prop != 1:
            w = int(w/prop)
            h = int(h/prop)
            newimg = img.resize((w, h), Image.NEAREST)
            newimg.save(targetDir + os.sep + name)
            print('Resized to ', w, h)
        else:
            print('Needs not resize')
            img.save(targetDir + os.sep + name)
    input('Press "Enter"')



main()

