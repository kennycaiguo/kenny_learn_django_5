# 1.Django模板介绍

## 1.1模板概念

![image-20260625120010301](./note5-django模板语法学习.assets/image-20260625120010301.png)



## 1.2 模板渲染

![image-20260625120526496](./note5-django模板语法学习.assets/image-20260625120526496.png)

## 1.3模板匹配路径

![image-20260625124927587](./note5-django模板语法学习.assets/image-20260625124927587.png)

## 演练，还是我们的firstdjapp项目

### 1》我们在templates里面新建一个index.html,内容如下

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Welcome to index</title>
</head>
<body>
<ul>
    <li>
        <ul>
            Book应用程序
            <li><a href="book/">Random Books</a></li>
            <li><a href="book/query/?index=7">Query Book</a></li>
            <li><a href="book/item/1">Get a Book</a></li>
        </ul>
    </li>
    <li>
        <ul>
            Move应用程序
            <li><a href="movie/">Random Movies</a></li>
            <li><a href="movie/query/?index=7">Query Movie</a></li>
            <li><a href="movie/item/1">Get a Movie</a></li>
        </ul>

    </li>
</ul>
</body>
</html>
```

### 2> 然后我们修改一下默认应用程序里面的urls.py,用render（注意，是django.shortcuts 里面的render，不要搞错了)函数来形容我们的index.html文件

![image-20260625123624690](./note5-django模板语法学习.assets/image-20260625123624690.png)

## 运行程序，效果如下

![image-20260625123708496](./note5-django模板语法学习.assets/image-20260625123708496.png)

### 注意，

### 1，列表里面的超链接不要搞错，然后点击对应的超链接就可以打开对应的路由

### 2.可以在应用程序里面新建一个templates并且防止模板文件，前提是需要在默认应用程序里面的settings.py安装我们的应用程序，并且设置'APP_DIRS': True,

![image-20260625130401805](./note5-django模板语法学习.assets/image-20260625130401805.png)

#### 1.比如我们在我们的books文件夹里面新建一个templates文件夹，然后在里面新建一个testBook.html

![image-20260625130703889](./note5-django模板语法学习.assets/image-20260625130703889.png)

#### 2.然后我们在book.urls.py里面配置一个test/路由映射到book.views.py里面的test函数，然后在test函数里面渲染模板

![image-20260625131102004](./note5-django模板语法学习.assets/image-20260625131102004.png)

![image-20260625131117282](./note5-django模板语法学习.assets/image-20260625131117282.png)

### 效果如下

![image-20260625131227001](./note5-django模板语法学习.assets/image-20260625131227001.png)

# 2.模板语法

## 2.1变量

![image-20260625131709809](./note5-django模板语法学习.assets/image-20260625131709809.png)

## 演练

### 1》我们在渲染testBook.html的时候，传递一个greeting变量，然后可以在模板里面使用{{greeting}}来获取他的值

![image-20260625133020784](./note5-django模板语法学习.assets/image-20260625133020784.png)

![image-20260625133045631](./note5-django模板语法学习.assets/image-20260625133045631.png)

### 2.效果

![image-20260625133118071](./note5-django模板语法学习.assets/image-20260625133118071.png)

## 演练2，把一个字典传递给模板

### 1.我们创建一个author字典，然后把他传递给模板

![image-20260625133834024](./note5-django模板语法学习.assets/image-20260625133834024.png)

### 2.然后我们需要在模板文件里面获取这个字典的每一个属性的值，注意在模板里面不能使用author['name']的语法来获取值，需要使用.语法，就像使用js的对象获取属性一样的语法

![image-20260625134458439](./note5-django模板语法学习.assets/image-20260625134458439.png)

## 演练3，把一个列表传递给模板

### 1>我们创建一个datas字典，里面添加一个“like”，他的值是一个列表

![image-20260625135243926](./note5-django模板语法学习.assets/image-20260625135243926.png)

### 2>此时如果我们需要获取列表里面的项，我们需要使用列表名称.0来获取的第一项，列表名称.1来获取第二项...以此类推

![image-20260625135742642](./note5-django模板语法学习.assets/image-20260625135742642.png)

### 效果

![image-20260625135847322](./note5-django模板语法学习.assets/image-20260625135847322.png)

## 还可以使用对象列表

![image-20260625140043572](./note5-django模板语法学习.assets/image-20260625140043572.png)

### 然后列表里面的一个对象的属性需要这么获取

![image-20260625140200546](./note5-django模板语法学习.assets/image-20260625140200546.png)

### 效果

![image-20260625140220509](./note5-django模板语法学习.assets/image-20260625140220509.png)

## 演练4.传递一个person的类对象

### 4.1》我们创建一个Book类，有一个info方法和一个魔术方法 __ str__

![image-20260625141435508](./note5-django模板语法学习.assets/image-20260625141435508.png)

### 4.2>然后我们创建一个book对象并且把它中文一个context的属性传递给模板，

![image-20260625141707698](./note5-django模板语法学习.assets/image-20260625141707698.png)

### 4.3>然后在模板里面居然也可以定义book的方法，但是不需要小括号

![image-20260625141830110](./note5-django模板语法学习.assets/image-20260625141830110.png)



### 效果

![image-20260625141855987](./note5-django模板语法学习.assets/image-20260625141855987.png)

# 3.常用标签

## 在模板里面可以使用python代码，但是必须放在{%%}里面，可以使用循环，推荐，操作符号等等一系列的语法，在调用方法或者函数时不要使用小括号

![image-20260625145818396](./note5-django模板语法学习.assets/image-20260625145818396.png)

![image-20260625145941193](./note5-django模板语法学习.assets/image-20260625145941193.png)

![image-20260625150039539](./note5-django模板语法学习.assets/image-20260625150039539.png)

![image-20260625150116728](./note5-django模板语法学习.assets/image-20260625150116728.png)

![image-20260625151027371](./note5-django模板语法学习.assets/image-20260625151027371.png)

![image-20260625151151141](./note5-django模板语法学习.assets/image-20260625151151141.png)

![image-20260625151243484](./note5-django模板语法学习.assets/image-20260625151243484.png)

![image-20260625151336914](./note5-django模板语法学习.assets/image-20260625151336914.png)

## 演练，

### 1.给我们的下面添加有famous应用程序，用来显示名著信息

![image-20260625153320573](./note5-django模板语法学习.assets/image-20260625153320573.png)

### 2.个famous模块添加一个urls.py和一个templates文件夹，用来存放这个路由相关的模板文件

![image-20260625153521422](./note5-django模板语法学习.assets/image-20260625153521422.png)

### 3.在默认应用程序的settings.py里面注册famous应用程序

![image-20260625153646821](./note5-django模板语法学习.assets/image-20260625153646821.png)

### 4.在firstdjapp/urls.py里面配置famous相关的路由

![image-20260625153833559](./note5-django模板语法学习.assets/image-20260625153833559.png)

### 5.转到famous/urls.py,首先添加命名空间，然后添加一条路由映射，注意此时我们视图函数还没有创建，我们马上就会创建它

![image-20260625154148144](./note5-django模板语法学习.assets/image-20260625154148144.png)

### 6.回到famous/views.py,我们来创建这个index函数

![image-20260625171825018](./note5-django模板语法学习.assets/image-20260625171825018.png)

### 7.然后我们需要在famous/templates里面新建一个famous.html模板文件，在里面遍历整个列表，然后显示我们的数据

![image-20260625172150480](./note5-django模板语法学习.assets/image-20260625172150480.png)

### 运行程序，效果如下

![image-20260625172205466](./note5-django模板语法学习.assets/image-20260625172205466.png)

# 4.常用过滤器



# 5.自定义管理器



# 6.模板结构



# 7.静态文件



