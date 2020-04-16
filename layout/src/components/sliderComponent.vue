<template>
    <div class="slider-wrapper" @mousemove="clearInv" @mouseout="runInv">     <!-- 绑定事件 鼠标 进入、出去 -->
        <!-- 五张轮播图 -->                <!-- 清除定时   运行定时 -->
        <div class="slider-item item1">1</div>
        <div class="slider-item item2">2</div>
        <div class="slider-item item3">3</div>
        <div class="slider-item item4">4</div>
        <div class="slider-item item5">5</div>

        <!-- 下方圆点 -->
        <ul class="slider-dots">
            <li>&lt;</li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li>&gt;</li>
        </ul>
    </div>
</template>


<script>
export default {
    props:{
        inv:{
            type:Number,
            default:1000
        }
    },
    data() {
        return {
            
        }
    },
    methods: {
        runInv(){
            // 设置定时器
            setInterval(()=>{
                // 开启定时器

            },this.inv)
        },
        clearInv(){

        }
    },

}
</script>


<style scoped>
    .slider-wrapper{
        width: 900px;
        height: 500px;
        background: red;
        position: relative;
    }
    .slider-item{
        width: 900px;
        height: 500px;
        text-align: center;
        line-height: 500px;
        font-size: 40px;
        position: absolute;     /* 重叠定位 */
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
    .item5{
        z-index: 60;
    }
    .slider-dots {
        position: absolute;
        right: 60px;
        bottom: 20px;
    }
    .slider-dots li{
        width: 20px;
        height: 20px;
        border-radius: 70%;
        background: black;
        color: white;
        text-align: center;
        line-height: 20px;
        float: left;
        margin: 0 10px;
        opacity: 0.6;    /* 透明度 */
    }
</style>