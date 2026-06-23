## 1.创建django项目有2种方法

![image-20260623115632874](./note04-第一个django项目.assets/image-20260623115632874.png)

### 我们创建一个firstdjapp应用程序，然后我们创建一个book应用程序，如图

![image-20260623132634247](./note04-第一个django项目.assets/image-20260623132634247.png)

### 注意，最好在firstdjapp/settings.py里面注册我们的book应用程序

![image-20260623133052054](./note04-第一个django项目.assets/image-20260623133052054.png)

## 2.项目的运行

![image-20260623122128165](./note04-第一个django项目.assets/image-20260623122128165.png)

## 3.项目解析

![image-20260623122204273](./note04-第一个django项目.assets/image-20260623122204273.png)

## 4.路由映射

   ### 1>在项目的默认app里面的urls.py里面配置，也就是项目的同名目录，需要先定义视图函数，一般在我们自己创建的app的views.py文件里面定义，比如我们在book的view模块里面创建一个show_books函数，我们用它来中文/books路由的函数

![image-20260623132803218](./note04-第一个django项目.assets/image-20260623132803218.png)

### 2>然后我们需要在默认应用程序firstdjapp里面的urls.py里面建立这个路由映射，需要把我们的show_books函数导入进来

![image-20260623133235608](./note04-第一个django项目.assets/image-20260623133235608.png)

### 3>启动项目，输入books/就可以访问了

![image-20260623133330545](./note04-第一个django项目.assets/image-20260623133330545.png)

## 5.在url中携带参数，有2种方法

![image-20260623133600842](./note04-第一个django项目.assets/image-20260623133600842.png)

### 方法1.我们在book.view模块里面创建一个函数，获取book/?index=1里面的index.值，然后返回对应索引的书，我们先在book.view里面新建一个query_book_by_id函数，获取url传递过来的index变量，然后把对应索引的书籍返回给用户，注意：从url里面获取的是字符串，我们需要整数，所以需要类型转换

![image-20260623134829770](./note04-第一个django项目.assets/image-20260623134829770.png)

### 然后我们需要在firstdjapp.urls.py里面添加这样子的匹配，不需要匹配查询字符串

![image-20260623134954465](./note04-第一个django项目.assets/image-20260623134954465.png)

### 效果：

![image-20260623150645979](./note04-第一个django项目.assets/image-20260623150645979.png)

### 方法2.使用路径参数如books/book/3,此时我们需要在firstdjapp.urls.py里面的路由匹配里面使用变量，我们先在在firstdjapp.urls.py里面配置一个带参数的路由，

![image-20260623145834070](./note04-第一个django项目.assets/image-20260623145834070.png)

#### 注意，变量前面的参数类型可以不写，不过建议还是写了，因为这样子才会有变量类型检查。

### 然后我们需要在book.view.py里面创建一个get_book_by_id函数，需要一个id参数来接收来自url的变量

![image-20260623145900734](./note04-第一个django项目.assets/image-20260623145900734.png)

### 效果

![image-20260623145940952](./note04-第一个django项目.assets/image-20260623145940952.png)

## 6.path函数的使用

![image-20260623155437085](./note04-第一个django项目.assets/image-20260623155437085.png)

### 那么问题来了，什么是slug类型？什么是path类型？

#### slug类型的用法

![image-20260623160242086](./note04-第一个django项目.assets/image-20260623160242086.png)

![image-20260623160323942](./note04-第一个django项目.assets/image-20260623160323942.png)

![image-20260623160535655](./note04-第一个django项目.assets/image-20260623160535655.png)

![image-20260623160623319](./note04-第一个django项目.assets/image-20260623160623319.png)

![image-20260623160748437](./note04-第一个django项目.assets/image-20260623160748437.png)

![image-20260623160834940](./note04-第一个django项目.assets/image-20260623160834940.png)

#### path类型的用法

![image-20260623160940103](./note04-第一个django项目.assets/image-20260623160940103.png)

![image-20260623161025315](./note04-第一个django项目.assets/image-20260623161025315.png)

![image-20260623161121861](./note04-第一个django项目.assets/image-20260623161121861.png)

![image-20260623161216338](./note04-第一个django项目.assets/image-20260623161216338.png)
