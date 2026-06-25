# 1.创建项目以及基本的路由映射和路由参数的使用
## 1》创建django项目有2种方法

![image-20260623115632874](./note04-第一个django项目.assets/image-20260623115632874.png)

### 我们创建一个firstdjapp应用程序，然后我们创建一个book应用程序，如图

![image-20260623132634247](./note04-第一个django项目.assets/image-20260623132634247.png)

### 注意，最好在firstdjapp/settings.py里面注册我们的book应用程序

![image-20260623133052054](./note04-第一个django项目.assets/image-20260623133052054.png)

## 2》项目的运行

![image-20260623122128165](./note04-第一个django项目.assets/image-20260623122128165.png)

## 3》项目解析

![image-20260623122204273](./note04-第一个django项目.assets/image-20260623122204273.png)

## 4》路由映射

   ### 1>在项目的默认app里面的urls.py里面配置，也就是项目的同名目录，需要先定义视图函数，一般在我们自己创建的app的views.py文件里面定义，比如我们在book的view模块里面创建一个show_books函数，我们用它来中文/books路由的函数

![image-20260623132803218](./note04-第一个django项目.assets/image-20260623132803218.png)

### 2>然后我们需要在默认应用程序firstdjapp里面的urls.py里面建立这个路由映射，需要把我们的show_books函数导入进来

![image-20260623133235608](./note04-第一个django项目.assets/image-20260623133235608.png)

### 3>启动项目，输入books/就可以访问了

![image-20260623133330545](./note04-第一个django项目.assets/image-20260623133330545.png)

## 5》在url中携带参数，有2种方法

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

## 6》path函数的使用

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

## 扩展：为了方便学习，我们给项目添加一个movie应用程序

![image-20260624141307698](./note04-第一个django项目以及django基础-路由.assets/image-20260624141307698.png)

### 我们给movie应用程序创建一个urls.py,创建一些路由和对应的views.py里面的函数映射起来

![image-20260624145235109](./note04-第一个django项目以及django基础-路由.assets/image-20260624145235109.png)

### 然后在movie/views.py里面创建一些视图函数

### ![image-20260624145155122](./note04-第一个django项目以及django基础-路由.assets/image-20260624145155122.png)

#### 运行程序，效果一切正常

![image-20260624145319513](./note04-第一个django项目以及django基础-路由.assets/image-20260624145319513.png)

![image-20260624145345879](./note04-第一个django项目以及django基础-路由.assets/image-20260624145345879.png)

![image-20260624145418589](./note04-第一个django项目以及django基础-路由.assets/image-20260624145418589.png)

# 2.路由功能学习

## 2.1》路由模块化

### 1）在一个urls文件里面包含另外一个urls文件

![image-20260624134955293](./note04-第一个django项目以及django基础-路由.assets/image-20260624134955293.png)

### 演练

####  1.在book应用程序文件夹里面新建一个urls.py,把book修改的路由都放在book/urls.py中,同时我们把books路由改为book，books/book改为book/item

![image-20260624140453998](./note04-第一个django项目以及django基础-路由.assets/image-20260624140453998.png)

#### 2.然后我们修改firstdjapp里面的urls.py,在里面包含book/urls.py

![image-20260624140655719](./note04-第一个django项目以及django基础-路由.assets/image-20260624140655719.png)

##### 注意：为了防止访问http:127.0.0.1:8000/报错，我们添加了一个空路由，一栏匹配主机根路由

![image-20260624140842951](./note04-第一个django项目以及django基础-路由.assets/image-20260624140842951.png)

### 效果：

![image-20260624140908288](./note04-第一个django项目以及django基础-路由.assets/image-20260624140908288.png)

![image-20260624140932442](./note04-第一个django项目以及django基础-路由.assets/image-20260624140932442.png)

![image-20260624140959369](./note04-第一个django项目以及django基础-路由.assets/image-20260624140959369.png)

![image-20260624141027059](./note04-第一个django项目以及django基础-路由.assets/image-20260624141027059.png)

## 注意，方便路由过来，我们需要在movie/urls.py里面设置一个应用程序名称，好处是方便团队的其他成员明白你这个urls是哪个应用程序里面的。还可以避免命名冲突，并且如果修改路由，可以不用修改路由别名

![image-20260624192010070](./note04-第一个django项目以及django基础-路由.assets/image-20260624192010070.png)

## 2.2》路由反转，好处是在项目非常大的情况下，可以快速找到路由

![image-20260624192625963](./note04-第一个django项目以及django基础-路由.assets/image-20260624192625963.png)

## 演练：

![image-20260624194534604](./note04-第一个django项目以及django基础-路由.assets/image-20260624194534604.png)

## 注意2种路由反转的传参方式

![image-20260624195628962](./note04-第一个django项目以及django基础-路由.assets/image-20260624195628962.png)

## 运行结果

