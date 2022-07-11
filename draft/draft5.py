import os
import shutil



if __name__ == '__main__':
	folder = r'E:\BaiduNetdiskDownload\课程007：算法数据结构体系学习班'
	subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
	print(subfolders)
for sub in subfolders:
    for f in os.listdir(sub):
        src = os.path.join(sub, f)
        dst = os.path.join(folder, f)
        shutil.move(src, dst)