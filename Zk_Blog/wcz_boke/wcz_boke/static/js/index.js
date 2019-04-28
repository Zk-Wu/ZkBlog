// 左侧导航栏
$(function () {
    $("#left-bar").find("a.mya").each(function () {
        $(this).on("click", function () {
            $(".nav-link.active.mya").removeClass("active");
            $(this).addClass("active");
        })
        // if ($(mes).attr("href") == location.pathname){
        //     $(this).addClass("active");
        // } else {
        //     $(this).removeClass("active");
        // }
    })
})

// 左侧导航栏浮动
$(function () {
    $(window).scroll(function () {
        //滚动条离顶部距离
        // var scrollTop = $(this).scrollTop(); 
        // // 屏幕总高度
        // var scrollHeight = $(document).height();
        // // 滚动条长度
        // var windowHeight = $(this).height();
        // var hhh=$("#leftbardiv").position().top == 0
        // alert($("#leftbardiv").scrollTop())
        // alert('kk')
        // alert($("#leftbardiv").position().top)
        // alert('kkss')
        // alert($("#leftbardiv").offsetTop())
        // var window_width = $(window).width()
        var lefttop = $("#leftbardiv").offset().top
        var top = $(this).scrollTop()
        var nav_width = $("#sidebar").width()
        // alert(nav_width)
        if (lefttop - top <= 0) {
            // alert(window_width)
            $("#leftbardiv").attr('style', 'position: fixed;top:-3px;z-index: 999;width:' + nav_width + 'px')
            // if (window_width >= 1420) {
            // $("#leftbardiv").attr('style','position: fixed;top:-3px;left:9.4%;z-index: 999;width:'+nav_width+'px')
            // } else if (window_width < 1420 && window_width >= 1390) {
            //     $("#leftbardiv").attr('style','position: fixed;top:-3px;left:9.0%;z-index: 999;width:' +nav_width+'px')
            // } else if (window_width < 1390 && window_width >= 1200) {
            //     $("#leftbardiv").attr('style','position: fixed;top:-3px;left:8%;z-index: 999;width:'+nav_width+'px')
            // } else if (window_width < 1200) {
            //     $("#leftbardiv").attr('style','position: fixed;top:-3px;left:0px;z-index: 999;width:'+nav_width+'px')
            // }
        }
        if (top <= 69) {
            $("#leftbardiv").attr('style', '')
        }
    })
})

$(function () {
    if ($("#cklogin").val()) {
        $("#userlogin").click();
    }
})

// 最新文章显示
$(function () {
    // 1.0版本
    // $.get('/newest_subject/',function(data){
    //     $("#newest_subject").append(data)
    // })
    // 1.1版本
    $("#newest_subject").load('/newest_subject/')
})

// 顶部导航栏导航
$(function () {
    $("#top-navbar").find("a.nav-link").each(function (i, obj) {
        // alert($(obj).attr("href"))
        // alert(location.pathname)
        if ($(obj).attr("href") == location.pathname) {
            $(obj).addClass("active");
            return false;
        } else {
            $(obj).removeClass("active");
        }
    })
})

// 左侧导航栏导航
$(function () {
    $(".left-bar").find("a").each(function () {
        var ok = $(this).data("name");
        if ($(this).data("name")) {
            $(this).on("click", function () {
                $(".main_subject_list").load(
                    "/nav/",
                    { 'block_name': ok, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
                    function (data) {
                        if (!data) {
                            alert("该板块暂无信息，将返回首页");
                            window.location.href = '/';
                        }
                    }
                )
            })
            // $(this).on("click",function(){
            //     $.get('/nav/',{'block_name':$(this).data("name")},function(data){
            //         if (data) {
            //             // remove()删除所选元素和子元素，empty()删除所选元素的子元素
            //             $("#main_subject_list").empty().append(data)
            //             // $("#main_subject_list").load(data)
            //         } else {
            //             alert("暂无此板块主题")
            //         }
            //     })
            // })
        }
    })
})

// 验证码
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
            $("#imgyzm").html(img);
        }
    }
    xhr.send();
}

$(function () {
    $.yzm()
    $("#imgyzm").on('click', function () {
        $.yzm()
    })
})

