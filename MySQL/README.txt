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
      该文档中用练习运用time，sched等模块，学习如何联系运行代码
      该文档使用pymysql练习connect.cursor与插入查询等操作
      使用的工具包：
          pymysql,time,sched
      使用的函数：
          scheduler,enter,run 
        使用的步骤：
          1.schedule = sched.scheduler(time.time,time.sleep)
            inc:为间隔时间 cmd：为执行的参数
          2.def fonction1{需要持续执行的函数}(cmd,inc):
            schedule.enter(inc,0,fonction,(cmd, inc))
            """
            反复执行的函数体 
            """
          3.def fonction2{首次执行的函数}(cmd,inc)
            schedule.enter(inc,0,fonction,(cmd, inc))
            #开始执行函数
            schedule.run()
          4.fonction2{首次执行的函数}(cmd,inc)
      简单SQL语句
          cmd窗口登陆数据库： mysql -u root -p
          
          查询mysql的端口号:show global variables like 'port';

          列出字段及详情：SHOW FULL COLUMNS FROM tb1_name[FROM db_name]

          SELECT * FROM open_medic WHERE AGE BETWEEN 12 and 60

          改变数据库的编码方式：
             
             ALTER DATABASE scraping CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
          
          改变表的编码方式
          
             ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
          
          改变具体字段的编码方式
          
             ALTER TABLE pages CHANGE title title VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
             
          
          创建，指定数据库存放数据：
            >CREATE DATABASE scraping   >USE scraping
            
          创建表
            >CREATE TABLE pages(id BIGINT(7) NOT NULL AUTO_INCREMENT, title     VARCHAR(200),content VARCHAR(10000), created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(id))
            
          插入字段
            >INSERT INTO pages(title,content) VALUES ("Test page title", "This is some test page content. It can be up to 10,000 characters long.");
          
          数据选择和查询语句
            > SELECT * From pages WHERE id=2;

            > SELECT * FROM pages WHERE title LIKE "%test%"(title包含test的所有行)

            > SELECT id, title FROM pages WHERE content LIKE "%page content%"

          数据删除与更新
            > DELETE FROM pages WHERE id = 1
            
            > UPDATE pages SET title="A new title", content="Some new content" WHERE id=2

                    