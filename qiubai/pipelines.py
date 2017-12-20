# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import codecs

class QiubaiPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/qiubai.txt'
        try:
            with open(filename, 'a') as f:
                f.write('作者:{}\n作者链接:{}\n{}\n点赞数目:{}\t评论数目:{}\n\n'.format(item['author'], item['link'], item['content'], item['supportNum'], item['commentNum']))
        except:
            print('写txt文件失败')
            return 'error'
        return item

class Qiubai2Json(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/qiubai.json'
        try:
            with codecs.open(filename, 'a') as f:
                line = json.dumps(dict(item), ensure_ascii = False) + '\n'
                f.write(line)
        except:
            print('写json文件失败')
            return 'error'
        return item
