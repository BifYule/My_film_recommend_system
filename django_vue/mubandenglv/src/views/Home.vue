<template>

<el-container>
  <el-header>
    <div class="ui top fixed pointing menu " style="background-color:rgba(100,100,100,0.9);">
        <!-- 顶层菜单 -->
        <img class="ui medium circular image" style="width:50px;height:50px;margin:10px 20px 0 0;" src="./img/image/logo/pumpkin.jpg" @click="to_homepage()">
        

        <a class="item font-set active" style="color:white;width:80px;height:45px;margin: 10px 10px 0px 0px;"> 主页 </a>
        
        <a class="item font-set" style="color:white;width:115px;height:45px;margin:10px 10px 0px 0px;" @click="to_filmanalysis()"> 电影分析 </a>

        <a class="item font-set" style="color:white;width:80px;height:45px;margin:10px 10px 0px 0px;" @click="to_classify()">分类 </a>
        

        <div class="right menu" >
            <div class="ui search right" style="margin:10px 20px 0px 0px;">
                <div class="ui icon input">
                    <input class="prompt" type="text" v-model="movie" @keyup.enter="searchmovie" placeholder="搜索">
                    <i class="search icon"></i>
                </div>
                <div class="results"></div>
            </div>
        </div>
        
    </div>
    
  </el-header>



  <el-main  style="background-color:#afb5c1;margin:0;">

        <div>
            <!-- 主体部分 -->
                <!-- 照片显示 -->
                
                <div>     

                  <img :src="photos[now_p].COVER" style="width: 1000px;height:550px; margin-left: 10%;cursor:pointer;"  @click="to_detailpage(photos[now_p].NAME)" alt="">
           
                  <div style="float:right;margin-right:8%;">
                    <button @mouseover="get_url(0)" @click="to_detailpage(photos[type[0].t].NAME)">{{ photos[0].NAME }}</button><p></p>
                    <button @mouseover="get_url(1)" @click="to_detailpage(photos[type[0].t+1].NAME)">{{ photos[1].NAME }}</button><p></p>
                    <button @mouseover="get_url(2)" @click="to_detailpage(photos[type[0].t+2].NAME)">{{ photos[2].NAME }}</button><p></p>
                    <button @mouseover="get_url(3)" @click="to_detailpage(photos[type[0].t+3].NAME)">{{ photos[3].NAME }}</button><p></p>
                    <button @mouseover="get_url(4)" @click="to_detailpage(photos[type[0].t+4].NAME)">{{ photos[4].NAME }}</button><p></p>
                    <button @mouseover="get_url(5)" @click="to_detailpage(photos[type[0].t+5].NAME)">{{ photos[5].NAME }}</button><p></p>
                    <button @mouseover="get_url(6)" @click="to_detailpage(photos[type[0].t+6].NAME)">{{ photos[6].NAME }}</button><p></p>
                    <button @mouseover="get_url(7)" @click="to_detailpage(photos[type[0].t+7].NAME)">{{ photos[7].NAME }}</button><p></p>
                    <button @mouseover="get_url(8)" @click="to_detailpage(photos[type[0].t+8].NAME)">{{ photos[8].NAME }}</button><p></p>
                    <button @mouseover="get_url(9)" @click="to_detailpage(photos[type[0].t+9].NAME)">{{ photos[9].NAME }}</button><p></p>

                  </div>
                </div>
                <!-- <img src="./img/beach.jpg" style="width:1200px;height:700px" alt=""> -->
                <!-- <a href="">
                         <img :src="imgArr[num1]" class="Topimg" style="text-align:center;" alt="physics" >
                </a>  -->

        <!-- 推荐  剧情  爱情  动作 -->
        <div style="width:90%;height:400px;margin:10px 50px 0 8%;">
              <p class="font-set" style="margin:0 0 0 30px;font-size:18px;">猜你喜欢</p>

                <div style="height:150px;float:right;margin:65px 70px 0 0;">
                    <el-button @click="clicklike_pre(type[1].t,1)" class="button_block"  style="margin-top:53%;"><i class="el-icon-caret-top"></i></el-button>
                    <p></p>
                    <el-button @click="clicklike_next(type[1].t,1)" class="button_block"><i class="el-icon-caret-bottom"></i></el-button>
                </div>

                <div style="margin:10px 20px 0 30px;float:left;cursor:pointer;text-align: center;"  v-for="(item,i) in 5" >
                    <img :src="photos[type[1].t+i].COVER" alt="" @click="to_detailpage(photos[type[1].t+i].NAME)">
                    <p>{{ photos[type[1].t+i].NAME}}</p>     
                </div>
           
        </div>
          
        <div style="width:90%;height:400px;margin:10px 50px 0 8%;" >
              <p class="font-set" style="margin:0 0 0 30px;font-size:18px;">动作电影</p>
   
                <div style="height:150px;float:right;margin:65px 70px 0 0;">
                    <el-button @click="clicklike_pre(type[2].t,2)" class="button_block" style="margin-top:53%;"><i class="el-icon-caret-top"></i></el-button>
                    <p></p>
                    <el-button @click="clicklike_next(type[2].t,2)" class="button_block" ><i class="el-icon-caret-bottom"></i></el-button>
                </div>

                <div style="margin:10px 20px 0 30px;float:left;cursor:pointer;text-align: center;"  v-for="(item,i) in 5" >
                    <img :src="photos[type[2].t+i].COVER" alt="" @click="to_detailpage(photos[type[2].t+i].NAME)">
                    <p>{{ photos[type[2].t+i].NAME}}</p>     
                </div>
      
        </div>

        <div style="width:90%;height:400px;margin:10px 50px 0 8%;" >
              <p class="font-set" style="margin:0 0 0 30px;font-size:18px;">剧情电影</p>
             
                <div style="height:150px;float:right;margin:65px 70px 0 0;">
                    <el-button @click="clicklike_pre(type[3].t,3)" class="button_block" style="margin-top:53%;"><i class="el-icon-caret-top"></i></el-button>
                    <p></p>
                    <el-button @click="clicklike_next(type[3].t,3)" class="button_block"><i class="el-icon-caret-bottom"></i></el-button>
                </div>

                <div style="margin:10px 20px 0 30px;float:left;cursor:pointer;text-align: center;"  v-for="(item,i) in 5" >
                    <img :src="photos[type[3].t+i].COVER" alt="" @click="to_detailpage(photos[type[3].t+i].NAME)">
                    <p>{{ photos[type[3].t+i].NAME }}</p>     
                </div>
          </div>


          <div style="width:90%;height:400px;margin:10px 50px 0 8%;" >
              <p class="font-set" style="margin:0 0 0 30px;font-size:18px;">爱情电影</p>

                <div style="height:150px;float:right;margin:65px 70px 0 0;">
                    <el-button @click="clicklike_pre(type[4].t,4)" class="button_block" style="margin-top:53%;"><i class="el-icon-caret-top"></i></el-button>
                    <p></p>
                    <el-button @click="clicklike_next(type[4].t,4)" class="button_block"><i class="el-icon-caret-bottom"></i></el-button>
                </div>

                <div style="margin:10px 20px 0 30px;float:left;cursor:pointer;text-align: center;"  v-for="(item,i) in 5" >
                    <img :src="photos[type[4].t+i].COVER" alt="" @click="to_detailpage(photos[type[4].t+i].NAME)">
                    <p>{{ photos[type[4].t+i].NAME}}</p>     
                </div>
                  

          </div>
        </div>



  </el-main>
