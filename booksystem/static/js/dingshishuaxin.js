//��ʱˢ�½��棨0.5�룩
$(document).ready(function(){
  setInterval(function() {
    $.get("{% url 'barrages_refresh' %}" + window.location.search,//GET�����url��ַ
    function(data,status){
      $("#barrages_list").html(data);//�����б�����
      });
    }, 500);
});