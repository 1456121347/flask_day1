<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <!-- 四张轮播图 -->
        <div v-show="newIndex === index" class="slider-item" v-bind:class="['item' +[index+1]]" v-for="(item,index) in sliderImgList" v-bind:key="index">
            <a href="">
                <img v-bind:src="item" style="width:900px;height:500px;" alt="">
            </a>
        </div>
        <!-- 左右<> 按钮 -->
        <a v-on:click="preHandler" class="btn pre-btn" href="javascript:void(0)">&lt;</a>
        <a v-on:click="nextHandler" class="btn next-btn" href="javascript:void(0)">&gt;</a>
        <!-- 下方圆点 -->
        <ul class="slider-dots">
        
            <li v-on:click="clickDots(index)" v-for="(item,index) in sliderImgList" v-bind:key="index">{{ index+1 }}</li>
           
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            newIndex:0,
            sliderImgList:[
                require('../assets/pic1.jpg'),
                require('../assets/pic2.jpg'),
                require('../assets/pic3.jpg'),
                require('../assets/pic4.jpg'),

            ]        
        }
    },
    methods: {
        clickDots(index){
            this.newIndex = index

        },
        preHandler(){
            this.newIndex --;
            if(this.newIndex < 0){
                this.newIndex = 3
            }
            console.log(this.newIndex);

        },
        nextHandler(){
            this.autoPlay()

        },
        autoPlay(){
            this.newIndex++;
            if(this.newIndex > 3){
                this.newIndex = 0
            }

        },
        runInv(){
            this.invId = setInterval(this.autoPlay,2000)
        
        },
        clearInv(){
            clearInterval(this.invId)
        }
    },
    created() {
        this.runInv()
    },
}
</script>

<style scoped>
    .slider-wrapper{
        width: 900px;
        height: 500px;
        /* background:blueviolet; */
        position: relative;
    }
    .slider-item{
        width: 900px;
        height: 500px;
        text-align: center;
        line-height: 500px;
        font-size: 40px;
        position: absolute;
    }
    .item1{
        z-index: 100;
    }
    .item2{
        z-index: 90;
    }
    .item3{
        z-index: 80;
    }
    .item4{
        z-index: 70;
    }
    .slider-dots{
        position: absolute;
        right: 50px;
        bottom: 20px;
        z-index: 200;
    }
    .slider-dots li{
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background:#000000;
        color: #ffffff;
        text-align: center;
        line-height: 20px;
        float: left;
        margin: 0 10px;
        /* 透明度 */
        opacity: 0.6;
        /* 点击小手 */
        cursor: pointer;
    }
    .btn{
        display: inline-block;
        width: 50px;
        height: 50px;
        color: #ffffff;
        /* background: #000000; */
        font-size: 40px;
        text-align: center;
        line-height: 50px;
        position: absolute;
        top: 50%;
        margin-top: -25px;
        z-index: 300;
        opacity: 0.6;
        
    }
    .pre-btn{
        left: 5px;
    }
    .next-btn{
        right: 5px;
    }
</style>