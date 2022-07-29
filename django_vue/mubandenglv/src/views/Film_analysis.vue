<template>
<el-container>
 <el-header>
    <div class="ui top fixed pointing menu " style="background-color:rgba(100,100,100,0.9);">
        <!-- 顶层菜单 -->
        <img class="ui medium circular image" style="width:50px;height:50px;margin:10px 20px 0 0;" src="./img/image/logo/pumpkin.jpg" @click="to_homepage()">
        

        <a class="item font-set" style="color:white;width:80px;height:45px;margin: 10px 10px 0px 0px;" @click="to_homepage()"> 主页 </a>
        
        <a class="item font-set  active" style="color:white;width:115px;height:45px;margin:10px 10px 0px 0px;"> 电影分析 </a>

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
    <div>
      <h1 style="text-align:center;">电影数据的可视化分析与呈现</h1>
      <div style="height:50px;"></div>
      <div class="round" style="display: flex;">
        <div id="star" style="width:40%;margin-left: 5%;margin-top: 0;"></div>
        <div id="languages" style="width:40%;margin-right: 5%;margin-top: auto;"></div>
      </div>
      
      <div id="year"></div>
      <div id="MINS"></div>
      <div class="IMG">
          <img style="float:right;width:45%;margin-left: 5%;height: 500px;" src="../views/img/genres.png">
      </div>
      <div class="IMG">
        <img style="width:45%;margin-right: 5%;height: 500px;" src="../views/img/regions.png"> 
      </div>
      <!-- <img src="..\assets\genres.png" width="600px" height="400px"> -->
      <!-- <img src="..\assets\regions.png" width="600px" height="400px">  -->
    </div>
  </el-main>
</el-container>
  
</template>

