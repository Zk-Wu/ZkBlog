$.show_usermes = function () {
    $("#list_div").load('/show/usermes/')
}

$.check_email = function (email) {
    var ckemail = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
    if (email) {
        if (ckemail.test(email)) {
            return true;
        } else {
            return false;
        }
    } else {
        return true;
    }
}

$.check_nicheng = function (nicheng) {
    var cknicheng = /^[\u4e00-\u9fa5_a-zA-Z0-9]{1,10}$/
    if (nicheng) {
        if (cknicheng.test(nicheng)) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

$(function () {
    $.show_usermes()
})

$(function () {
    $("#usermes_submit").on('click', function () {
        var csrf = $('input[name=csrfmiddlewaretoken]').val()
        var user_message = $("#user_message").val()
        var email = $("#email").val()
        var nicheng = $("#nicheng").val()
        var a = $.check_email(email)
        var b = $.check_nicheng(nicheng)
        if (a && b) {
            // "#list_div"
            $.post('/usermes/', { csrfmiddlewaretoken: csrf, 'mes': user_message, 'email': email, 'nicheng': nicheng }, function (data) {
                if (data.status == 't') {
                    $.show_usermes()
                    alert("留言成功，请勿重复提交")
                    $("#user_message").val("");
                } else {
                    alert("未知错误")
                }
            })
        } else {
            $("#helperror").html("昵称或邮箱格式错误");
        }
    })
})

$(function () {
    $('#UserMessageModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget)
        var mesid = button.data('mesid')
        $("#usermesid").val(mesid)
        var nicheng = button.data('nicheng')
        var modal = $(this)
        modal.find('.modal-title').text('回复@' + nicheng)
    })

    $("#userhuifu").on("click", function () {
        var csrf = $('input[name=csrfmiddlewaretoken]').val()
        var userhuifu = $("#user-message").val()
        var email = $("#message-email").val()
        var nicheng = $("#message-nicheng").val()
        var fuid = $("#usermesid").val()
        var a = $.check_email(email)
        var b = $.check_nicheng(nicheng)
        if (a && b) {
            $.post('/usermes/', { csrfmiddlewaretoken: csrf, 'fuid':fuid, 'mes': userhuifu, 'email': email, 'nicheng': nicheng }, function (data) {
                if (data.status == 't') {
                    $.show_usermes()
                    // alert("回复成功")
                    $(".close").click();
                } else {
                    alert("未知错误")
                }
            })
        } else {
            $("#errorhf").html("昵称或邮箱格式错误");
        }
    })
})