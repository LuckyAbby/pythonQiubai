# pythonQiubai
一个运用 scrapy 框架爬取糗事百科相关信息的小爬虫

## 运行环境
- python3
- scrapy

## 运行步骤
- install scrapy
```
pip install scrapy
```
- clone &&  run project
```
git clone https://github.com/LuckyAbby/pythonQiubai.git
cd pythonQiubai
scrapy crawl qiubaispider
```
## 注意要点
- 最后爬取的数据以txt和json的数据格式存放在data目录下，运行前可以删除之前的data目录里面的文件，重新爬取相关的信息。
- 代码中我只爬取了前三页，具体可以自己更改。

最后祝大家python越学越6
