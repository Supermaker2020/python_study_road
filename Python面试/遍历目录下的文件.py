import os


def walkfile(rt, shuf):
    res = []
    for root, dirs, files in os.walk(rt):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == shuf:
                res.append(os.path.join(root, filename))
    print(res)


def isfile2(obj):
    if obj.endswith('.py'):
        print(obj)


def scan_path(ph):
    file_list = os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):
            isfile2(obj)
        elif os.path.isdir(obj):
            scan_path(obj)


if __name__ == '__main__':
    rt = r'C:\Users\Administrator\Desktop\算法学习'
    try:
        walkfile(rt, '.py')
    except BaseException:
        pass
