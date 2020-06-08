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

​	this 是DOM对象

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

# day08
1. jQuery工厂函数：$()
	用于加工对象，获取元素节点
	
2. 选择器：id 标签 类 群组  后代/子代  相邻兄弟/通用兄弟,**过滤选择器**
	过滤选择器：配合其它选择器，设置选择条件。
```javascript
   city=$('#city').find('option:selected').text();
   //在'#city'中找到属性为selected的option
```
3. 获取或设置标签属性
    attr():获取和设置写在标签内部的属性的值,若没写入过，会报错.
    prop():获取和设置标签原本自带的属性的值，若没有设置，则为undefined.



# Day09
1.jQuery   redy/load

原生onload事件不能重复书写，会产生覆盖问题；jquery中对事件做了优化,可以重复书写ready方法,依次执行

```javascript
// ready 这个方法只是在页面所有的DOM加载完毕后就会触发

// 方式1
$(function(){ 
// do something 
}); 

// 方式2
$(document).ready(function(){ 
//do something 
});

// 方式3
$().ready(function(){ 
//do something 
});


// load 这个方法会等到页面所有内容加载完毕后才会触发

$(window).load(function() { 
alert("hello"); 
}); 
```

# Day10

- HTML
	表单：get/post
	get:get: http://www,tmooc.cn?key=value&key=value 
	post:post: key=value&key=value
	表单控件:属性（name,value）

- CSS:排版布局与样式美化
```
选择器：id，类，标签，群组，后代子代，伪类
优先级：权重	

display: 
block: 独占一行，可手动设置宽高，默认100%
inling: 可以和其它内容一行显示，但是宽高由内容决定
inling-block: 可共行,可手动设置宽高
none: 隐藏元素
内容溢出：overflow:auto/hidden
边框圆角：border-radius

外边距溢出：子元素外边距作用在了父元素(无border)身上,会把父元素带着一起移动
解决：给父元素加边框或加上内边距

浮动和定位：摆脱元素在页面排列的默认方式
浮动：解决块元素的水平排列
定位：结合偏移属性调整元素的显示位置
								
```
- JS：页面交互
```
变量、常量、数据类型、运算符号
隐式转换：字符串在做+运算时，会把其它类型转换为字符串
						其它情况下，一律转换为number
						在逻辑判断时：字符串之间的比较-->比较Unicode码
														其它情况，一律转换为number,如果无法转换，则转换为NaN，结果一律为False
语句：if、switch、while、do-while
函数（传参）、匿名函数、作用域
声明提前： 
					   在js执行时，会把声明提前到最上方
					   变量只会提前变量名，赋值在后面进行
						函数会将内容一起提前
内置方法：
					 对象{'key':'value'} 、数组[]
					 for(index in obj){}   index--->下标
字符串，正则表达式对象(RegExp，new RegExo('reg','ig'), /reg/ig   )
随机数，时间对象(new Date())-->倒计时

BOM对象(Browser Object Model):
						定时器:周期性定时器，一次性定时器
JS是单线程执行，但是JS代码在执行过程中，还有其它线程的参与：
						JS引擎-->执行JS代码
							↑↑↑↑↑协助
	事件触发线程     定时器触发线程     HTTP异步线程
		
history     location
location.hrf = 地址-->页面跳转

前段数据获取思路：
		location.hrf获取地址栏内容，再进行分割

DOM节点(Document Object Model)
jQuery....

```


