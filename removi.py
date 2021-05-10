a = list(map(lambda h: h.replace(remove, ''), file_list))
b = a
for x in b:
    try:
        os.mkdir(os.path.join(dire, str(x)))
    except WindowsError:
        pass
file_list2 = os.listdir(dire)
files = [i for i in os.listdir(dire) if i.endswith(remove) and path.isdir(path.join(dire, i))]
files2 = [p for p in os.listdir(dire) if not p.endswith(remove) and path.isdir(path.join(dire, p))]


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


def listfiles_fullpath(d):
    return [os.path.join(d, f) for f in files]


def listfiles2_fullpath(d):
    return [os.path.join(d, f) for f in files2]


h = listfiles_fullpath(dire)
g = listfiles2_fullpath(dire)
for f, b in zip(h, g):
    shutil.move(str(f), str(b)