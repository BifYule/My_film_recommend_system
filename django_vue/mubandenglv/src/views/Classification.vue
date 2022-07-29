<template>
    <el-container>
<el-header>
    <div class="ui top fixed pointing menu " style="background-color:rgba(100,100,100,0.9);">
        <!-- 顶层菜单 -->
        <img class="ui medium circular image" style="width:50px;height:50px;margin:10px 20px 0 0;" src="./img/image/logo/pumpkin.jpg" @click="to_homepage()">
        

        <a class="item font-set" style="color:white;width:80px;height:45px;margin: 10px 10px 0px 0px;" @click="to_homepage()"> 主页 </a>
        
        <a class="item font-set" style="color:white;width:115px;height:45px;margin:10px 10px 0px 0px;" @click="to_filmanalysis()"> 电影分析 </a>

        <a class="item font-set active" style="color:white;width:80px;height:45px;margin:10px 10px 0px 0px;">分类 </a>
        

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
        <div style="margin:50px 50px 0 8%;">
            <p>全部类型: </p>
            <!-- 更改分类后，初始化变量 -->
            <div  @click="get_classify()" v-for="(item,i) in list" style="float:left;">            
                <el-radio-group v-model="radio">
                <el-radio-button :label="item" ></el-radio-button>

                </el-radio-group>
            </div>
        </div>

       

    <div style="width:90%;height:1400px;margin:80px 0 0 5%;">
            <div style=" margin:50px 20px 0 40px;float:left;cursor:pointer;text-align: center;"  v-for="(item,i) in list2" >
                <img :src="photos[item].COVER" alt="" @click="to_detailpage(photos[item].NAME)">
                <p >{{ photos[item].NAME}}</p>     
            </div>
        
 
            <div style=" margin:50px 20px 0 40px;float:left;cursor:pointer;text-align: center;" v-for="(item,i) in list3">
                <img :src="photos[item].COVER"  alt="" @click="to_detailpage(photos[item].NAME)">  
                <p >{{ photos[item].NAME}}</p>   
            </div>
    

            <div  style=" margin:50px 20px 0 40px;float:left;cursor:pointer;text-align: center;"  v-for="(item,i) in list4">
                <img :src="photos[item].COVER" alt="" @click="to_detailpage(photos[item].NAME)">  
                <p >{{ photos[item].NAME}}</p>   
            </div>


            <div  style=" margin:50px 20px 0 40px;float:left;cursor:pointer;text-align: center;" v-for="(item,i) in list5">
                <img :src="photos[item].COVER"  alt="" @click="to_detailpage(photos[item].NAME)">     
                <p >{{ photos[item].NAME}}</p>
            </div>
    </div>

    <div style="margin:20px 0 200px 350px;">
        <el-pagination
             background
             :page-size="pageSize"
             :pager-count="16"
             layout="prev, pager, next"
             :total="totalnum"
             @current-change="pager"
         >
         </el-pagination>
    </div>

    </el-main>
    </el-container>
</template>


<script>
export default{

    data(){
        return{
            radio:'剧情',
            totalnum:192,
            pageSize:20,
            pageNum:null,
            list:['剧情', '喜剧', '动作','爱情','科幻','动画','悬疑', '惊悚', '恐怖', '犯罪', '同性', '音乐', '歌舞', '传记', '历史', '战争', '西部'],
            list2:[0,1,2,3,4],
            list3:[5,6,7,8,10],
            list4:[10,11,12,13,14],
            list5:[15,16,17,18,19],
            photos:[
               
            ]
        }
    },

    mounted () {
      this.init(); 
    },
    methods:{
         pager:function (currentPage){
               //将当前页码赋值给pageNum
               this.pageNum=currentPage
               console.log("pageNum:",this.pageNum)
               // 得到当前页码 请求下一页数据
               this.$http.get('http://127.0.0.1:8000/getd/other_page',{ params:{ CLASSIFY:this.radio,PAGE:this.pageNum,SIZE:this.pageSize}},{
                            emulateJSON:true})
                    .then((response) => {             
                    
                    var res = JSON.parse(response.body) 
                    console.log('pager.res:',res)
                    this.photos = []
                    
                    for (var i=0;i<res.length;i++) {               
                        this.photos.push(res[i]['fields'])
                    }
                    // console.log("photos:",this.photos)
                    // console.log("len:",len(photos))

                    if (res.error_num === 0) {
                        console.log('success____'+res)
                    } else {
                        console.log('error____'+res)
                    }
                    });
           },

        get_classify(){             
               // PAGE:this.pageNum,CLASSIFY:this.radio,PAGE_SIAE:this.pageSize
               // 得到当前页码 请求下一页数据
               this.pageNum = 1
               this.currentPage = 1
               this.$http.get('http://127.0.0.1:8000/getd/get_classify',{ params:{ CLASSIFY:this.radio}},{
                            emulateJSON:true})
                    .then((response) => {             
                    
                    var res = JSON.parse(response.body) 
                    console.log('classify.res:',res)
                    this.photos = []
                    
                    for (var i=0;i<res.length;i++) {               
                        this.photos.push(res[i]['fields'])
                    }


                    if (res.error_num === 0) {
                        console.log('success____'+res)
                    } else {
                        console.log('error____'+res)
                    }
                    });
                     
        },
        init(){
                         
               // PAGE:this.pageNum,CLASSIFY:this.radio,PAGE_SIAE:this.pageSize
               // 得到当前页码 请求下一页数据
               this.$http.get('http://127.0.0.1:8000/getd/get_classify',{ params:{ CLASSIFY:this.radio}},{
                            emulateJSON:true})
                    .then((response) => {             
                    
                    var res = JSON.parse(response.body) 
                    console.log('pager.res:',res)

                    for (var i=0;i<res.length;i++) {   
                        console.log(i)                
                        this.photos.push(res[i]['fields'])
                    }
                    console.log(this.photos[0].COVER)
                    console.log(len(this.photos))
                    if (res.error_num === 0) {
                        console.log('success____'+res)
                    } else {
                        console.log('error____'+res)
                    }
                    });
                    
           
        },

        to_homepage(){
            this.$router.push("Home")
        },
        to_filmanalysis(){
            this.$router.push("Film_analysis")
        },
        to_detailpage(name){
            this.$router.push("Detailpage")
            this.$root.movie_name = name
        },
        searchmovie(){
                this.$http.get('http://127.0.0.1:8000/sos/sos_data',{ params:{'NAME':this.movie}},{
                emulateJSON:true})
                    .then((response) => {   
                        var res = JSON.parse(response.body)  
                        this.to_detailpage(res[0]['fields'].NAME)    
                    })
        },

        

    },

}

</script>


<style>

    img{
        width: 189px;height:266px;
    }

</style>