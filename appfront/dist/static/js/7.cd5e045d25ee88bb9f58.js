webpackJsonp([7],{Bnrh:function(t,e){},gc5f:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});a("mtWM");var s=a("7t+N"),i=a.n(s),o=(a("4f4F"),a("LK9V"),{mounted:function(){this.getPatent()},methods:{getPatent:function(){var t=document.getElementById("chart1"),e=this.$echarts.init(t);e.showLoading(),i.a.get("http://124.223.32.208:8000/media/json_files/patentAss.json",function(t){e.hideLoading(),console.log(t);for(var a=[],s=[],i=[],o=0;o<t.length;o++)a.push(t[o].assignee),console.log(a),s.push(t[o].C12m_count),i.push(t[o].all_count);s=s.reverse(),i=i.reverse(),e.setOption({color:["#2f89cf","#ee6666"],tooltip:{trigger:"axis",axisPointer:{type:"shadow"}},legend:{top:"2%",right:"38%",data:["过去12个月专利数","2005年起专利数"],textStyle:{color:"#616161",fontSize:16}},grid:{x:0,y2:0,left:"25%",right:"19%",bottom:"2%",top:"10%",containLabel:!0},xAxis:[{type:"value",axisLabel:{textStyle:{show:!0,fontFamily:"微软雅黑",color:"#5b5b5b",fontSize:"18"}}}],yAxis:[{type:"category",axisTick:{alignWithLabel:!0},data:a,axisLabel:{textStyle:{show:!0,fontFamily:"微软雅黑",color:"#5b5b5b",fontSize:"18",rotate:60,interval:0}}}],series:[{name:"2005年起专利数",type:"bar",stack:"Total",barWidth:"90%",barCategoryGap:"40%",itemStyle:{barBorderRadius:3},label:{show:!1},emphasis:{focus:"series"},data:i},{name:"过去12个月专利数",type:"bar",stack:"Total",barWidth:"90%",barCategoryGap:"40%",itemStyle:{barBorderRadius:3},label:{show:!1,position:"left"},emphasis:{focus:"series"},data:s}]})})}}}),l={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"search-model-rank",staticStyle:{display:"block"}},[e("div",{staticClass:"el-col el-col-22",staticStyle:{"padding-left":"10px","padding-right":"10px",float:"left","box-sizing":"border-box",display:"block"}},[e("p",{staticClass:"retrieves_title"},[this._v("科研情报--专利受让机构")]),this._v(" "),e("div",{staticClass:"echarts1",attrs:{id:"chart1"}})])])}]};var r=a("VU/8")(o,l,!1,function(t){a("Bnrh")},null,null);e.default=r.exports}});
//# sourceMappingURL=7.cd5e045d25ee88bb9f58.js.map