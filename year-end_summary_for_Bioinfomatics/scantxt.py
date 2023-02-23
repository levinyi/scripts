import os
import multiprocessing
def scan_files(dir):
    # 获取指定目录下的所有文件
    files = os.listdir(dir)
    # 遍历文件
    for file in files:
        # 判断文件是否为文件夹
        if os.path.isdir(os.path.join(dir, file)):
            # 递归调用函数
            scan_files(os.path.join(dir, file))
        # 判断文件是否为txt文件
        elif file[-3:] == 'txt':
            print(file)


if __name__ == '__main__':
    # 获取指定目录
    dir = './'
    # 创建进程池
    pool = multiprocessing.Pool()
    # 向进程池中添加任务
    pool.apply_async(scan_files, args=(dir,))
    # 关闭进程池
    pool.close()
    # 等待进程池中的任务完成
    pool.join()
