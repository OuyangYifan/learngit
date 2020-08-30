import os,glob


def rename(dir,pattern,new):
    #[os.rename(f, f.replace('_', '-')) for f in os.listdir('.')]
    i_No = 0;
    for pathAndFilename in glob.iglob(os.path.join(dir,pattern)):
            title,ext = os.path.splitext(os.path.basename(pathAndFilename))
            print(title + ext)
           
            os.rename(pathAndFilename,os.path.join(dir,new %i_No+ext))
            i_No = i_No + 1


def main():
    rename(r'e://',r'*.mp3',r'No_%d')
    rename(r'e://',r'*.mp4',r'No_%d')

if __name__ == '__main__':
    main()