<script>
// 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
import * as echarts from "echarts";
// 引入柱状图图表，图表后缀都为 Chart
import { BarChart } from "echarts/charts";
// 引入提示框，标题，直角坐标系，数据集，内置数据转换器组件，组件后缀都为 Component
import {
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
} from "echarts/components";
// 标签自动布局，全局过渡动画等特性
import { LabelLayout, UniversalTransition } from "echarts/features";
// 引入 Canvas 渲染器，注意引入 CanvasRenderer 或者 SVGRenderer 是必须的一步
import { CanvasRenderer } from "echarts/renderers";
export default {
  created() {
    // 注册必须的组件
    echarts.use([
      TitleComponent,
      TooltipComponent,
      GridComponent,
      DatasetComponent,
      TransformComponent,
      BarChart,
      LabelLayout,
      UniversalTransition,
      CanvasRenderer,
    ]);
  },
  methods:{
    to_homepage(){
        this.$router.push("Home")
    },
    to_filmanalysis(){
        this.$router.push("Film_analysis")
    },
    to_classify(){
        this.$router.push("Classification")
    },
  },
  mounted() {
    let color = [
      "#dd6b66",
      "#759aa0",
      "#e69d87",
      "#8dc1a9",
      "#ea7e53",
      "#eedd78",
      "#73a373",
      "#73b9bc",
      "#7289ab",
      "#91ca8c",
    ];
    // 接下来的使用就跟之前一样，初始化图表，设置配置项
    var myChart1 = echarts.init(document.getElementById("year"));
    var myChart2 = echarts.init(document.getElementById("MINS"));
    var myChart3 = echarts.init(document.getElementById("star"));
    var myChart4 = echarts.init(document.getElementById("languages"));
    let option1 = {
      title: {
        text: "各年份上映电影数",
        subtext: "上映数",
      },
      tooltip: {
        trigger: "axis",
      },
      legend: {
        data: ["上映数量", "Evaporation"],
      },
      toolbox: {
        show: true,
        feature: {
          dataView: { show: true, readOnly: false },
          magicType: { show: true, type: ["line", "bar"] },
          restore: { show: true },
          saveAsImage: { show: true },
        },
      },
      calculable: true,
      xAxis: [
        {
          type: "category",
          // prettier-ignore
          data: ['1923-1932', '1933-1942', '1943-1952', '1953-1962', '1963-1972', '1973-1982', '1983-1992', '1993-2002', '2003-2012', '2013-2022'],
        },
      ],
      yAxis: [
        {
          type: "value",
        },
      ],
      series: [
        {
          name: "",
          type: "bar",
          data: [
            2679, 4678, 4406, 6586, 8337, 10323, 12937, 17399, 32160, 35077,
          ],
          itemStyle: {
            color: (params) => color[params.dataIndex] || "#893448",
          },
          markPoint: {
            data: [
              { type: "max", name: "Max" },
              { type: "min", name: "Min" },
            ],
          },
          markLine: {
            data: [{ type: "average", name: "Avg" }],
          },
        },
      ],
    };
    let option2 = {
      title: {
        text: "最受欢迎的电影时长",
        subtext: "电影数量",
      },
      tooltip: {
        trigger: "axis",
      },
      legend: {
        data: ["上映数量", "Evaporation"],
      },
      toolbox: {
        show: true,
        feature: {
          dataView: { show: true, readOnly: false },
          magicType: { show: true, type: ["line", "bar"] },
          restore: { show: true },
          saveAsImage: { show: true },
        },
      },
      calculable: true,
      xAxis: [
        {
          type: "category",
          // prettier-ignore
          data: ['1-30', '31-60', '61-90', '91-120', '121-150', '151-180'],
        },
      ],
      yAxis: [
        {
          type: "value",
        },
      ],
      series: [
        {
          name: "",
          type: "bar",
          data: [613, 2520, 35304, 42734, 3188, 115],
          itemStyle: {
            color: (params) => color[params.dataIndex] || "#893448",
          },
          markPoint: {
            data: [
              { type: "max", name: "Max" },
              { type: "min", name: "Min" },
            ],
          },
          markLine: {
            data: [{ type: "average", name: "Avg" }],
          },
        },
      ],
    };
    let option3 = {
      title: {
        text: "电影星级分布",
        subtext: "电影数量",
      },
      tooltip: {
        trigger: "item",
      },
      legend: {
        top: "5%",
        left: "center",
      },
      series: [
        {
          name: "Access From",
          type: "pie",
          radius: ["40%", "70%"],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 10,
            borderColor: "#fff",
            borderWidth: 2,
          },
          label: {
            show: false,
            position: "center",
          },
          emphasis: {
            label: {
              show: true,
              fontSize: "40",
              fontWeight: "bold",
            },
          },
          labelLine: {
            show: true,
          },
          data: [
            { value: 318322, name: "1星" },
            { value: 529544, name: "2星" },
            { value: 1404020, name: "3星" },
            { value: 1276241, name: "4星" },
            { value: 641293, name: "5星" },
          ],
        },
      ],
    };
    let option4 = {
      title: {
        text: "电影语言数量统计",
        subtext: "电影数量",
        top:0,
      },
      tooltip: {
        trigger: "item",
      },
      legend: {
        top: "10%",
        left: "center",
      },
      series: [
        {
          name: "Access From",
          type: "pie",
          radius: ["40%", "70%"],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 10,
            borderColor: "#fff",
            borderWidth: 2,
          },
          label: {
            show: false,
            position: "center",
          },
          emphasis: {
            label: {
              show: true,
              fontSize: "30",
              fontWeight: "bold",
            },
          },
          labelLine: {
            show: false,
          },
          data: [
            { value: 49578, name: "英语" },
            { value: 30858, name: "其他" },
            { value: 16153, name: "汉语普通话" },
            { value: 13256, name: "日语" },
            { value: 8802, name: "法语" },
            { value: 4296, name: "韩语" },
            { value: 4162, name: "粤语" },
            { value: 4339, name: "意大利语" },
          ],
        },
      ],
    };
    myChart1.setOption(option1);
    myChart2.setOption(option2);
    myChart3.setOption(option3);
    myChart4.setOption(option4);
  },
};
</script>
  
<style>

#year {
  width: 1000px;
  height: 400px;
  margin: 40px auto;
}
#MINS {
  width: 1000px;
  height: 400px;
  margin: 40px auto;
}
#star {
  width: 600px;
  height: 400px;
  margin: 50px auto;
}
#languages {
  width: 600px;
  height: 400px;
  margin: 70px auto;
}
</style>