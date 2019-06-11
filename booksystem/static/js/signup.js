function checksub() {
    if($.trim($("#password").val())==''){
        alert('请输入密码');
        $("#password").focus();
        return false;
    }
    if($.trim($("#uname").val())==''){
        alert('请输入密码');
        $("#uname").focus();
        return false;
    }if($.trim($("#idn").val())==''){
        alert('请输入学号');
        $("#idn").focus();
        return false;
    }if($.trim($("#name").val())==''){
        alert('请输入姓名');
        $("#name").focus();
        return false;
    }
}


