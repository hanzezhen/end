window.onload=function(){
      updatenum()
      var pichuli=document.getElementById("pichuli")

      var dangechuli=document.getElementById("dangechuli")
      var piliangdiv=document.getElementById("piliangdiv")
      var dangediv=document.getElementById("dangediv")
      pichuli.onclick=function(){
          pichuli.style.backgroundColor="#4b9aeb";
          dangechuli.style.backgroundColor="#dddddd";
          piliangdiv.style.display="block";

          dangediv.style.display="none";
      };
      dangechuli.onclick=function(){
          dangechuli.style.backgroundColor="#4b9aeb";
          pichuli.style.backgroundColor="#dddddd";


          dangediv.style.display="block";
          piliangdiv.style.display="none";
      };







}

function updatenum(){

    var checkstudents=document.getElementsByName("_selected_action")

    var num=0;
    for (i=0;i<checkstudents.length;i++){
		if(checkstudents[i].checked) {

            num=num+1;
		}
    }

    var stunum=document.getElementById("stunum")

    stunum.innerText=num+"";
};






function quanxuan1(){//没有导入jquery
    	var item=document.getElementsByName("item1")
		// item.prop("checked",true)
		for (i=0;i<item.length;i++){
			item[i].checked=true
		}

	}
function fanxuan1(){//没有导入jquery
    var item=document.getElementsByName("item1")
    // item.prop("checked",true)
    for (i=0;i<item.length;i++){
        if(item[i].checked) {

            item[i].checked = false
        }
        else{
            item[i].checked = true
        }
    }

}

function quanxuan2(){//没有导入jquery
    	var item=document.getElementsByName("item2")
		// item.prop("checked",true)
		for (i=0;i<item.length;i++){
			item[i].checked=true
		}

	}
function fanxuan2(){//没有导入jquery
    var item=document.getElementsByName("item2")
    // item.prop("checked",true)
    for (i=0;i<item.length;i++){
        if(item[i].checked) {

            item[i].checked = false
        }
        else{
            item[i].checked = true
        }
    }

}


function quanxuan3(){//没有导入jquery
    	var item=document.getElementsByName("_selected_action")
		// item.prop("checked",true)
		for (i=0;i<item.length;i++){
			item[i].checked=true
		}
		updatenum();

	}
function fanxuan3(){//没有导入jquery
    var item=document.getElementsByName("_selected_action")
    // item.prop("checked",true)
    for (i=0;i<item.length;i++){
        if(item[i].checked) {

            item[i].checked = false
        }
        else{
            item[i].checked = true
        }
    }
    updatenum();

}


function chongxinfenpei1(){
    stuid=$.trim($("#stuid").text())
    stuname=$.trim($("#stuname").text())
    item1=$("item1")
    var values=new Array()
    var texts=new Array()
    $.each($("input[name='item1']"),function () {
        if(this.checked){
            texts.push($(this).next().text())
            values.push($(this).val())
        }

    })





    if(stuid==""){
        $("#rizhi").text("*请先点击学生编号来选择学生")
        $("#rizhi").css("color","red")
    }
    else if(values.length==0){
        $("#rizhi").text("*请选择设备")
        $("#rizhi").css("color","red")
    }
    else{

        $.post(
        	"/chongxinfenpei1/",
			JSON.stringify({"stuid":stuid,"values":values}),
			function(data) {
                 $("#rizhi").text("重新分配:  "+stuname+" 具有 "+texts+" 使用权限 ")
                 $("#rizhi").css("color","blue")
            },
			"json"
	);
    }

}

function tianjia1(){
    stuid=$.trim($("#stuid").text())
    stuname=$.trim($("#stuname").text())
    item1=$("item1")
    var values=new Array()
    var texts=new Array()
    $.each($("input[name='item1']"),function () {
        if(this.checked){
            texts.push($(this).next().text())
            values.push($(this).val())
        }

    })

    if(stuid==""){
        $("#rizhi").text("*请选择学生")
        $("#rizhi").css("color","red")
    }
    else if(values.length==0){
        $("#rizhi").text("*请选择设备")
        $("#rizhi").css("color","red")
    }
    else{

        $.post(
        	"/tianjia1/",
			JSON.stringify({"stuid":stuid,"values":values}),
			function(data) {
                 $("#rizhi").text("添加权限:  已为"+stuname+" 添加 "+texts+" 使用权限 ")
                 $("#rizhi").css("color","blue")
            },
			"json"
	);
    }
}

