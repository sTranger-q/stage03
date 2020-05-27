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
