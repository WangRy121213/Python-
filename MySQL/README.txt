本文档旨在记录pymysql的语法与图片下载和csv文件的简单用法与例子
   -数据存储：
      使用的工具包：
          urllib.request,os,csv,ssl
      使用的函数：
          urlretrieve,urlopen
      注意：
          1.ssl包用于解决爬虫中的证书错误问题：
            ssl._create_default_https_context = ssl._create_unverified_context
          2.urlretrieve(imageLocation,"图片路径.jpg")
            imageLocation:图片的下载路径
            bs0bj.find("a",{"id":"logo"}).find("img")["src"]
   -MySQL:
      使用的工具包：
          pymysql      