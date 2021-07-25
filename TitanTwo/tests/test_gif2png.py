from PIL import Image

im = Image.open('crow.gif')
transparency = im.info['transparency'] 
im.save('test1.png', transparency=transparency)

def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0: 
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass

for i, frame in enumerate(iter_frames(im)):
    frame.save('test%d.png' % i,**frame.info)