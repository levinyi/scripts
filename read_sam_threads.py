import threading
import url_func
import sys
import Queue
 
 
class Reader(threading.Thread):
    def __init__(self, thread_id):
        super(Reader, self).__init__()
        self.thread_id = thread_id
 
    def run(self):
        global q
 
        temp_list = q.get()
 
        for text in temp_list:
            columns = text.split('\001')
            if len(columns) == 8:
                #取出线程对应文件内容后的文件操作,可忽略
                url_func.url_make_open(a_o_b, plat_form, self.thread_id, columns)
 
 
class Partition(object):
    def __init__(self, file_name, thread_num):
        self.file_name = file_name
        self.block_num = thread_num
 
    #按照线程数对文件进行分块并存进queue中
    def part_and_queue(self):
        pos_list = []
        #文件总行数
        file_size = url_func.file_lines(self.file_name)
        #按照线程数分成对应块的大小
        block_size = file_size / self.block_num
        start_pos = 0
        global q
 
        for i in range(self.block_num):
            if i == self.block_num - 1:
                end_pos = file_size - 1
                pos_list.append((start_pos, end_pos))
                break
            end_pos = start_pos + block_size - 1
            if end_pos >= file_size:
                end_pos = file_size - 1
            if start_pos >= file_size:
                break
            pos_list.append((start_pos, end_pos))
            start_pos = end_pos + 1
 
        #读取每块内容存进queue中
        fd = open(self.file_name, 'r')
        for pos_tu in pos_list:
            temp_text = []
            start = pos_tu[0]
            end = pos_tu[1]
 
            while start <= end:
                text = fd.readline().strip('\n')
                temp_text.append(text)
                start = start + 1
 
            q.put(temp_text)
        fd.close()
 
 
if __name__ == '__main__':
    
    file_name = sys.argv[1] #samfile
    plat_form = sys.argv[2]
    a_o_b = sys.argv[3]
 
    #线程数量可配
    thread_num = 10
    q = Queue.Queue()
    p = Partition(file_name, thread_num)
    t = []
    p.part_and_queue()
 
    for i in range(thread_num):
        t.append(Reader(i))
    for i in range(thread_num):
        t[i].start()
    for i in range(thread_num):
        t[i].join()
