<template>
  <div class="con" id="app">
    <h2>我的购物车清单</h2>
    <div class="inp_shop">
      <input class="js-new" type="text" placeholder="输入你想购买的物品">
      <span class="btu">
        <button class="js-add btn btn-default">添加到购物车</button>
      </span>
    </div>
    <ul>
      <li>
        <div class="checkbox">
          <label for>
            <input class="js-item" type="checkbox">苹果
          </label>
        </div>
      </li>
      <li>
        <div class="checkbox">
          <label for>
            <input class="js-item" type="checkbox">香蕉
          </label>
        </div>
      </li>
      <li>
        <div class="checkbox">
          <label for>
            <input class="js-item" type="checkbox">榴莲
          </label>
        </div>
      </li>
    </ul>
    <div class="footer">
      <span>改变你的标题</span>
      <input type="text" class="js-change" placeholder="我的购物车清单">
    </div>
  </div>
</template>
<script>
</script>
<style>
.con{
  width: 40%;
  margin: 1oopx auto;
}
ul{
  border: 1px solid black;
  margin-top: 20px;
}
ul li{
  list-style-type: none;
}
.removed{
  color: gray;
}
.removed label{
  text-decoration: line-through;
}
</style>
