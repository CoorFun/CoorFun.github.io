Title: Pelican & GitHub Pages使用手记
Date: 2017-03-07 23:30
Category: Tech
Tags: Pelican, Python
Slug: Python-Pelican—Installation
Authors: Coor
Summary: Pelican

> 正式开始之前首先吐槽一下，呈现在这里的文章已经是”第三次创作“了。前两次的写作因为使用有道云笔记MAC OS客户端，由于未知原因，不仅文章未能同步至云端，本地的记录也消失不见，将此Bug反馈后未得到任何回复。。

> 不过不管有道云笔记怎么抽风，Pelican的好都值得我再写一遍此文，前两次就算是教训了！

> 此致敬礼，吐槽完毕，请看正文！

# 前言
在了解到静态博客之前，我曾使用Wordpress搭建我的个人博客。毫无疑问，Worepress可以说是目前为止最为强大的开源博客系统，大到资讯网站，小到个人博客都可以见到它的踪影。但是随着近些日子使用Markdown和Github的频次增加，越发感觉到用Markdown写作所带来的体验是以前那种“富文本”编辑器所不能及的。对于我这种英年早懒的人来说，Wordpress的很多所谓强大功能本身就是我所用不到的。像我这么少有的懒人，内容也没有那么高产，大多就是随便写写，打发打发时间。

于是最终我决定，通过GitHub Pages搭建一个纯静态的个人博客并自制一个主题。本文将首先介绍如何使用Pelican静态博客生成器和GitHub Pages服务搭建一个个人博客，后续的文章我会将主题的构建过程也分享给大家。

#静态博客
顾名思义，静态博客的概念相对于动态博客而来。其实所谓静态博客，可以简单的理解为一个纯粹由HTML和CSS构建起来的网站系统。相较于比较流行的动态博客系统，它的主要优缺点可以总结如下。

> 优点：

> - 部署简单
> - 体量轻盈
> - 加载速度很快
> - 方便使用git进行版本控制
> - 方便直接使用Markdown进行写作

> 缺点：

> - 灵活性和扩展性相对较差
> - 功能通常较为简单
> - 图片的插入与管理较为繁琐（无媒体管理和富文本编辑器）

在实际的应用场景下，大家可以根据自己的需要灵活的选择。

既然说静态博客完全由HTML页面组成，这就意味着在网页中的每一个链接实际都对应有一个HTML文件，如果将这些文件逐个编写保存，那使用静态博客就是一件得不偿失的事情了。所以这就是为什么我们需要使用“生成器”，静态博客生成器可以直接将用户编写的诸如Markdown之类的文本文件和主题样式整合后，一次性输出所有必要的HTML文件，有了这些文件后，我们直接将其上传到网页服务器就完成了部署。

# Pelican 
Pelican是一款基于Python编写的纯静态博客生成器，支持使用restructuredText和Markdown格式编写的文章，可以说是一款比较成熟的静态博客系统。相关的技术细节可以在官方和文档中找到。

- [Pelican 官方网站](https://blog.getpelican.com/)
- [Pelican 使用手册](http://docs.getpelican.com/en/stable/)
- [Pelican GitHub](https://github.com/getpelican/pelican)

以及本文需要用的Python虚拟环境Virtualenv参考网站：

- [Virtualenv 官方文档](https://virtualenv.pypa.io/en/stable/)

# 安装
**请注意，Pelican的环境要求为 Python 2.7.X或Python 3.3+**

该过程已Mac OS下的实践为例，其它平台大同小异，不再赘述。

比较简单的安装方式是直接使用pip获取Pelican包，Sierra自带有Python2.7但是没有pip包管理工具，所以我们首先通过easy-install安装pip：

> $ sudo easy_nstall pip

有了pip以后有两种方式继续安装，对于很少使用Python的用户而言，可以直接跟随第一种安装方式；对于平时还使用Python进行其它项目开发的用户，建议使用第二种方式，虚拟环境的好处是可以将不同Python项目的包分开管理，将每一个项目所需要的包独立存储在为这个项目的虚拟环境目录下。

### 方式1：直接安装

> $ sudo pip install pelican

### 方式2：在虚拟环境下安装
首先安装虚拟环境
> $ sudo pip install virtualenv

然后为Pelican创建一个专属虚拟环境（该目录可以随意指定，以下方式为官方建议方式）
> $ sudo virtualenv ~/virtualenv/pelican

> $ cd ~/virtualenv/pelican

启动虚拟环境
> $ source bin/activate

至此，接下来的所有操作都将在这个虚拟环境中完成，如果为其它的Python项目创建虚拟目录，该过程一样，只是存储目录有所不同。

用pip安装Pelican
> $ sudo pip install pelican

### 初始化一个Pelican项目
通过以上的步骤，我们获取的只是Pelican的工具包，现在使用该工具包对生成器环境进行初始化。

首先进入到站点所在的目录下（可以自定义）
> $ cd 目录名
        
运行快速启动指令
> $ pelican-quickstart

如果一切正常，该指令会产生一系列的问题，回答完毕后就完成了网站设定的初始化，这些问题可以稍后在pelicanconfg.py中修改。

**_但是，在Mac OS X和Sierra中，存在运行该指令后报错的问题，报错内容为:_**

> **ValueError: unknown locale: UTF-8**

**这是由于系统自身的一个小bug导致的。你可以尝试在用户目录下， 找到文件.bash_profile，在文件内容的开头加入下面两行内容即可。**
```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

**如果在用户目录一下找不到该文件，可以直接创建一个名为.bash_profile的文件，然后将以上内容写入即可**
> $ nano .bash_profile

至此，Pelican的安装和初始化就完成了。

# 写一篇文章
Pelican支持使用**_reStructuredText_**， **_Markdown_** 和 **_AsciiDoc formats_**等格式书写文章，我个人比较倾向于使用Markdown，关于Markdwon的语法这里不做赘述，请参考其官方网站：
> [Markdwon 语法参考](http://daringfireball.net/projects/markdown/syntax)

在文章正文开始之前，需要加入一些基本信息，如标题、修改时间、分类、关键词等等。
```
Title: 文章标题
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: 关键词1, 关键词2
Slug: my-super-post
Authors: 维多克雨果
Summary: 这是一篇假冒维多克雨果的文章

这里开始正文。
```
# 生成博客
将上面写好的文章保存在项目目录下的content，使用pelican命令生成网站。
> $ pelican content -s pelicanconfig.py

运行该指令后生成的静态HTML文件存放在output文件夹中。cd到output目录下，开启python的http服务即可预览网站的效果：

Python 2.7.X 用户请使用：
> $ python -m SimpleHTTPServer

Python 3.3+ 用户请使用：
> $ python -m http.server

现在就可以在浏览器中输入[http://localhost:8000/](http://localhost:8000/)查看博客了。