![image-20260624195727672](./note04-第一个django项目以及django基础-路由.assets/image-20260624195727672.png)

# 扩展，路由反转参考文档

# Django入门 · 路由反向解析和名称空间

## **Django中路由的名称空间和反向解析**

**Django中对不同的路由我们可以进行不同的命名，并且针对于多个App我们可以定义不同的名称空间(namespace)**

**项目结构:**

![img](https://pica.zhimg.com/v2-40edc71da0bfaf94459669e70c5ce3fe_1440w.jpg)

项目基本结构



## **1. 路由的基础命名(不附带命名空间)**

在对于单个App进行路由定义的时候，可能一个urls.py文件的定义就足够了我们的使用，但是对于多个App，我们可能通过 include方法，生成了多个子路由，通过每个App内单独的urls.py进行二次管理，所以此时，我们可以对路由进行命名，方便于我们对路由的快速调用。

**通过path(name参数)我们可以快捷的路由进行命名。**

**项目主文件夹/urls.py**

```python
from django.urls import path,include

urlpatterns = [
    path("user/", include('user.urls')), # 路由分发到user.urls中
]
```

**user/urls.py**

```python
from django.urls import path, include,re_path
import user.views

urlpatterns = [
    path("userlist/", user.views.user_list, name='userlist'), # 设置name为userlist
    re_path(r"userdetail/(?P<uid>\d*)", user.views.user_detail, name='userdetail'), # 设置name为userdetail
]
```

此时我们通过name的设置，已经让路由有了更加简单的"别名"，我们可以方便的使用"别名"去获取他的Url值。

## **2. 反向解析基础**

## **2.1 通过Python方法进行反向解析**

### **反向解析：顾名思义，通过别名，解析出来Url的原值**

**反向解析的用途**

**eg: 现在有很多很多个路由，几百个不同的路由，我们在访问其中一个路由的时候，需要让他跳转到另一个路由，那几百个路由那么复杂，我们不可能快读的找到对应的链接值，但是我们可以通过起的别名，反向解析出来URL，便于我们使用。**

**在Django中的反向解析一般有这几种:**

1. reverse 方法反向解析
2. reverse_lazy 方法反向解析
3. resolve_url 方法反向解析
4. redirect 反向解析并重定向
5. Django-HTML模板语法中反向解析动态生成Url

```python
# 在1.路由的基础命名中，我们定义了 user/userlist/ 的 name = 'userlist'
# 此时我们便可以通过调用reverse /reverse_lazy /resolve_url 传入"userlist" 获取到user/userlist/的值

#################

view.py

#################
from django.shortcuts import render, reverse, redirect,resolve_url # 导入包
from django.urls import reverse_lazy # reverse_lazy只在django.urls中存在,但是reverse, resolve_url在shortcuts和urls中都存在


def user_list(request):
    user_list = User.objects.all()
    return render(request, 'user_list.html', {"user_list": user_list})


def user_detail(request, uid):
    print(request.resolver_match.namespace)
    -> userdetail
    # request.resolver_match.namespace 用于获取当前访问的路由的名称空间
    
    print(reverse('userlist', )) # 获取 别名=userlist的原URL
    -> /user/userlist/
    print(reverse_lazy('userlist')) # reverse_lazy返回与reverse一样(一般在类视图使用,见后续解释)
    -> /user/userlist/
    print(resolve_url("userlist")) # resolve_url 不仅仅能返回 别名对应的Url 
    -> /user/userlist/
    print(resolve_url(user_list)) # 还可以通过传入视图方法/视图类进行返回
    -> /user/userlist/
    if not uid:
        return redirect('userlist') # 重定向到 别名userlist对应的路由
    user_info = User.objects.get(pk=uid)
    return render(request, "user_detail.html", {"user_info": user_info})

```



**但是，要注意，当前对Url进行的别名命名，其实都是 \*全局范围\* 生效的命名**

**也就是说，例如你在App1中定义了userlist这个链接，你就不能在App2中再起userlist，不然就会造成冲突！**

**所以这里我们需要引出命名空间的概念**



## **3. 路由命名空间**

**上面的路由基础命名，使用的名称空间都是全局的，这就导致了，我们不同App中不能够使用相同的名称**

**而Django为了方便区分，于是在命名的基础上，增加了命名空间的相关参数**



**项目主文件夹/ urls.py**

```python
# 命名空间主要针对于上层的命名重复问题,所以首先我们修改 项目主文件夹/ urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include('user.urls',namespace='user')), 
    # 设置user/域名下的所有的路由的命名名称空间都在user空间中
]
```

**user/urls.py (App下的urls)**

```python
from django.urls import path, include,re_path
import user.views

app_name = 'user' # 设置该urls的名称空间为user,此时下方定义的path都会在user名称空间中
urlpatterns = [
    path("userlist/", user.views.user_list, name='userlist'), # 设置名称为 userlist
    re_path(r"userdetail/(?P<uid>\d*)", user.views.user_detail, name='userdetail'), # 设置名称为userdetail
]

## 这里注意,虽然我们设置了名称为userlist，但是由于userlist在user的命名空间下
## 所以在实际调用过程中,user的名称实际为: user:userlist 
## 格式: [name:namespace]
```

**views.py**

```python
from django.shortcuts import render, reverse, redirect,resolve_url

def user_detail(request, uid):
    print(request.resolver_match.view_name)
    -> user:userdetail
    print(reverse('user:userlist', )) 
    -> /user/userlist/
    print(reverse_lazy('user:userlist')) 
    -> /user/userlist/
    if not uid:
        print(f'重定向')
        return redirect('user:userdetail',uid=2) 
    user_info = User.objects.get(pk=uid)
    return render(request, "user_detail.html", {"user_info": user_info})

```

**需要注意的是，当我们使用了命名空间对某个路由进行命名后，它的名字将不在全局名称空间中，所以我们命名后**

**可以使用user:userlist 来反向解析，但是不可以直接使用 userlist进行解析**

## **4. 反向解析传参**

## **4.1 函数反向解析传参**

reverse，reverse_lazy ，resolve_url，redirect的反向解析都支持传参

```python
# 例如我们定义了一个路由
re_path(r"userdetail/(?P<uid>\d*)", user.views.user_detail, name='userdetail')
# userdetail/<uid> -> uid参数将传入user.views.user_detail
# 此时我们如果反向解析到user.views.user_detail，那也需要传递参数

# 例如reverse:
reverse('user:userdetail',uid=10) # 关键字参数设置uid=10
redirect('user:userdetail',2) # 位置参数设置uid=2
redirect('user:userdetail',kwargs={"uid":2}) # kwargs传参
```

## **4.2 HTML模板语法反向解析传参**

```python
# 语法格式
## 不传参格式
{% url "Url名称空间:Url别名" %}
## 传参格式
{% url "Url名称空间:Url别名" 参数1 参数2%} # 不同参数之间有空格！！
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户列表</title>
</head>
<body>
    <h2>用户列表</h2>
    <ul>
        {% for user in user_list %} // user_list由Django - ORM返回
            <li>
                <a href="{% url "user:userdetail" user.id %}">姓名:{{ user.name }}</a> //反向解析userdetail并传入uid参数
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

## **5. 三种反向[解析函数](https://zhida.zhihu.com/search?content_id=231854948&content_type=Article&match_order=1&q=解析函数&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI1MjM2NzUsInEiOiLop6PmnpDlh73mlbAiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzE4NTQ5NDgsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.S8X_455_9pNtqqpf535xR4g3MRzfXv90t5kzXTbqmLo&zhida_source=entity)的区别，及用途**

## **5.1 reverse()**

- 接受一个 URL 名称作为参数，会根据该名称解析出对应的 URL，并返回解析后的 URL 字符串。
- 使用 `reverse()` 需要保证 Django 的 URL 配置已经加载，并且解析过程能够找到对应的 URL。
- **适用于在[视图函数](https://zhida.zhihu.com/search?content_id=231854948&content_type=Article&match_order=1&q=视图函数&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI1MjM2NzUsInEiOiLop4blm77lh73mlbAiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzE4NTQ5NDgsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9._MZ4pG7bCjcLp8l6uLUXk6mKPqlh3CS2bTKf-dw13vw&zhida_source=entity)、模板等地方进行 URL 反转。**

## **5.2 reverse_lazy()**

- `reverse_lazy()` 是 Django 的一个实用函数，类似于 `reverse()`，但它返回的是一个**延迟解析的对象**。
- 它接受一个 URL 名称作为参数，会根据该名称延迟解析出对应的 URL，并返回一个[代理对象](https://zhida.zhihu.com/search?content_id=231854948&content_type=Article&match_order=1&q=代理对象&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI1MjM2NzUsInEiOiLku6PnkIblr7nosaEiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzE4NTQ5NDgsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.UOa8m-UuIOB5-kkSVY8C0eLKS4hgwjZtJYncykoOC9s&zhida_source=entity)。
- `reverse_lazy()`**不会在初始化阶段尝试解析 URL**，只有在实际访问代理对象时，**才会触发 URL 解析。**
- **适用于在类视图等场景下，保证在实际访问视图时才会解析 URL，避免在启动时可能发生的错误。**
- 说白了，类视图把reverse换成这个，函数视图开发种，用reverse()就可以。

## **5.3 resolve_url()**

- 可以根据多种类型的参数进行解析，包括 URL 字符串、URL 名称、视图函数、类视图、对象的 `get_absolute_url()` 方法等。
- 适用于在视图中构建动态链接、进行重定向等场景。
- resolve_url不光可以解析字符串，例如你传一个函数，他也能给你解析出来，所以更加专业，但是一般用不到。
