$(document).ready(function(){

    var number1=$.trim($("#number1").text())

    if(number1!='0'){

        $("#number1").css("color","red")
    }



    // setInterval(function() {
    // $.post("/dingshiforadmin" ,//GET请求的url地址
    //     {},
    // function(data){
    //   $("#number1").val(data["number1"]);//更新列表内容
    //   },'json');
    // }, 1000);







});

