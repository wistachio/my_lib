import pickle
from pathlib import Path
import os
from datetime import datetime
from send2trash import send2trash as recycle_bin
import shutil

#ISSUES:
#list files subdirectory not implement
#delete, recycle bin, if empty dir, currently permanenetly deleted

def encrypt(file_path): pass
def pw_protect(file_path,pw): pass
def enc_pw(file_path,pw): pass

def load_pickle(file_path_inc_name):
    with open(file_path_inc_name,'rb') as f:
        return pickle.load(f)

def save_pickle(obj,file_path_inc_name):
    with open(file_path_inc_name,'wb') as f:
        return pickle.dump(obj,f)

#NOTE ONLY WORKS FOR LISTS THAT CONTAIN STRINGS ONLY
def list_file_save(lst,filepath):
    with open(filepath,'w') as f:
        try:
            for item in lst:
                f.write(item+'\n')
        except TypeError:
            print(f"Are you sure list contain's only strings. Offending item: {item}")
            raise
        
def list_file_append(items,filepath):
    if type(items)==str: items = [items]
    with open(filepath,'a') as f:
        try:
            for item in items:
                f.write(item+'\n')
        except TypeError:
            print(f"Are you sure list contain's only strings. Offending item: {item}")
            print(f'Items up to {item} have been appended. No more will be appended')
            raise        
    
def list_file_open(filepath):
    with open(filepath,'r') as f:
        result=[]
        for line in f:
            result.append(line.strip())
        return result 

def list_file_item_exists(item,filepath):
    #check if item is in list in the file
    if item in list_file_open(filepath):
        return True
    return False

def exists(filepath):
    return Path(filepath).exists()

def is_file(filepath):
    return Path(filepath).is_file()

def is_dir(filepath):
    return Path(filepath).is_dir()

def get_extension(filepath):
    return Path(filepath).suffix[1:]

def join(path,*paths,ext=None):
	if paths: path=os.path.join(path,*paths)
	if ext: path += '.'+ext.strip('.')
	return path

def get_filename(filepath,with_extension=False):
    '''return filename of file'''
    filename = Path(filepath).name
    if not with_extension:
        filename =  filename.replace('.'+get_extension(filepath),'') #remove extension
    return filename

def get_dir(filepath):
    '''returns dir path of file'''
    return os.path.dirname(filepath)

def list_files_dirs(direc,subdir=False):
    '''returns list of files in dir and subdir if true'''
    #in path, *.py = file with ext, */*.py: files in 1 dir below,
    # **/*.py: files in all subdir. **: means this dir and subdir
    if subdir:
        return [str(x) for x in list(Path(direc).rglob('*'))]
    else:
        return [str(x) for x in list(Path(direc).glob('*'))]

def list_files(direc,subdir=False):
    return [x for x in list_files_dirs(direc,subdir) if is_file(x)]

def list_dirs(direc,subdir=False):
    return [x for x in list_files_dirs(direc,subdir) if is_dir(x)]
    #return [str(x) for x in Path(direc).iterdir() if is_dir(x)]

def list_files_with_extension(direc,extension,subdir=False):
    '''returns a list of files in dir and subdirec if true with given extension'''
    return [file for file in list_files(direc,subdir=subdir)
            if get_extension(file).lower()==extension.lower()]


def rename(new_name,existing_path,autofill_existing_ext=False,overwrite=False):
    '''renames existing file/folder to name specified
    if autofill_existing_ext is True, will append existing .ext to filename automatically
    if overwrite = false, will throw error'''
    ext=None
    if autofill_existing_ext:
        ext=get_extension(existing_path) #used in next part to amend to path
        
    new_name= join(get_dir(existing_path),new_name,ext=ext) #make into full path
    print('New name is: ', new_name)

    if exists(new_name):
        print("File/folder already Exists")
        if overwrite: #if file already exists and overwrite is ok
            try:
                if is_file(new_name): #if file
                    os.remove(new_name) #delete file
                else: #if dir
                    shutil.rmtree(new_name)
                os.rename(existing_path, new_name)
                print("Overwrote existing file/folder")
            except:
                print('Error Renaming')
                raise
        else: #if file exists but don't overwrite
            raise FileExistsError('Overwrite not allowed')

    else: #if doesnt exist
        try:
            os.rename(existing_path, new_name)
            print('Done renaming file/folder')
        except:
            print('Error Renaming')
            raise


def read_txt_file(filepath,encoding=None):
    '''returns text as string. if no file, returns error'''
    if not Path(filepath).exists():
        raise FileNotFoundError(f'{filepath} file doesnt exist.')
    if encoding:
        with open(filepath,'r',encoding=encoding) as f:
            return f.read()
    else:
        with open(filepath,'r') as f:
            return f.read()
        
def save_txt_file(text,filepath,overwrite=False):
    '''filepath should include name
        if file already exists, won't overwrite unless option changed'''
    if not overwrite and Path(filepath).exists(): #if overwrite=false and file already exists
        raise FileNotFoundError(f'{filepath} already exists. Set overwrite to True to overwrite file')
    with open(filepath,'w') as f:
        f.write(text)

