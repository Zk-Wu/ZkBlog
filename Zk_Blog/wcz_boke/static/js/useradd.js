$.yzm = function () {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/yzm/', true);
    xhr.responseType = 'blob';
    xhr.onload = function () {
        if (this.status == 200) {
            var blob = this.response;
            var img = document.createElement("img");
            img.setAttribute("class", "yzm-img");
            img.src = window.URL.createObjectURL(blob);
            img.onload = function (e) {
                window.URL.revokeObjectURL(img.src);
            };
            $("#imgcontainer").html(img);
        }
    }
    xhr.send();
}

$(function () {
    $.yzm()
    $("#imgcontainer").on('click', function () {
        $.yzm()
    })
})

$.error = function (id, helpmes) {
    $(id).addClass("input-error");
    $(helpmes).addClass("help-error");
}

$.ok = function (id, helpmes) {
    $(id).removeClass("input-error");
    $(helpmes).removeClass("help-error");
}

$.pass = function (id) {
    $(id).addClass("oi oi-check oi-color");
}

$(function () {
    $("input.form-control").on("focus", function () {
        // onfocus是得到焦点, onblur 是失去焦点
        var id = $(this).attr("id");
        action[id].call(this);
    })

    var action = {
        user: function () {
            $("#userHelp").removeClass("oi oi-check oi-color");
            $("#userHelp").html("提交后不可更改，为字母/数字/下划线组合")
        },
        pwd: function () {
            $("#pwdHelp").removeClass("oi oi-check oi-color");
            $("#pwdHelp").html("密码长度为8-16位，不允许有空格")
        },
        repwd: function () {
            $("#repwdHelp").removeClass("oi oi-check oi-color");
            $("#repwdHelp").html("确认密码，与密码一致")
        },
        email: function () {
            $("#emailHelp").removeClass("oi oi-check oi-color");
            $("#emailHelp").html("我们不会将你的邮箱分享给任何人")
        },
        emailyzm: function () {
            $("#emailyzmHelp").removeClass("oi oi-check oi-color");
            $("#emailyzmHelp").html("输入6位验证码，字母/数字组合")
        },
        yzm: function () {
            $("#yzmHelp").removeClass("oi oi-check oi-color");
            $("#yzmHelp").html("输入4位验证码，字母/数字组合")
        }
    }

    $("input.form-control").on("blur", function () {
        var id = $(this).attr("id");
        unaction[id].call(this);
    })

    var unaction = {
        user: function () {
            $.ajaxSettings.async = false;
            $("#userHelp").html("");
            var status = false;
            if ($(this).val()) {
                var username = $(this).val();
                var ckname = /^[A-Za-z0-9_]{3,10}$/;
                if (ckname.test(username)) {
                    $.get('/check/username/' + username + '/', function (mes) {
                        if (mes.status == 'f') {
                            $("#userHelp").removeClass("oi oi-check oi-color");
                            $.error("#user", "#userHelp");
                            $("#userHelp").html("该用户名已存在");
                        } else {
                            $.ok("#user", "#userHelp");
                            $.pass("#userHelp");
                            status = true;
                        }
                    });
                } else {
                    $("#userHelp").removeClass("oi oi-check oi-color");
                    $.error(this, "#userHelp");
                    $("#userHelp").html("长度为3-10位，为字母/数字/下划线组合");
                }
            }
            return status
        },
        pwd: function () {
            $("#pwdHelp").html("");
            var status = false;
            if ($(this).val()) {
                var pwd = $(this).val();
                var ckpwd = /^.*(?=.{8,16})(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).*$/;
                if (ckpwd.test(pwd)) {
                    $.ok(this, "#pwdHelp");
                    $.pass("#pwdHelp");
                    status = true;
                } else {
                    $("#pwdHelp").removeClass("oi oi-check oi-color");
                    $.error(this, "#pwdHelp");
                    $("#pwdHelp").html("必须包含数字/大/小写字母");
                }
            }
            return status;
        },
        repwd: function () {
            $("#repwdHelp").html("");
            var status = false;
            if ($(this).val()) {
                if ($(this).val() == $("#pwd").val()) {
                    $.ok(this, "#repwdHelp");
                    $.pass("#repwdHelp");
                    status = true;
                } else {
                    $("#repwdHelp").removeClass("oi oi-check oi-color");
                    $.error(this, "#repwdHelp");
                    $("#repwdHelp").html("两次输入密码不一致");
                }
            }
            return status;
        },
        email: function () {
            $("#emailHelp").html("");
            var status = false;
            if ($(this).val()) {
                var mail = $(this).val();
                var ckemail = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
                if (ckemail.test(mail)) {
                    $.ok(this, "#emailHelp");
                    $.pass("#emailHelp");
                    status = true;
                } else {
                    $("#emailHelp").removeClass("oi oi-check oi-color");
                    $.error(this, "#emailHelp");
                    $("#emailHelp").html("邮箱格式错误");
                }
            }
            return status;
        },
        emailyzm: function () {
            $("#emailyzmHelp").html("");
            var status = false;
            if ($(this).val()) {
                $.get('/check/email/' + $(this).val() + '/', function (mes) {
                    if (mes.status == 'f') {
                        $("#emailyzmHelp").removeClass("oi oi-check oi-color");
                        $.error("#emailyzm", "#emailyzmHelp");
                        $("#emailyzmHelp").html("验证码不正确");
                    } else {
                        $.ok("#emailyzm", "#emailyzmHelp");
                        $.pass("#emailyzmHelp");
                        status = true;
                    }
                })
            }
            return status;
        },
        yzm: function () {
            $("#yzmHelp").html("");
            var status = false;
            if ($(this).val()) {
                $.get('/check/yzm/' + $(this).val() + '/', function (mes) {
                    if (mes.status == 'f') {
                        $("#yzmHelp").removeClass("oi oi-check oi-color");
                        $.error("#yzm", "#yzmHelp");
                        $("#yzmHelp").html("验证码不正确，注意区分大小写");
                    } else {
                        $.ok("#yzm", "#yzmHelp");
                        $.pass("#yzmHelp");
                        status = true;
                    }
                })
                $.ajaxSettings.async = true;
            }
            return status;
        }
    }

    $(".email-yz").on('click', function () {
        if ($(".email-yz").hasClass("disabled")) {
            return false
        } else {
            if (!$("#email").val()) {
                $.error("#email", "#emailHelp")
                $("#emailHelp").html("请您输入邮箱");
            } else {
                if (unaction.email.call($("#email"))) {
                    // alert(unaction.email.call($("#email")))
                    $.post(
                        '/send/email/',
                        { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), 'user_email': $("#email").val() },
                        function (mes) {
                            if (mes.status == 'f') {
                                alert("出现未知错误")
                            } else {
                                let count = 60;
                                const countDown = setInterval(() => {
                                    if (count == 0) {
                                        $(".email-yz").html("重新发送").removeClass("disabled");
                                        clearInterval(countDown);
                                    } else {
                                        $(".email-yz").html(count + "秒重新发送").addClass("disabled");
                                        count--;
                                    }
                                }, 1000);
                            }
                        })
                }
            }
        }
    })

    $("#useraddform").on('submit', function () {
        if (unaction.user.call($("#user")) && unaction.pwd.call($("#pwd")) && unaction.repwd.call($("#repwd")) && unaction.email.call($("#email")) && unaction.emailyzm.call($("#emailyzm")) && unaction.yzm.call($("#yzm"))) {
            return true
        } else {
            return false
        }
    })
})