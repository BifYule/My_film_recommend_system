<template>
<el-container>

<el-header>
    <div class="ui top fixed pointing menu " style="background-color:rgba(100,100,100,0.9);">
        <!-- 顶层菜单 -->
        <img class="ui medium circular image" style="width:50px;height:50px;margin:10px 20px 0 0;" src="./img/image/logo/pumpkin.jpg" @click="to_homepage()">
        

        <a class="item font-set active" style="color:white;width:80px;height:45px;margin: 10px 10px 0px 0px; " @click="to_homepage()"> 主页 </a>
        
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


    <el-main style="background-color:#afb5c1;margin:0;">
        <div style="width:84%;margin:auto;">

            <div style="width:60%;height:400px;float:right; margin-right:200px ;">
                <!-- <div style="width:150px;height:100px;float:right;font-size: 25px; margin:30px 100px 0 0;font-weight :600;">
                    评分:9.8
                </div> -->
                <div style="width:150px;height:100px;float:right;font-size: 25px; margin:30px 100px 0 0;font-weight :600;color: black;">
                    <p style="font-size:15px;margin:0 20% 0 30%;">豆瓣评分:</p><div style="float:left;font-weight :600;margin-left: 40%;font-size:27px;">{{score}}</div>
                </div>

                <p class="word">电影名:{{name }}</p>
                <p class="word">上映时间:{{release_date}}</p>        
                
                <div>
                    <div   style="width:300px;height:40px; background-color:#afb5c1;color:black">主演:{{actors.substr(0, 40)}}</div>
                    <div  v-if="actors.length>=46&isShow" style="width:300px;height:100px;background-color:#afb5c1;color:black">{{actors.substr(40, actors.length)}}</div>
                    <a  style="font-size:14px;" class="button" @click="toggleIsShow">更多</a>
                </div>
                

                <p class="word">语言:{{language }}</p>
                <p class="word">时间长:{{time_long }}分钟</p> 
                <p class="word">类型:剧情 / 家庭</p>
                

                <!-- 评分 -->
                <p style="font-size:20px;color:black">评分:</p>
                <div @click="save_evaluate()">
                    <el-rate
                    v-model="value"
                    show-text>
                    </el-rate>
                </div>


                <!-- <div class="ui divider"></div> -->
            </div>
            

            
            
            <img :src="photo_url" style="width:270px;height:380px;margin-right:0;" alt="电影图片">
           

            <div  style="width:90%;height:400px; margin:50px 0 40px 0;">
                <div style="width:90%;height:200px;">
                    <p class="word">简介: {{ storyline }}</p>
                </div>
            </div>  
        

        </div>

    </el-main>

</el-container>

</template>


<script>


    export default{
        name:'Detailpage',
        data(){
            return{
                // 评分绑定的数据
                value: null,   
                
                name:null,
                score:null,
                photo_url:null,
                release_date:null,
                actors:null,
                language:null,
                time_long:null,
                director:null,
                storyline:null,
                movie_id:null,
                isShow:false,
                // txt:"朱一龙/杨恩又/王戈/刘陆/罗京民/吴倩/郑卫莉/陈创/李春嫒/钟宇升/刘亚津/小爱/韩延朱一龙/杨恩又/王戈/刘陆/罗京民/吴倩/郑卫莉/陈创/李春嫒/钟宇升/刘亚津/小爱/韩延朱一龙/杨恩又/王戈/刘陆/罗京民/吴倩/郑卫莉/陈创/李春嫒/钟宇升/刘亚津/小爱/韩延"
            
            }
        },
        mounted () {
            this.get_data();
            this.get_evaluate();
        },
        
        methods: {
            toggleIsShow:function(){
                     this.isShow = !this.isShow
                 },
            to_homepage(){
                this.$router.push("Home")
            },
            to_filmanalysis(){
                this.$router.push("Film_analysis")
            },
            to_classify(){
                    this.$router.push("Classification")
            },
            save_evaluate(){
                this.$http.get('http://127.0.0.1:8000/save/save_evaluate',{ params:{ MOVIE_ID:this.movie_id,MOVIE_NAME:this.$root.movie_name, USER_NAME:this.$root.user_name,SCORE:this.value}},{
                            emulateJSON:true})
                    .then((response) => {             
                    
                    });
            },
            get_evaluate(){
                this.$http.get('http://127.0.0.1:8000/getd/get_evaluate',{ params:{ MOVIE_ID:this.movie_id,MOVIE_NAME:this.$root.movie_name, USER_NAME:this.$root.user_name,SCORE:this.value}},{
                            emulateJSON:true})
                    .then((response) => {        
                    console.log("test begin")

                    var res = JSON.parse(response.body) 
                    console.log("detail:",res)
                    this.value = res[0]['fields'].SCORE

                    console.log("value值:",this.value)

                    if (res.error_num === 0) {
                        console.log('success____'+res)
                    } else {
                        console.log('error____'+res)
                    }
                    });    
            },
            get_data(){
                this.$http.get('http://127.0.0.1:8000/getd/get_data',{ params:{ NAME:this.$root.movie_name}},{
                            emulateJSON:true})
                    .then((response) => {             
                    console.log('detail:',response)
                    
                    var res = JSON.parse(response.body) 
                    // console.log('res:',res)
                    // console.log(res.length)              //得到长度
                    // console.log(res[0]['fields'])  //0是第几个电影的数据，pk是id,fields是其他字段，用 .字段名 获取


                    this.name = res[0]['fields'].NAME
                    this.actors = res[0]['fields'].ACTORS
                    this.director = res[0]['fields'].DIRECTORS
                    this.score = res[0]['fields'].DOUBAN_SCORE
                    this.language = res[0]['fields'].LANGUAGES
                    this.release_date = res[0]['fields'].RELEASE_DATE
                    this.time_long = res[0]['fields'].MINS
                    this.storyline = res[0]['fields'].STORYLINE
                    this.photo_url = res[0]['fields'].COVER,
                    this.movie_id = res[0]['fields'].MOVIE_ID

                    if (res.error_num === 0) {
                        console.log('success____'+res)
                    } else {
                        console.log('error____'+res)
                    }
                    });
            }
        }
    }
</script>


<style>
    body {
        padding: 0;
        margin: 0;
        width: 100%;

    }
    .button{
        text-decoration: none;
        background-color:#afb5c1;
        margin:0 0 3px 40%;
        cursor:pointer;
        color:black
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
          width: 189px;height:266px;
          margin-left:30px;
    }
    .word{
        font-size: 16px;
        /* width: 100%; */
        overflow: hidden;
        color: black;
    }
</style>


