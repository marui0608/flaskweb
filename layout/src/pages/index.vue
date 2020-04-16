<template>
  <div class="index-wrapper">
    <div class="index-left">
      <!-- 全部产品 -->
      <div class="index-left-block">
        <h2>全部产品</h2>
        <template v-for="product in productList">
          <h3>{{ product.title }}</h3>
          <ul>
            <li v-for="item in product.list">
              <a v-bind:href="item.url">{{ item.title }}</a>
              <span v-if="item.hot== true" class="hot-tag">HOT</span>
            </li>
          </ul>
          <!-- <div class="hr" v-if="product.title=='PC产品'"></div> -->
          <div v-if="!product.last" class="hr"></div>
        </template>
      </div>
      <!-- 最新消息 -->
      <div class="index-left-block lastest-news">
        <h2>最新消息</h2>
        <ul>
          <li v-for="item in newsList">
            <a v-bind:href="item.url">{{ item.title }}</a>
          </li>
        </ul>
      </div>
    </div>
    <div class="index-right">
      <slider-component></slider-component>
      <div class="index-boader-list">
        <div class="index-boader-item" v-for="board in boardList">
          <div class="index-boader-item-inner">
            <h2>{{ board.title }}</h2>
            <p>{{ board.description }}</p>
            <div class="index-boader-button">立即购买</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from 'axios'    // 第一步引入
import SliderComponent from '../components/sliderComponent'
export default {
  components:{
    SliderComponent
  },
  mounted() {                // 一般都写在这个里面
    axios.get('api/getNewsList').then((res) => {
      console.log(res)
      this.newsList = res.data.list
    })
    .catch((error) => {
      console.log(error)
    }
    ),
    axios.get('api/getProductList').then((res) => {
      console.log(res)
      this.productList = res.data
    })
    .catch((error) => {
      console.log(error)
    }
    ),
    axios.get('api/getBoardList').then((res) => {
      console.log(res)
      this.boardList = res.data
    })
    .catch((error) => {
      console.log(error)
    }
    )
  },
  data() {
    return {
      newsList: [],
      productList: null,
      boardList: null,
    }
  }
};
</script>


<style scoped>
.index-wrapper {
  width: 1200px;
  display: flex;
}
.index-left {
  width: 300px;
}
.index-left-block {
  margin: 15px;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0 0 1px #dddddd; /* 盒子阴影 */
}
.index-left-block .hr {
  border-bottom: 1px solid #e2e2e2;
  margin: 20px 0;
}
.index-left-block h2 {
  background: #4fc08d;
  color: #ffffff;
  padding: 10px 15px;
  margin-bottom: 20px;
  cursor: pointer;
}
.index-left-block h3 {
  color: #222;
  font-weight: bolder;
  padding: 0 15px 0 15px;
  cursor: pointer;
}
.index-left-block ul {
  padding: 10px 15px;
}
.index-left-block ul li {
  padding: 5px 10px;
}
.index-right {
  width: 900px;
  margin-top: 15px;
}
.index-boader-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 15px;
}
.index-boader-item {
  width: 400px;
  height: 150px;
  background: #ffffff;
  box-shadow: 0 0 1px #ddd;
  border-radius: 0 0 10px 10px;
  margin-bottom: 20px;
  padding: 20px;
}
.index-boader-item-inner {
  height: 130px;
  padding-left: 180px;
  background-image: url("../assets/logo.png");
  background-repeat: no-repeat;
  background-size: 25%;
}
.index-boader-item-inner h2{
  font-size: 18px;
  font-weight: bolder;
  color: #000;
  margin-top: 15px;
}
.index-boader-item-inner p {
  margin-bottom: 15px;
}
.index-boader-button {
  width: 80px;
  height: 40px;
  background: #4fc08d;
  color: white;
  border-radius: 5px;
  text-align: center;
  line-height: 40px;
  cursor: pointer;
}
.hot-tag {
  color: #ffff;
  background: purple;
  font-size: 13px;
  cursor: pointer;
}
</style>