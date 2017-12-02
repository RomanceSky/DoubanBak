# DoubanBak
仿豆瓣网站代码备份
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# git remote rm origin1
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# ls
db.sqlite3  manage.py  minicms  news  static
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# git remote -v
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# git remote add origin1 https://github.com/RomanceSky/DoubanBak.git
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# git config --global user.name "RomanceSky"
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# git config --global user.email "1171039932@qq.com"
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# git add -A
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# git commit -m "xixi"
# On branch master
nothing to commit, working directory clean
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# git push origin1 master
Username for 'https://github.com': RomanceSky
Password for 'https://RomanceSky@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/RomanceSky/DoubanBak.git/'
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# 
Connection closed by foreign host.

Disconnected from remote host(阿里云服务器) at 10:32:29.

Type `help' to learn how to use Xshell prompt.
[c:\~]$ 
使用这种方式创建失败：
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz minicms]# git remote add origin1 git@github.com:RomanceSky/DoubanBak.git
参考
https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93%E7%9A%84%E4%BD%BF%E7%94%A8
