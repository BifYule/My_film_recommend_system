<template>

  <div id="building">
    <div class="container">
    <div class="main">
        <!-- 整个注册盒子 -->
      <div class="loginbox">
          <!-- 左侧的注册盒子 -->
          <div class="loginbox-in">
            <div class="userbox">
            <span class="iconfont">&#xe817;</span>
            <input  class="user" id="user"  v-model="name" placeholder="用户名">
            </div>

            <br>
            <div class="pwdbox">
              <span class="iconfont">&#xe775;</span>
            <input  class="pwd"  id="password" v-model="pwd" type="password"  placeholder="密码">
            </div>

            <br>
            <button type="primary"  class="register_btn" @click="register()">注册</button>
          </div>

        <!-- 右侧的注册盒子 -->
         <div class="background">
            <div class="title"></div>
        </div>

      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: "Login",

  data:function (){
    return{
      name:'',
      pwd:'',
      user_list:[
      ]
    }
  },
  methods:{

    register(){
      this.$http.get('http://127.0.0.1:8000/api/add_user',{params:{user_name:this.name,user_password:this.pwd}},{
                            emulateJSON:true})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.showBooks()
          } else {
            this.$message.error('新增用户失败，请重试')
            console.log(res['msg'])
          }
        });
        alert('注册成功');
          this.$router.push({
            path: '/',
            query: {
              list: this.user_list,}
          })
        }
      }

    }

</script>

<style scoped>
#building{
  background:url("./img/beach.jpg");
  width:100%;
  height:100%;
  position:fixed;
  background-size:100% 100%;
}
.loginbox{
    display:flex;
    position:absolute;
    width:800px;
    height:400px;
    top:40%;
    left:50%;
    transform:translate(-50%,-50%);
    box-shadow: 0 12px 16px 0  rgba(0,0,0,0.24), 0 17px 50px 0 #4E655D;
}
.loginbox-in{
     background-color:#89AB9E;
     width:240px;
}
.userbox{
    margin-top:120px ;
    height:30px;
     width:230px;
     display: flex;
     margin-left:25px;
}
.pwdbox{
    height:30px;
    width:225px;
    display: flex;
    margin-left:25px;
}

.background{
    width:570px;
    background-image:url('./img/gross.jpg');
    background-size:cover;
    font-family:sans-serif;
}
.title{
    margin-top:320px;
    font-weight:bold;
    font-size:20px;
    color:#4E655D;

}
.title:hover{
     font-size:21px;
     transition: all 0.4s ease-in-out;
     cursor: pointer;
}
.uesr-text{
     position:left;
}
input{
    outline-style: none ;
    border: 0;
    border-bottom:1px solid #E9E9E9;
    background-color:transparent;
    height:20px;
     font-family:sans-serif;
    font-size:15px;
    color:white;
    font-weight:bold;
}
 /* input::-webkit-input-placeholder{
    color:#E9E9E9;
 } */
input:focus{
    border-bottom:2px solid #445b53;
    background-color:transparent;
     transition: all 0.2s ease-in;
     font-family:sans-serif;
    font-size:15px;
     color:white;
     font-weight:bold;

}
input:hover{
    border-bottom:2px solid #445b53;
    background-color:transparent;
     transition: all 0.2s ease-in;
     font-family:sans-serif;
    font-size:15px;
     color:#445b53;
     font-weight:bold;

}

input:-webkit-autofill {
 box-shadow: 0 0 0px 1000px  #89AB9E inset !important;
 -webkit-text-fill-color: #445b53;

}

input:-webkit-autofill::first-line {
 font-size: 15px;
 font-weight:bold;
 }
.log-box{
    font-size:12px;
    display: flex;
    justify-content: space-between ;
    width:174px;
    margin-left:30px;
    color:#4E655D;
    margin-top:-5px;
    align-items: center;

}
.log-box-text{
    color:#4E655D;
    font-size:12px;
      text-decoration:underline;
    }
.register_btn{
    background-color: #5f8276; /* Green */
    border: none;
    color: #FAFAFA;
    padding: 7px 35px;
    margin-left:50px;
    text-align: center;
    text-decoration: none;
    font-size: 13px;
    border-radius: 20px;
    outline:none;
}
.register_btn:hover{
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
    cursor: pointer;
     background-color: #0b5137;
    transition: all 0.2s ease-in;
}

.warn{
    margin-top:60px;
    margin-right:110px;
    margin-bottom: 5px;
    font-weight:bold;
    font-size:17px;
}


.register_btn:hover{
    font-weight:bold;
    cursor: pointer;
}
@font-face {
    font-family: "iconfont";
    src: url('./font/iconfont.eot');
    src: url('./font/iconfont.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
    url('./font/iconfont.woff2') format('woff2'), url('./font/iconfont.woff') format('woff'), url('./font/iconfont.ttf') format('truetype'), /* chrome, firefox, opera, Safari, Android, iOS 4.2+ */
    url('./font/iconfont.svg#iconfont') format('svg');
}

.iconfont {
    font-family: "iconfont" !important;
    font-size: 20px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    height:22px;
    color:#4E655D;
    margin-right:10px;
    margin-top:3px;
}

.icon-key:before {
    content: "\e775";
}

.icon-account:before {
    content: "\e817";
}

</style>
