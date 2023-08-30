import zipfile
import os
from pathlib import Path

def extractFile(zfile, password, dir):
    try:
        zfile.extractall(path=dir, pwd=password)
        return password
    except:
        print('Wrong password')
        return


def main():
    userzFile = input('Enter name of archive: ')
    userpFile = input('Enter name of password wordlist: ')
    userExtDir = input('Enter name of directory to exract to: ')

    if os.path.exists(userExtDir):
        print('Directory found, files are going to be extracted to ' + userExtDir)
    else:
        print('Directory not found, instead created one')
        os.makedirs(userExtDir)

    zfile = zipfile.ZipFile(userzFile)
    passFile = open(userpFile)
    
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile, password, userExtDir)
        if guess:
            print('Password is: ' + password)
            print('Your archive was decompressed')
            break


if __name__ == '__main__':
    main()