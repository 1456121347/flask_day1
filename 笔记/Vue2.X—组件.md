# Vue2.X—组件

## 一、组件

1. **组件是Vue项目中拥有自己作用域，数据，方法的特殊部分，项目中的组件可以重复使用**

2. **创建组件需要三步：**

   ```
   创建组件： var ItemsComponents = Vue.extend({ })
   
   注册组件：Vue.component('items-component',ItemsComponents)
   
   使用组件：<'items-component></'items-component>
   ```

   注意：Vue2.X规范的写法：

   ```
   Vue.component('items-component',{template:'<h1> Hello </h1>'})
   ```

3. **vue 中的组件**

   vue init webpack component-demo

   通过template 标签在HTML声明模板

4. **组件中的data和el属性**

   ```
   <template id="hello">
     <h1>hello</h1>
   </template>
   //vue中要求用函数的形式来声明这些属性
   Vue.component("hello-component",{
     el:function(){
       return "#hello";
     },
     data:function(){
       return {
         msg:'hello'
    }
     }
   })
   ```

5. **组件的作用域（父子组件进行数据传递）**

   组件都有自己的独立的作用域，而且不会被其他组件访问到，但是，项目中全局作用域可以被所有注册过的组件访问。

   在组件内不能使用父作用域的数据，如果要是用父作用域的数据的话，指出到底哪个组件的父级数据属性可以被访问，

   - 通过props属性传递，
   - 用v-bind把他们绑定到组件上

1. **组件嵌套**

## 二、单文件组件（.vue）

1. 单文件组件，就是以.vue结尾的文件，使用vue-cli生成
2. 一个Vue单文件组件由3个部分组成：
   - template HTML模板
   - script JavaScript代码
   - style CSS样式
1. 新建一个simple文件夹，cd simple , vue init webpack-simple，一路回车即可
4. 下载路由代码 npm install vue-router --save