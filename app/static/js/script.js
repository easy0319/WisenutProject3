var INDEX = 0;
$(function() {
  
  $("#chat-submit").click(function(e) {
    e.preventDefault();
    var msg = $("#chat-input").val(); 
    // console.log(msg)
    if(msg.trim() == ''){
      return false;
    }
    generate_message(msg, 'self');
    var buttons = [
        {
          name: 'Existing User',
          value: 'existing'
        },
        {
          name: 'New User',
          value: 'new'
        }
      ];
    // setTimeout(function() {
    //   generate_message('잘 모르겠습니다. 다시 입력해주세요.', 'user');
    // }, 500)

    var postdata = {
      'msg':msg
    }
    // console.log(typeof(postdata))
    $.ajax({
                type: 'POST',
                url: '/',
                data: JSON.stringify(postdata),
                dataType : 'JSON',
                contentType: "application/json; charset=utf-8",
                success: function(data){
                    // console.log(data.result2['msg'])
                    setTimeout(function() {
                      generate_message(data.result2['msg'], 'user');
                    }, 500)
                },
                error: function(request, status, error){
                    // alert('ajax 통신 실패')
                    alert(error);
                }
    })
  })
  function generate_message(msg, type) {
    if (msg.indexOf('|') != -1){
      var m = msg.split('|');
      // console.log('if')
      // console.log(m[0])
      for (var i = 0; i < m.length; i++){
        INDEX++;
        var str="";
        if(i == 0){
          str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
          str += "          <span class=\"msg-avatar\">";
          str += "            <img src=\"../../static/images/avatar.png\">";
          str += "          <\/span>";
          str += "          <div class=\"cm-msg-text\">";
          str += m[i];
          str += "          <\/div>";
          str += "        <\/div><br/><br/><br/><br/>";
        } else{
          str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
          str += "          <input type='button' id='"+INDEX+"' class='primary' onclick='handleBtn("+INDEX+")' value=\'";
          str += m[i];
          str += "          \'/>"
          str += "        <\/div><br/>";
        }
        $(".chat-logs").append(str);
        $("#cm-msg-"+INDEX).hide().fadeIn(300);
        if(type == 'self'){
        $("#chat-input").val(''); 
        }    
        $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);    
      }
    }
    else{
      // console.log('else')
      INDEX++;
      var str="";
      str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
      if(type == 'user'){
        str += "          <span class=\"msg-avatar\">";
        str += "            <img src=\"../../static/images/avatar.png\">";
        str += "          <\/span>";
      }
      str += "          <div class=\"cm-msg-text\">";
      str += msg;
      str += "          <\/div>";
      str += "        <\/div>";
      $(".chat-logs").append(str);
      $("#cm-msg-"+INDEX).hide().fadeIn(300);
      if(type == 'self'){
      $("#chat-input").val(''); 
      }    
      $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);    
    }
  }  
  
  function generate_button_message(msg, buttons){    
    /* Buttons should be object array 
      [
        {
          name: 'Existing User',
          value: 'existing'
        },
        {
          name: 'New User',
          value: 'new'
        }
      ]
    */
  }
  
  $(document).delegate(".chat-btn", "click", function() {
    var value = $(this).attr("chat-value");
    var name = $(this).html();
    $("#chat-input").attr("disabled", false);
    generate_message(name, 'self');
  })
  
  $("#chat-circle").click(function() {    
    $("#chat-circle").toggle('scale');
    $(".chat-box").toggle('scale');
    type = 'user';
    INDEX++;
      var str="";
      str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
      str += "          <span class=\"msg-avatar\">";
      str += "            <img src=\"../../static/images/avatar.png\">";
      str += "          <\/span>";
      str += "          <div class=\"cm-msg-text\">";
      str += "안녕하세요! <br/>\"강아지 백과사전 챗봇 입니다.\"<br/> 질문을 해주세요."
      str += "          <\/div>";
      str += "        <\/div>";
      $(".chat-logs").append(str);
      $("#cm-msg-"+INDEX).hide().fadeIn(300);
      if(type == 'self'){
      $("#chat-input").val(''); 
      }    
      $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);    
  })
  
  $(".chat-box-toggle").click(function() {
    $("#chat-circle").toggle('scale');
    $(".chat-box").toggle('scale');
  })

})

function handleBtn(index) {
  const element = document.getElementById(index);
  // console.log(element.value)
  var postdata = {
    'btn':element.value
  }
  $.ajax({
    type: 'POST',
    url: '/',
    data: JSON.stringify(postdata),
    dataType : 'JSON',
    contentType: "application/json; charset=utf-8",
    success: function(data){
        // console.log(data.result2['btn'])
        setTimeout(function() {
          // generate_message(, 'user');
          type = 'user'
          INDEX++;
          var str="";
          str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
          str += "          <div class=\"cm-msg-text\">";
          str += data.result2['btn'];
          str += "          <\/div>";
          str += "        <\/div>";
          $(".chat-logs").append(str);
          $("#cm-msg-"+INDEX).hide().fadeIn(300);
          if(type == 'self'){
           $("#chat-input").val(''); 
          }    
          $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);          
        }, 500)
    },
    error: function(request, status, error){
        // alert('ajax 통신 실패')
        alert(error);
    }
})
}
