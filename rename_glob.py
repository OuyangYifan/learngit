import os,glob


def rename(dir,pattern,new):
    i_No = 0;
    for pathAndFilename in glob.iglob(os.path.join(dir,pattern)):
            title,ext = os.path.splitext(os.path.basename(pathAndFilename))
            if ext == None:
                ext = '.mp3'
            os.rename(pathAndFilename,os.path.join(dir,new %i_No+ext))
            i_No = i_No + 1


def main():
    rename(r'e://',r'*.*',r'No_%d')

if __name__ == '__main__':
    main()