</el-container>
    
</template>

<!-- ************************** -->

<script>


export default({
            name:'top',
            data(){
              return {

                movie:'',

                now_p:0,
                //热门，推荐，剧情，爱情，动作
                type:[
                    {t:0},{t:10},{t:20},{t:30},{t:40}
                ],
                type2:[
                    {t:0},{t:10},{t:20},{t:30},{t:40}
                ],

                photos:[
                ],
                
            }
            },
            mounted () {             //打开页面时调用里面的函数
                this.init();
            },  
            
            methods:{

                init(){
                    console.log(1112222)
                    this.$http.get('http://127.0.0.1:8000/init/init_data',{ params:{ NUM:50 }},{
                            emulateJSON:true})
                    .then((response) => {             

                    var res = JSON.parse(response.body) 
                    console.log(res)

                    for (var i=0;i<res.length;i++) {                   
                        // console.log(i,"fields",res[i]['fields'])
                        this.photos.push(res[i]['fields'])
                    }
                    // console.log(this.photos)

                    if (res.error_num === 0) {
                        console.log('success____'+res)
                    } else {
                        console.log('error____'+res)
                    }
                    });
                }, 
                searchmovie(){
                    this.$http.get('http://127.0.0.1:8000/sos/sos_data',{ params:{'NAME':this.movie}},{
                    emulateJSON:true})
                        .then((response) => {   

                            var res = JSON.parse(response.body)  

                            console.log(res[1])
                            console.log(res)
                            this.to_detailpage(res[0]['fields'].NAME)

                            
                        })
                },
                to_filmanalysis(){
                    this.$router.push("Film_analysis")
                },
                to_detailpage(name){
                    this.$router.push("Detailpage")
                    this.$root.movie_name = name
                },
                to_classify(){
                    this.$router.push("Classification")
                },
                get_url(n){
                    this.$data.now_p = n
                }
                ,

                clicklike_pre(num,n){

                    if(num > this.type2[n].t){
                        this.$data.type[n].t -= 5
                    }else{
                        console.log("到头了！")
                    }  
                },
                clicklike_next(num,n){

                    if(num < this.type2[n].t + 5){
                        this.$data.type[n].t += 5
                    }else{
                        console.log("到头了！")
                    }
                },

                }
                
            }
            
        )
    


</script>

<!-- ************************** -->

<style>

    body {
          padding: 0;
          margin: 0;
          width: 100%;  
          display: table;
    }
 
    a:hover {
          font-size: 18px;
          text-decoration: underline;
    }

    .font-set {
          font-size:17px;
          font-family:"KaiTi";
          font-weight:normal;
    }
    .block_img{
          width: 200px;height:150px;
          margin-left:30px;
          cursor:pointer;
    }

    button{
        width: 160px;height:40px;
        text-align: center;
        background-color: #afb5c1;
        color: white;
        font-size: 18px;
        border-style: none;
        cursor:pointer
    }
    /* button:hover{
        font-size:23px;
    } */

    .button_block{
        width:50px;
        height:40px;
        cursor:pointer
    }
    .block_img:hover{
        transform:scale(1.2);
    }
    img{
         width: 189px;height:266px;
    }
</style>