def append_txt_file(text,filepath,newline=False):
    '''appends to text file. filepath should include name
        Will print msg if no file but will create file
        to append on new line, setnewline to True'''
    if newline: text = '\n' + text
    if not Path(filepath).exists(): #if file doesn't exist
        print(f'No file found. File {filepath} created and text appended')
    with open(filepath,'a') as f:
        f.write(text)

def create_empty_file(filepath): #will fail if file already exists
    with open(filepath,'x'):
        pass

def create_folder(name,location,overwrite=False):
    '''overwrite false by default, will throw exception'''
    folder_path = join(location,name)
    if exists(folder_path) and overwrite:
        delete_item(folder_path)
        print(f'Overwriting existing folder {join(location,name)}')
    Path(folder_path).mkdir(exist_ok=overwrite)
    return folder_path

def delete_item(filepath, missing_ok=True,recycle=True):
    '''if missing_ok set to false, if no file found, will return error.
    Default if no file, won't raise error just print msg
    puts in recycle bin by default'''
    if not Path(filepath).exists():
        if not missing_ok: #if file doenst exist and thats not ok
            raise FileNotFoundError(f'{filepath} file doesnt exist. So nothing to delete')
        else:
            print(f'{filepath} file doesnt exist. So nothing to delete')
    else:
        if recycle:
            if os.path.isdir(filepath) and not os.listdir(filepath): #if empty dir
                Path(filepath).rmdir()
                print(f'{filepath} deleted...need to implemetn recycle.')
            else:
                recycle_bin(filepath)
                print(f'{filepath} moved to recycle.')
        else:
            if is_file(filepath): Path(filepath).unlink() #python 3.8 has missing_ok parameter
            elif is_dir(filepath): Path(filepath).rmdir()
            print(f'{filepath} deleted.')

def move_item(item_filepath,new_cotaining_path,overwrite=False):
    if not exists(item_filepath):
        raise Exception(f"File to be moved: {item_filepath} doesn't exist")
    
    #new_path = Path(Path(new_cotaining_path) / get_filename(item_filepath,with_extension=True))
    new_path = Path(join(new_cotaining_path,get_filename(item_filepath,with_extension=True)))
    print('###')
    print(item_filepath)
    print(new_path)
    
    if not overwrite and exists(str(new_path)):
        raise Exception('Cannot overwrite existing file')
    else:
        print(3)
        print(Path(item_filepath))
        Path(item_filepath).rename(new_path)
        print(f'Move successful. {item_filepath} to {str(new_path)}')
        return str(new_path)

def copy_entire_dir(existing_item_filepath,new_cotaining_path,overwrite=False):
    shutil.copytree(existing_item_filepath, new_cotaining_path, dirs_exist_ok=overwrite)

def rename_item(new_name,existing_item_path):
    new_path = Path(Path(existing_item_path).parent / new_name)
    Path(existing_item_path).rename(new_path)
    return str(new_path)

def get_all_files_of_size(direc,size,comparison,subdir=True):
    '''input direc to search, comparison: either >,<,=
    and size(in kb)'''
    size = size*1000
    if comparison == '=':
        def f(file): return os.stat(file).st_size == size
    elif comparison == '>':
        def f(file):
            return os.stat(file).st_size > size
    elif comparison == '<':
        def f(file): return os.stat(file).st_size < size
    else:
        raise Exception(f'No valid comparison operator supplied. {comparison}')
    return [file for file in list_files(direc,subdir=subdir) if f(file)]

#date file was created, in numeric form
def _get_datecreated_file(filepath):
    return os.stat(filepath).st_ctime

#date file was created, in human form
def get_datecreated_file(filepath):
    return datetime.fromtimestamp(_get_datecreated_file(filepath))

#date file was modified, in numeric form
def _get_datemodified_file(filepath):
    return os.stat(filepath).st_mtime

#date file was modified, in human form
def get_datemodified_file(filepath):
    return datetime.fromtimestamp(_get_datemodified_file(filepath))

#helper function, returns list of files created, sorted on key
def _list_files(files=None,folder=None,subdir=False, descending=False, key=None):
    if not files: files=list_files(folder,subdir=subdir) #get list of files if arg=folder
    return sorted(files,key=key,reverse=descending)

'''return list of files sorted by date created, with earliest file on top
either input list of files or folder(choose if subdirectories as well'''
def list_file_date_created(files=None,folder=None,subdir=False, descending=False):
    return _list_files(files=files,folder=folder,subdir=subdir, descending=descending,key=get_datecreated_file)

'''return file with the latest date_created'''
def latest_file_date_created(files=None, folder=None,subdir=False):
    return list_file_date_created(files=files,folder=folder,subdir=subdir)[-1]

def list_file_date_modified(files=None,folder=None,subdir=False, descending=False):
    return _list_files(files=files,folder=folder,subdir=subdir, descending=descending,key=get_datemodified_file)

def latest_file_date_modified(files=None, folder=None,subdir=False):
    return list_file_date_modified(files=files,folder=folder,subdir=subdir)[-1]
