# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


# class DaomubijiPipeline(object):#需要在setting.py里设置'coolscrapy.piplines.CoolscrapyPipeline':300
#     def process_item(self, item, spider):
#         # 获取当前工作目录
#         base_dir = os.getcwd()
#         filename = base_dir + '/daomubijiquanji.txt'
#         # 从内存以追加的方式打开文件，并写入对应的数据
#         with open(filename, 'a', encoding='utf-8') as f:
#             f.write("\n".join(item['book_name']))
#             f.write("\n".join(item['chapter_name']))
#             f.write(item['content'])
#         return item



class DaomubijiPipeline(object):
    def process_item(self, item, spider):
        curPath = 'D:\盗墓笔记全集'
        tempPath = str(item['book_name'])
        targetPath = curPath + os.path.sep + tempPath
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)

        filename_path = 'D:\盗墓笔记全集' + os.path.sep + str(item['book_name']) + os.path.sep + str(item['chapter_name']) + '.txt'
        with open(filename_path, 'w', encoding='utf-8') as f:
            f.write(item['content'] + "\n")
        return item
