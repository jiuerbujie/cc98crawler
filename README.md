cc98crawler
==========================
浙大CC98论坛的爬虫，可以通过*正则表达式*指定需要爬下的板块和内容，默认配置为爬下[缘分天空]板块中的图片（所谓王道）。
通过修改配置文件，也可以应用与其他论坛。

依赖
----------
python 2.7

如何使用
--------------
```
git clone git@github.com:jiuerbujie/cc98crawler.git

python cc98crawler.py
```

配置文件
--------------
文件```config.ini```为配置文件，对其进行修改，可以指定不同板块，不同内容。如，可以指定[开怀一笑]板块中的[gif动图]。配置文件中每一项的具如含义如下：
- form_user：登录表单中“用户名”这一项的名称
- form_pwd：登录表单中“密码”这一项的名称
以上两项是为了兼容其他论坛，若无需要不要更改。
- username：论坛用户名
- password：密码
- cookieFile：若有cookie文件，则指定文件名，若无，则为空
- loginUrl：登录地址
**下面是重点**
- pageFormat：论坛每一页的地址，对于CC98来说，“BoardID=”后面的数字指定了板块，[缘分天空]是152，“page=”后面的数字指定了页码，因此此选项设为http://www.cc98.org/list.asp?BoardID=152&page=%d&action=就指定了[缘分天空]板块，页码通过“%d”由程序指定。其他论坛也类似，比如19楼论坛的某个板块的此选项可以为http://www.19lou.com/forum-32-filter-type-typeid-825-%d.html?order=lastpost
- prefix：在某个板块的html中，每个帖子的url是简写，会省略掉前缀
- nPage：要爬下的页数
- postReg：在板块中通过此参数的正则表达式找到帖子的url，每个论坛不一样
- postRegIdx：上面的正则表达式可能返回多个内容，指定所需要的下标
- targetReg：在每个帖子中通过此正则表达式找到需要的内容，如图片
- targetRegIdx：上面的正则表达式可能返回多个内容，指定所需要的下标
- savePath：保存的路径，windows用户请用“/”指定路径，如“D:/cc98/”

