---
[toc]


# 第三阶段 WEB

- 前端：HTML+CSS+JavaScript    

- 后端：Django+数据库技术+前端+后端交互技术+项目  



## 项目开发阶段：
UI（User Interface）界面设计---->前端开发/后端开发---->测试----->运维



# Day01
课外练习：搜索如何修改导航栏图表

# Day02
- 清除列表默认格式
```css
     ul,ol,li{
            /* 清除列表默认样式 */
            margin: 0;
            padding: 0;
            list-style: none;
        }
```

- 选择器全中:
	一般来说,<body>里的最外层标签一般都要加id属性,以提高优先级,避免冲突
	
	```css
	<-- div#header+tab -->
	<div id="header"></div>
	```
	
- 标签分类及嵌套
   - 将元素设置为块元素
   ```css
   span{
    width: 200px;
    height: 200px;
    background-color: blue;
    /* 將元素設置成块元素 */
    display: block;
}
   ```
   
   - diplay:转换元素类型

- 字体尺寸
   - 按%设置尺寸(宽度),会根据窗口大小变化而变化(可以通过自适应框架进行设置)
   - html body 默认没有高度

# Day05(js)

- JS存在声明提前：
   1. 全局的变量和函数在声明时，会进行声明提前。
   2. 变量会将变量名提前到最上方，值留在原地。
   3. 函数名会携带函数的内容一起提前到最上方。

```javascript
  <button id='btn'>
        click me!
    </button>
    <script>
        console.log(btn)//undefined
        console.log(sayHello)//function
        var btn=document.getElementById('btn')
        // console.log(btn.onclick)
        // sayHello定义在下边...可以在上边找到---->声明提前
        console.log(sayHello);
        btn.onclick=sayHello;
        function sayHello() {
            alert('hello world');
        }
    </script>
```

# Day06

1. let声明:let和for一起使用，会将for循环当做一个独立的代码块，let声明的变量只在当前代码块中（for,function），可以起到类似闭包保留变量的作用
```javascript
    <script>
        var lis=document.getElementsByTagName('li')
        for(let i=0;i<lis.length;i++){
            lis[i].onclick=function(){
                alert(lis[i].innerText);
            }
        }
    </script>
```

2.this:指向对象本身，类似python中的self

```javascript
    <script>
        var lis=document.getElementsByTagName('li');
        for(var i=0;i<lis.length;i++){
            lis[i].onclick=function(){
                alert(this.innerText);
            }
        }
    </script>
```

3. JSON对象写法：两种无本质区别，key加引号适用与前后端数据交互

```javascript
var qtx={name:'qtx',age:18};//<--JSON对象
  var obj={
            'name':'Tom',
            'age':19
        };
```

4.可以用JSON.stringify将对象转换为字符串，以便于将数据发送给服务端。

```javascript
var res=JSON.stringify(qtx);
        console.log(res);//-->'{"name":"qtx","age":18}'
```

5.JSON.parse可以将符合格式的字符串转换为对象，以便于在接受到服务端数据之后的数据处理

```javascript
  var json_obj=JSON.parse(json_res);
        console.log(json_obj);
//Object
//age: 18  name: "qtx"
//__proto__: Object
```