function shanchu1(){
    stuid=$.trim($("#stuid").text())
    stuname=$.trim($("#stuname").text())
    item1=$("item1")
    var values=new Array()
    var texts=new Array()
    $.each($("input[name='item1']"),function () {
        if(this.checked){
            texts.push($(this).next().text())
            values.push($(this).val())
        }

    })

    if(stuid==""){
        $("#rizhi").text("*请选择学生")
        $("#rizhi").css("color","red")
    }
    else if(values.length==0){
        $("#rizhi").text("*请选择设备")
        $("#rizhi").css("color","red")
    }
    else{

        $.post(
        	"/shanchu1/",
			JSON.stringify({"stuid":stuid,"values":values}),
			function(data) {
                 $("#rizhi").text("删除权限:  已为"+stuname+" 删除 "+texts+" 使用权限 ")
                 $("#rizhi").css("color","blue")
            },
			"json"
	);
    }
}
//批处理分配
function chongxinfenpei2(){

    var stus=new Array()
    var stunames=new Array()
    $.each($("input[name='_selected_action']"),function () {
        if(this.checked){
            stunames.push($(this).parent().next().next().next().children("span").text())
            stus.push($(this).val())
        }

    })



    var values=new Array()
    var texts=new Array()
    $.each($("input[name='item2']"),function () {
        if(this.checked){
            texts.push($(this).next().text())
            values.push($(this).val())
        }

    })

    if(stus.length==0){
        $("#rizhi").text("*请先点击学生编号来选择学生")
        $("#rizhi").css("color","red")
    }
    else if(values.length==0){
        $("#rizhi").text("*请选择设备")
        $("#rizhi").css("color","red")
    }
    else{

        $.post(
        	"/chongxinfenpei2/",
			JSON.stringify({"stus":stus,"values":values}),
			function(data) {
               $("#rizhi").text("重新分配:  "+stunames+" 具有 "+texts+" 使用权限 ")
               $("#rizhi").css("color","blue")
            },
			"json"
	);
    }

}

function tianjia2(){
    var stus=new Array()
    var stunames=new Array()
    $.each($("input[name='_selected_action']"),function () {
        if(this.checked){
            stunames.push($(this).parent().next().next().next().children("span").text())
            stus.push($(this).val())
        }
    })
    var values=new Array()
    var texts=new Array()
    $.each($("input[name='item2']"),function () {
        if(this.checked){
            texts.push($(this).next().text())
            values.push($(this).val())
        }
    })
    if(stus.length==0){
        $("#rizhi").text("*请先点击学生编号来选择学生")
        $("#rizhi").css("color","red")
    }
    else if(values.length==0){
        $("#rizhi").text("*请选择设备")
        $("#rizhi").css("color","red")
    }
    else{
        $.post(
        	"/tianjia2/",
			JSON.stringify({"stus":stus,"values":values}),
			function(data) {
               $("#rizhi").text("添加权限:  已为"+stunames+" 添加 "+texts+" 使用权限 ")
               $("#rizhi").css("color","blue")
            },
			"json"
	);
    }
}

function shanchu2(){
    var stus=new Array()
    var stunames=new Array()
    $.each($("input[name='_selected_action']"),function () {
        if(this.checked){
            stunames.push($(this).parent().next().next().next().children("span").text())
            stus.push($(this).val())
        }
    })
    var values=new Array()
    var texts=new Array()
    $.each($("input[name='item2']"),function () {
        if(this.checked){
            texts.push($(this).next().text())
            values.push($(this).val())
        }
    })
    if(stus.length==0){
        $("#rizhi").text("*请先点击学生编号来选择学生")
        $("#rizhi").css("color","red")
    }
    else if(values.length==0){
        $("#rizhi").text("*请选择设备")
        $("#rizhi").css("color","red")
    }
    else{
        $.post(
        	"/shanchu2/",
			JSON.stringify({"stus":stus,"values":values}),
			function(data) {
               $("#rizhi").text("删除权限:  已为"+stunames+" 删除 "+texts+" 使用权限 ")
               $("#rizhi").css("color","blue")
            },
			"json"
	);
    }
}


