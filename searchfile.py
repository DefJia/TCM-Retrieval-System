# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 09:46:50 2019

@author: yang
"""

from docx import Document
import os,sys

def search_word(filename,word):
    #打开文档
    document = Document(filename)
    # document = Document(r'C:\Users\Cheng\Desktop\kword\words\wind.docx')
    print(filename)
    #读取每段资料
    #l = [ paragraph.text.encode('gb2312') for paragraph in document.paragraphs]
    l = [ paragraph.text.encode('utf-8') for paragraph in document.paragraphs]
    #输出并观察结果，也可以通过其他手段处理文本即可
    wordB = word.encode('utf-8')
    for i in l:
        i=i.strip()
        #print(i)
        if i.find(wordB)!=-1:
            print(filename, i.decode())

def get_process_files(root_dir):
    """process all files in directory"""
    cur_dir=os.path.abspath(root_dir)
    file_list=os.listdir(cur_dir)
    process_list=[]
    for file in file_list:
        fullfile=cur_dir+"\\"+file
        if os.path.isfile(fullfile):
            process_list.append(fullfile)
        elif os.path.isdir(fullfile):
            dir_extra_list=get_process_files(fullfile)
            if len(dir_extra_list)!=0:
                for x in dir_extra_list:
                    process_list.append(x)
    return process_list

def find_files(root_dir,word):
    process_list=get_process_files(root_dir)
    for files in process_list:
        try:
            search_word(files, word)
        except Exception as e:
            print(e)
            

if __name__=='__main__':
    #文件根目录
    #root_dir=sys.argv[1]
    root_dir = r"D:\2018.6.25组会\药方著作"
    #要搜索的关键字
    #word=sys.argv[2]
    word = "枸杞"
    try:
        find_files(root_dir,word)
    except Exception as e:
        print(e)
