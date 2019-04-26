$.show_message=function(){
    $(".message_ul").load('/show_subject/message/' + $("#subject_id").val() + '/')
}

$(function () {
    $.show_message()
})

$(function () {
    $("#submit_message").submit(function (e) {
        var a = $("#submit_message").serializeArray()
        // alert(JSON.stringify(a[1]))   //解析json对象为json字符串
        // alert($('input[name=csrfmiddlewaretoken]').val())
        $.ajax({
            type: "POST",
            url: "/add/message/",
            data: {
                csrfmiddlewaretoken: a[0].value,
                'subject_id': a[1].value,
                'user_message': a[2].value
            },
            success: function (data) {
                // alert(data.status)
                // alert(data.status)
                if (data.status == "error") {
                    $("#userlogin").click();
                } else {
                    $("#user_message").val("");
                    $.show_message()
                }
            }
        })
        // $(".message_ul").load('/add/message/', {'subject_id': a[1].value, 'user_message': a[2].value, csrfmiddlewaretoken: a[0].value }, function (data) {
        //     $("#user_message").val("");
        // })
        return false
    })
});



$(document).on("click","a.btn-delete", function () {
    var type = $(this).data("type");
    // alert($(this).data("id"));
    action[type].call(this);
});

var action = {
    delmessage: function () {
        $(".message_ul").load("/del/message/"+$("#subject_id").val()+"/"+ $(this).data("id") + "/")
    }
};

$(function(){
    $("#study_back").addClass("active");
})

// 留言计数
$(function () {
    $("#user_message").bind('input porpertychange', function (e) {
        max_lengthSet($(this).val().length)
    });
    function max_lengthSet(unm) {
        // alert($("#user_message").val().length)
        if (unm > 1000) {
            // var a = $("#user_message").val().substr(0,1000)
            // $("#user_message").val(a)
            $('#check_zf').text(0)
            $("#user_message").keyup(function () {
                var a = $("#user_message").val().substr(0, 1000)
                $("#user_message").val(a)
            })
        } else {
            $('#check_zf').text(1000 - unm)
        }
    }
    max_lengthSet($("#user_message").val().length)
})

// 留言按钮显示
$(function () {
    $("#user_message").on("focus", function () {
        $("#user_message").addClass("open");
        $(".form_bottom_div").show()
    })

    $("body").on("click", function (e) {
        if (!$(e.target).closest("#submit_message").length) {
            $(".form_bottom_div").hide()
            $("#user_message").removeClass("open");
        }
    })
})
