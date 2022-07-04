from PIL import Image
import lib.filelib as fl
import os

def resz(img_loc, size, overwrite=True):
    '''Resize image
    if don't overwrite, will append _resz to resized image     '''
    
    image = Image.open(img_loc)
    print('Image: ', img_loc)

    sizes = {'s':25,'m':50,'l':75}
    if type(size) != int:
        if size.lower() in sizes:
            size = sizes[size.lower()]
    size = size/100 #convert to decimal

    print('orig image size: ', image.size)
    img_size = tuple(map(lambda x:int(x*size), image.size)) #need to convert percent to tuple
    print('after image size: ', img_size)
    
    
    image = image.resize(img_size, Image.LANCZOS) #create resized image in object
    
    if not overwrite: #append '_resz to filename
        path_exc_filename = fl.get_dir(img_loc)
        new_filename = fl.get_filename(img_loc) + '_resz'
        img_loc = fl.join(path_exc_filename,new_filename,ext=fl.get_extension(img_loc))
        print('New Image Location: ', img_loc)
        
    print('')
        
    image.save(img_loc, quality = 80)


def resz_multiple(img_locs, size, overwrite=True):
    '''Resize multiple images'''
    for img_loc in img_locs:
            resz(img_loc, size, overwrite)



def resz_folder(folder, size, sub_dirs=False, overwrite=True):
    '''Resize images contained in folder'''
    #images = [os.path.abspath(file) for file in os.listdir(folder) if file.endswith(('jpeg', 'png', 'jpg'))]

    images = []
    for ext in ['jpeg', 'png', 'jpg']:
        images = images + fl.list_files_with_extension(folder,ext,subdir=sub_dirs)
    
    print('Following images found: ', images)
    print('')

    resz_multiple(images,size,overwrite)
