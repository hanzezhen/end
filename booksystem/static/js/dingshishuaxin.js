//定时刷新界面（0.5秒）
$(document).ready(function(){
  setInterval(function() {
    $.get("{% url 'barrages_refresh' %}" + window.location.search,//GET请求的url地址
    function(data,status){
      $("#barrages_list").html(data);//更新列表内容
      });
    }, 500);
});