// 登录验证
$(function () {
    $("#userloginmodal").on('submit', function () {
        if ($("#user").val() && $("#pwd").val()) {
            if (!$("#yzm").val()) {
                $(".errormes-div").html("验证码为空");
                return false
            } else {
                $.get('/check/yzm/' + $("#yzm").val() + '/', function (mes) {
                    if (mes.status == 'f') {
                        $(".errormes-div").html("验证码不正确，注意区分大小写");
                    } else {
                        var url = window.location.href
                        // var text = url.match(/^http(.*)?\/$/g)
                        // alert(text)
                        // var reg=/.*8000?(?=\/)(.*)/;
                        // var m=url.match(reg);
                        // alert(m[1])
                        var formData = $("#userloginmodal").serializeArray();
                        $.post(
                            '/userlogin/',
                            {
                                csrfmiddlewaretoken: formData[0].value,
                                'username': formData[1].value,
                                'pwd': formData[2].value,
                                // 'to_url': m[1]
                            },
                            function (data) {
                                if (data.status == 'f') {
                                    $(".errormes-div").html("用户名或密码错误");
                                } else {
                                    window.location.href = url;
                                }
                            }
                        )
                    }
                })
            }
            return false
        } else if (!$("#user").val()) {
            $(".errormes-div").html("用户名为空");
            alert('2')
            return false
        } else if (!$("#pwd").val()) {
            $(".errormes-div").html("密码为空");
            alert('3')
            return false
        } else if ($("#yzm").val()) {
            var status = false;
            if ($(this).val()) {
                $.ajaxSettings.async = false;
                $.get('/check/yzm/' + $(this).val() + '/', function (mes) {
                    if (mes.status == 'f') {
                        $(".errormes-div").html("验证码不正确，注意区分大小写");
                    } else {
                        status = true;
                    }
                })
                $.ajaxSettings.async = true;
            }
            return status;
        } else {
            $(".errormes-div").html("用户名为空");
            alert('4')
            return false
        }
    })
})

// 忘记密码
$(function () {
    $(document).on("click", "#reset-pwd", function () {
        $("#divuserform").load('/reset/userpwd/')
        $("#modal-title-login").html("ZCoreW博客·忘记密码")
    })

    $(document).on("blur", "input.form-control", function () {
        var id = $(this).attr("id");
        // alert(id)
        unaction[id].call(this);
    })
    var unaction = {
        email: function () {
            $.ajaxSettings.async = false;
            $(".errormes-div").html("");
            var status = false;
            if ($(this).val()) {
                var mail = $(this).val();
                var ckemail = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
                if (ckemail.test(mail)) {
                    status = true;
                } else {
                    $(".errormes-div").html("邮箱格式错误");
                }
            }
            return status;
        },
        emailyzm: function () {
            $(".errormes-div").html("");
            var status = false;
            if ($(this).val()) {
                $.get('/check/email/' + $(this).val() + '/', function (mes) {
                    if (mes.status == 'f') {
                        $(".errormes-div").html("验证码错误");
                    } else {
                        status = true;
                    }
                })
                $.ajaxSettings.async = true;
            }
            return status;
        }
    }

    $(document).on('click', ".emailyz", function () {
        if ($(".emailyz").hasClass("disabled")) {
            return false
        } else {
            if (!$("#email").val()) {
                $(".errormes-div").html("请您输入邮箱");
            } else {
                if (unaction.email.call($("#email"))) {
                    // alert(unaction.email.call($("#email")))
                    // alert($("#email").val())
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
                                        $(".emailyz").html("重新发送").removeClass("disabled");
                                        clearInterval(countDown);
                                    } else {
                                        $(".emailyz").html(count + "秒重新发送").addClass("disabled");
                                        count--;
                                    }
                                }, 1000);
                            }
                        })
                }
            }
        }
    })

    $(document).on("click", "#reset_pwd", function () {
        if (unaction.email.call($("#email")) && unaction.emailyzm.call($("#emailyzm"))) {
            $("#divuserform").load('/set/userpwd/setpwd/', { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), 'email': $("#email").val() })
            // alert($("#email").val()) 
        }
    })

    $(document).on("click", "#set_pwd", function () {
        if ($("#pwd").val() && $("#repwd").val()) {
            var ckpwd = /^.*(?=.{8,16})(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).*$/;
            if (ckpwd.test($("#pwd").val())) {
                if ($("#repwd").val() == $("#pwd").val()) {
                    $.post('/set/userpwd/updatepwd/', { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), 'pwd': $("#pwd").val() }, function (data) {
                        if (data.status == 't') {
                            alert("修改成功，返回首页登录")
                            window.location.href = '/'
                        }
                    })
                } else {
                    $(".errormes-div").html("两次输入密码不一致");
                }
            } else {
                $(".errormes-div").html("包含数字/大/小写字母，8-16位");
            }
        } else if (!$("#pwd").val()) {
            $(".errormes-div").html("密码为空");
        } else if (!$("#repwd").val()) {
            $(".errormes-div").html("确认密码为空");
        } else {
            $(".errormes-div").html("输入框为空");
        }
    })
})

