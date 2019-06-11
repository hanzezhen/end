$(document).ready(function () {
    $('#sid').focusout(function () {

        var a = $.trim($('#sid').val());
        if (a == '') {
            $('#che').text('请输入学号')
        }
        else {
            $.ajax({
                    url: '/ajax1get/',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({
                        'username': a
                    }),
                    headers: {'X-CSRFToken': $('[name="csrfmiddlewaretoken"]').val()},

                    success: function (data) {
                        var dataObj = JSON.parse(data);
                        if (dataObj['sttr'] == 'yes') {
                            $('#che').text('此学号已存在,请重新输入!');
                            $('#sid').val('')
                        }
                        else if (dataObj['sttr'] == 'no') {
                            $('#che').text('此学号可以使用!');
                        }
                    }
                }
            )

        }
    })

    $('#sid').focus(function () {
        $('#che').text('')
    })
})