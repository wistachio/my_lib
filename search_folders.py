import lib.filelib as fl


#search for words in text files in the direc and subdirs
#single word must be in list format as well
def search_word_files(direc, lst_words, subdir=False):
    files = fl.list_files_with_extension(direc,'txt',subdir)
    result = []
    for word in lst_words:
        for file in files:
            try:
                content=fl.read_txt_file(file)
                if word.lower() in content.lower():
                    result.append(file)
            except:
                print('error handling file: ', file)
    return result