// 搜索框
$(function () {
    $("#searchform").on("submit", function () {
        if (!$("#searchinput").val()) {
            return false;
        }
    })
})

// 手机侧边栏
$(function () {
    $("#sdaas").on("click", function () {
        var k = $("#phone_leftbar").offset().top;
        var winheight = $(document).height();
        $("#mobile-menu").slideToggle(400)
        if ($("#sdaas").hasClass('oi-caret-right')) {
            $("#sdaas").removeClass('oi-caret-right')
            $("#sdaas").addClass('oi-caret-bottom')
            if (winheight <= 360) {
                $("#phone_leftbar").attr('style', 'height:' + (winheight - k) + 'px;overflow-y:scroll')
            }
        } else {
            $("#sdaas").removeClass('oi-caret-bottom')
            $("#sdaas").addClass('oi-caret-right')
            $("#phone_leftbar").attr('style', '')
        }

    })
})

// 时间归档框
$(function () {
    $("#save_date").load('/date/save/', function () {
        // 判定当前年份
        var new_date = new Date()
        var new_year = new_date.getFullYear()
        $("#" + new_year + "ul").slideToggle(300, function () {
            $("#" + new_year + "icon").removeClass("oi-chevron-right");
            $("#" + new_year + "icon").addClass("oi-chevron-bottom");
        });
        $(".one_li").find("span.date-li-span").each(function (e) {
            $(this).on("click", function () {
                var li_year = $(this).data("dateyear")
                // alert(li_year)
                $("#" + li_year + "ul").slideToggle(300, function () {
                    if ($("#" + li_year + "icon").hasClass("oi-chevron-right")) {
                        $("#" + li_year + "icon").removeClass("oi-chevron-right");
                        $("#" + li_year + "icon").addClass("oi-chevron-bottom");
                    } else {
                        $("#" + li_year + "icon").removeClass("oi-chevron-bottom");
                        $("#" + li_year + "icon").addClass("oi-chevron-right");
                    }
                })

            })
        })
        // 点击查询
        $("#datesaveul").find("a").each(function (e) {
            // alert(e)
            $(this).on("click", function () {
                var date = $(this).data("date")
                // alert(date)
                $(".main_subject_list").load("/date/save/", { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), 'date': date })
            })

        })
    })

})

$(function () {
    var num = 30;
    var nowtime = 0;
    var lasttime = 0;
    $(window).scroll(
        function () {
            var scrollTop = $(this).scrollTop();
            var scrollHeight = $(document).height();
            var windowHeight = $(this).height();
            if (scrollTop + windowHeight >= scrollHeight * 0.97) {
                nowtime = new Date().getTime();
                time = nowtime - lasttime
                lasttime = nowtime
                if (lasttime == 0 || (lasttime != 0 && time >= 1000)) {
                    // 此处是滚动条到底部时候触发事件，加载的数据
                    $.get('/bottomlist/?first=' + num + '&last=' + (num + 10), function (data) {
                        if (data) {
                            // console.log(data)
                            $(".main_subject_list").append(data)
                        } else {
                            console.log("到底了")
                        }
                        num = num + 10
                    })
                }
            }
        });
})

//鼠标的移入移出  
// $(".sss").mouseover(function (){  
//         $("#kkk").show();  
//     }).mouseout(function (){  
//         $("#kkk").hide();  
//     });