$(function(){
    $("#textTitle").bind('input porpertychange',function(e){
      max_lengthSet($(this).val().length)
    });
    function max_lengthSet(unm){
      $('.title_span_change').text(unm)
    }
    max_lengthSet($("#textTitle").val().length)
  })


$(function(){
  $("#submit").bind("click",function(e){
    // alert($(".mes_body").summernote('code'))
    $.ajax({
      type:"POST",
      url:"/add/subject/",
      data:{
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        'subject_name':$("#textTitle").val(),
        'message':$(".mes_body").summernote('code'),
        'block':$("#subject_Category").val(),
        'subject_type':$("#post_Category").val()
      },
      success:function(data){
        if (data.status == "ok") {
          window.location.href = '/';
        }
      }
    })
  })
})

$(function(){
   $('.mes_body').summernote({
      placeholder:'请输入文章内容',
      tabsize: 2,
      height:1000,
      lang:'zh-CN',
      dialogsFade : true,
      dialogsInBody : true,
      disableDragAndDrop : false,
      focus: true,
      toolbar: [["style", ["style"]], ['fontsize', ['fontsize']],["font", ["bold", "underline", "clear"]], ["fontname", ["fontname"]], ["color", ["color"]], ["para", ["ul", "ol", "paragraph"]], ["table", ["table"]], ["insert", ["link", "picture"]], ["view", ["code","codeview", "help"]]],
      fontSizes: ['10', '12', '14', '16', '18','20', '22','24', '26','28','30','32','34','36','64','72'],
      callbacks:{
        // 调用图片上传
        onImageUpload:function (files){
          sendImg(files);
        },
        //取消粘贴时带上样式
        onPaste: function(ne){
          var bufferText = ((ne.originalEvent || ne).clipboardData || window.clipboardData).getData('Text/plain');
          // console.log(bufferText);
          ne.preventDefault ? ne.preventDefault() : (ne.returnValue = false);
          // console.log(bufferText);
          document.execCommand('insertText',false,bufferText);
          // console.log((e.originalEvent || e).clipboardData.getData('Html'))
          // console.log(e.currentTarget.innerHTML)
        },
      },
    });
    $('.mes_body').summernote('formatPara');


  // ajax上传图片
  function sendImg(files){
    var size = files[0].size;
    if((size/1024/1024) > 3){
      alert("图片大小不能超过3M...");
      return false;
    }
    var formData = new FormData();
    formData.append("file",files[0]);
    $.ajax({
      type:"POST",
      url:'/save/img/',
      data:formData,
      // data:{
      //   csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      //   'formdata':formData
      // },
      cache: false,  
      contentType: false,
      processData: false,
      dataType:"json",
      success:function(data){
        //直接插入路径就行，filename可选
        // console.log(data)
        data = JSON.parse(data)
        if (data.status) {
          alert("未知错误")
        } else {
          // alert(data)
          $('.mes_body').summernote('insertImage',data.FileUrl,data.FileName);
        }
      },
      error:function(){
        alert('图片上传失败！')
      }
    })
  }
})

$(function(){
  $("#create_subject").addClass("active");
})