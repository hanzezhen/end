function checkpost() {
    if(form.username.value==''){
        alert('请输入账号');
        form.username.focus();
        return false;
    }

    if(form.password.value==''){
        alert('请输入密码');
        form.password.focus();
        return false;
    }
}

