import os
import stat
import pwd
import grp
import glob
import datetime
import argparse

class Color:
    pass

class FileSysObject(object):
    def __init__(self, path):
        self.path = path

    def show(self):
        print(self.path + " is FileSysObject")

class NotExistObject(FileSysObject):
    def show(self):
        print("ls: " + self.path + ": No such file or directory")

class FileObject(FileSysObject):
    def show(self):
        print(self.path, end = " ")

class DirectoryObject(FileSysObject):

    isp = True

    def __init__(self,path, issolopath):
        super().__init__(path)
        DirectoryObject.isp = issolopath

    def show(self):
        if DirectoryObject.isp:
            pass
        else:
            print(self.path + ":")

        ld = os.listdir(self.path)
        for file in ld:
            print(file, end = " ")
        print()



#class LinkObject(FileSysObject):
#    def show(self):
#        print(self.path + " is LinkObject")

def get_object(path, issolopath):
    if not os.path.exists(path):
        return NotExistObject(path)
    #elif os.path.islink(path):
    #    return LinkObject(path)
    elif os.path.isfile(path):
        return FileObject(path)
    elif os.path.isdir(path):
        return DirectoryObject(path, issolopath)

def main(args):
    if len(args.path) == 0:
        args.path = ["./"]

    neos = []
    #los = []
    fos = []
    dos = []
    issolopath = len(args.path) == 1
    for i in args.path:
        fso = get_object(i, issolopath)
        if isinstance(fso, NotExistObject):
            neos.append(fso)
        #elif isinstance(fso, LinkObject):
        #    los.append(fso)
        elif isinstance(fso, FileObject):
            fos.append(fso)
        elif isinstance(fso, DirectoryObject):
            dos.append(fso)

    for neo in neos:
        neo.show()

    #for lo in los:
    #    lo.show()

    fos = sorted(fos, key=lambda fileobject: fileobject.path)
    for fo in fos:
        fo.show()
    if len(fos) != 0:
        print()

    dos = sorted(dos, key=lambda dirobject: dirobject.path)
    for do in dos:
        do.show()
        print()




if __name__ == "__main__":
    # arg parser
    parser = argparse.ArgumentParser("")
    parser.add_argument("-l", action="store_true", default=False)
    parser.add_argument("-a", action="store_true", default=False)
    parser.add_argument("path", nargs="*", default=None)
    # arg parse
    args = parser.parse_args()
    # main
    main(args)