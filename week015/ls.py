import os
import argparse
import stat
import pwd
import grp
import datetime

class Color:
    pass

class FileSysObject(object):
    def __init__(self, path, a = False, l = False, R = False):
        self.path = path
        self.a = a
        self.l = l
        self.R = R

    def show(self):
        if self.l:
            FileSysObject.show_long_format(self.path)
        else:
            print(self.path, end = " ")

    def show_long_format(path):
        file_name = os.path.basename(path)
        p_stat = os.stat(path, follow_symlinks=False)
        show_o_str = (stat.filemode(p_stat.st_mode)
            + " " + str(p_stat.st_nlink).rjust(3, " ")
            + " " + pwd.getpwuid(p_stat.st_uid).pw_name
            + " " + grp.getgrgid(p_stat.st_gid).gr_name
            + " " + str(p_stat.st_size).rjust(5, " ")
            + " " + datetime.datetime.fromtimestamp(p_stat.st_mtime).strftime("%m %d %H:%M")
            + " " + file_name
            + " ")
        if os.path.islink(path):
            show_o_str = show_o_str + "-> " + os.readlink(path)
        print(show_o_str, end="\n")

class NotExistObject(FileSysObject):
    def show(self):
        print("ls: " + self.path + ": No such file or directory")

class FileObject(FileSysObject):
    pass

class DirectoryObject(FileSysObject):

    isp = True

    def __init__(self,path, is_show_header = False, a = False, l = False, R = False):
        super().__init__(path, a, l, R)
        self.is_show_header = is_show_header

    def get_path_list(self):
        ld = os.listdir(self.path)
        if not self.a:
            #.ではじまるファイルを除く
            ld = filter((lambda x: x[0] != "."), ld)

        path_list = [os.path.join(self.path, filename) for filename in ld]
        if self.a:
            # .と..を先頭に追加
            path_list.insert(0, ".")
            path_list.insert(1, "..")

        return path_list

    def show(self):
        if self.is_show_header:
            print(self.path + ":")

        path_list = self.get_path_list()

        for path in path_list:
            if self.l:
                FileSysObject.show_long_format(path)
            else:
                print(os.path.basename(path), end = " ")

        for path in path_list:
            if self.R:
                if os.path.isdir(path):
                    print()
                    do = DirectoryObject(path, is_show_header = True, a = self.a, l = self.l, R = self.R)
                    do.show()

        if not self.l:
            print()

def get_object(path, is_not_solo_path, a, l, R):
    if not os.path.exists(path):
        return NotExistObject(path, a, l, R)
    elif os.path.isfile(path):
        return FileObject(path, a, l, R)
    elif os.path.isdir(path):
        return DirectoryObject(path, is_show_header = is_not_solo_path, a = a, l = l, R = R)

def main(args):
    if len(args.path) == 0:
        args.path = ["./"]

    neos = []
    fos = []
    dos = []
    is_not_solo_path = len(args.path) != 1
    for i in args.path:
        fso = get_object(i, is_not_solo_path, args.a, args.l, args.R)
        if isinstance(fso, NotExistObject):
            neos.append(fso)
        elif isinstance(fso, FileObject):
            fos.append(fso)
        elif isinstance(fso, DirectoryObject):
            dos.append(fso)

    for neo in neos:
        neo.show()

    fos = sorted(fos, key=lambda fileobject: fileobject.path)
    for fo in fos:
        fo.show()
    if len(fos) != 0:
        print()

    dos = sorted(dos, key=lambda dirobject: dirobject.path)
    for i, do in enumerate(dos):
        if i > 0:
            print()
        do.show()

if __name__ == "__main__":
    # arg parser
    parser = argparse.ArgumentParser("")
    parser.add_argument("-l", action="store_true", default=False)
    parser.add_argument("-a", action="store_true", default=False)
    parser.add_argument("-R", action="store_true", default=False)
    parser.add_argument("path", nargs="*", default=None)
    # arg parse
    args = parser.parse_args()
    # main
    main(args)