$(document).ready(function(){


    var cateli = $("#hy_category > *");
    var subitems = $("#hy_popCategory > .sub-item");
    $(".category").mouseover(function(){
        $("#hy_popCategory").show();

        for(var i=0; i<cateli.length; i++){
            cateli[i].index=i;
            cateli[i].onmouseover=function(){

                for(var j=0; j<subitems.length; j++){
                    subitems[j].style.display='none';
                }
                subitems[this.index].style.display='block';
            };
        }

    });

    
    $(".category").mouseout(function(){
        $("#hy_popCategory").hide();

    });



    $('#nav-login').click(function(){
        $('.popover-mask').fadeIn(50);
        $('.theme-popover').show();
    });

    $('.login-title .login-close').click(function(){
        $('.popover-mask').fadeOut(50);
        $('.theme-popover').hide();
    });

    $('#nav-register').click(function(){
        $('.popover-mask').fadeIn(50);
        //$('.popover-mask').;
        $('.reg-popover').show();
    });

    $('.register-title .register-close').click(function(){
        $('.popover-mask').fadeOut(50);
        $('.reg-popover').hide();});

    $("#nav-logout").click(function(){
        $.ajax({
            type:"POST",
            url:"/account/logout/",
            beforeSend:function(xhr){
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            success:function(data,textStatus){
                location.replace("/");
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                alert(XMLHttpRequest.responseText);
            }
        });
        return false;
    });

    $("#login-submit").click(function(){
        if (window.location.search){
            next = window.location.search.split('=')[1];
            next = unescape(next)

        }
        else{
            next = ''
        }
        phone = $('#login-phone').val();
        password = $('#login-pwd').val();
        if(!(phone && password)){
            $('#login-error').html('手机号和密码不能为空!')
        }
        else{
            $.ajax({
                type:'POST',
                url:'/account/login/',
                data:{'phone':phone,"password":password},
                dataType:'json',
                beforeSend:function(xhr){
                    xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                },
                success: function(data,textStatus){
                    var status = data['status'];
                    var message = data['message'];
                    if(status=="failure"){
                        $('#login-error').html('&nbsp;&nbsp;'+message);
                    }
                    else if(status=='success'){
                        alert('登录成功!');
                        if(next.length>1){
                            location.replace(next);
                        }
                        else{
                            location.reload();
                        }

                    }
                    else{
                        alert('异常');
                    }
                    },
                error:function(XMLHttpRequest, textStatus, errorThrown){

                        document.write(XMLHttpRequest.responseText);

                    }
            });
            return false;
        }
    });

    $('#reg-submit').click(function(){

            var phone = $('#reg-phone').val();
            var email = $("#reg-email").val();
            var password1 = $("#reg-pwd1").val();
            var password2 = $("#reg-pwd2").val();
            var rephone =/^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1})| (17[0-9]{1}))+\d{8})$/;
            var re = /^[0-9a-zA-Z\_]+@([0-9a-zA-Z\_\-])+(.[a-zA-Z0-9\-\_])+/;
            if(!rephone.test(phone)){
                $("#reg-error").html('手机号不符合规范');
            }
            else if(!re.test(email)){
                $("#reg-error").html('邮箱不符合规范');
              }
            else if(!(password1 && password2)){
                $("#reg-error").html('密码不能为空');
            }
            else if((password1.length<6) || (password2.length<6)){
                $("#reg-error").html('密码不能少于6位！');
            }
            else if(!(password1 == password2)){
                $("#reg-error").html('两次密码不一致');
                $("reg-pwd1").value ='';
                $("reg-pwd2").value ='';

            }
            else{
                  $.ajax({
                          type:'POST',
                          url:'/account/register/',
                          data:{"phone":phone,"email":email,"password":password2},
                          dataType:'json',
                          beforeSend:function(xhr){
                              alert('before');
                             xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                          },
                          success:function(data,textStatus){
                              var status = data['status'];
                              var message = data['message'];
                              if(status == 'failure'){
                                  $("#reg-error").html(message)
                              }
                              else{
                                  alert(message);
                                  location.reload();
                              }

                          },
                          error:function(XMLHttpRequest, textStatus, errorThrown){
                               alert(XMLHttpRequest.responseText);
                               $('#lala').html(XMLHttpRequest.responseText);
                          }
                  });
                  return false;
                  //alert('haha');

                  }
       });


    $('.uf-item-button').click(function(){
        var nickname = $("#nickname").val();
        var email = $("#email").val();
        var address = $("#address").val();
        var yuanxi = $("#yuanxi").val();
        var shenfen = $("#shenfen").val();
        var xuehao = $("#xuehao").val();
        var realname = $("#realname").val();
        var re = /^[0-9a-zA-Z\_]+@([0-9a-zA-Z\_\-])+(.[a-zA-Z0-9\-\_])+/;
        if (!email){
            $("#uf-email-error").html('邮箱不能为空!');
        }
        else if(!address){
            $("#uf-address-error").html('收货地址不能为空!');
        }
        else if(!realname){
            $("#uf-realname-error").html('真实姓名不能为空!');
        }
        else if(!re.test(email)){
                $("#reg-error").html('邮箱不符合规范');
        }
        else{
            $.ajax({
                          type:'POST',
                          url:'/account/userinfo/',
                          data:{'nickname':nickname,'email':email,'address':address,'shenfen':shenfen,
                          'yuanxi':yuanxi,'xuehao':xuehao,'realname':realname},
                          dataType:'json',
                          beforeSend:function(xhr){
                             xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                          },
                          success:function(data,textStatus){
                              var status = data['status'];
                              var message = data['message'];
                              if(status == 'failure'){
                                  $("#userinfo-error").html(message)
                              }
                              else if(status == 'success'){
                                  alert('提交成功!');
                                  location.reload();
                              }
                              else{
                                  alert('未知错误,请刷新再次尝试!');
                              }

                          },
                          error:function(XMLHttpRequest, textStatus, errorThrown){
                               alert(XMLHttpRequest.responseText);
                          }
                  });
            return false;

        }

        return false;

    });

    $("#passwd-change-submit").click(function(){
        var old_password = $('#id_old_password').val();
        var new_password1 = $('#id_new_password1').val();
        var new_password2 = $('#id_new_password2').val();
        if(!(old_password && new_password1 && new_password2)){
            $('#change-passwd-error').html('选项不能为空!');
        }
        else if(new_password1 != new_password2){
            $('#change-passwd-error').html("<div class='alert alert-danger'>两个新密码不一致!</div>");
        }
        else{
            $.ajax({
                          type:'POST',
                          url:'/account/changepasswd/',
                          data:{'old_password':old_password,'new_password1':new_password1,'new_password2':new_password2},
                          dataType:'json',
                          beforeSend:function(xhr){
                             xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                          },
                          success:function(data,textStatus){
                              var status = data['status'];
                              var message = data['message'];
                              if(status == 'failure'){
                                  var html = "<div class=\"alert alert-danger\">";
                                  for (var key in message){
                                  html += message[key]+"<br/>";
                                  }
                                  html += "</div>";
                                  $('#change-passwd-error').html(html);
                              }
                              else if(status == 'success'){
                                  alert('修改密码成功!');
                                  location.reload();
                              }
                              else{
                                  alert('未知错误,请刷新再次尝试!');
                              }

                          },
                          error:function(XMLHttpRequest, textStatus, errorThrown){
                               alert(XMLHttpRequest.responseText);
                          }
                  });
        }
    });

    $(".fp-btn").click(function(){
        var email = $('#fp-email').val();
        var re = /^[0-9a-zA-Z\_]+@([0-9a-zA-Z\_\-])+(.[a-zA-Z0-9\-\_])+/;
        if(!email){
            $('#fp-error').html("<div class='alert alert-danger'>email不能为空</div>");
        }
        else if(!re.test(email)){
                $("#fp-error").html("<div class='alert alert-danger'>邮箱不符合规范</div>");
        }
        else{
            $.ajax({
                type:'POST',
                url:'/account/forgetpassword/',
                data:{'email':email},
                dataType:'json',
                beforeSend:function(xhr){
                    xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                },
                success:function(data,textStatus){
                    var status = data['status'];
                    var message = data['message'];
                    if(status == 'failure'){
                        $('#fp-error').html("<div class='alert alert-danger'>"+message+"</div>");
                    }
                    else if(status == 'success'){
                        alert(message);
                        location.replace('/');
                    }
                },
                error:function(XMLHttpRequest, textStatus, errorThrown){
                    alert(XMLHttpRequest.responseText);
                }
            })
        }
    });

    $("#rp-btn").click(function(){
        var active_code = window.location.pathname.split('/')[window.location.pathname.split('/').length-2];
        var password1 = $('#rp-password1').val();
        var password2 = $('#rp-password2').val();
        if(!(password1 && password2)){
            $('#rp-error').html("<div class='alert alert-danger'>密码不能为空！</div>");
        }
        else if(password1 != password2){
            $('#rp-error').html("<div class='alert alert-danger'>密码不一致！</div>");
        }
        else if(!active_code){
            $('#rp-error').html("<div class='alert alert-danger'>error!</div>");
        }
        else{
            $.ajax({
                type:'POST',
                url:'/account/confirmreset/',
                data:{'active_code':active_code,'password1':password1,'password2':password2},
                dataType:'json',
                beforeSend:function(xhr){
                    xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                },
                success:function(data,textStatus){
                    var status = data['status'];
                    var message = data['message'];
                    if(status == 'failure'){
                        $('#rp-error').html("<div class='alert alert-danger'>"+message+"</div>");
                    }
                    else if(status == 'success'){
                        alert(message);
                        location.replace('/');
                    }
                },
                error:function(XMLHttpRequest, textStatus, errorThrown){
                    alert(XMLHttpRequest.responseText);
                }
            })
        }
    })


});
window.onload = function(){
    var obth = document.getElementById('btn_returntop');
    var clientHeight = document.documentElement.clientHeight;
    var timer = null;
    var isTop = true;

    window.onscroll=function(){
        var osTop = document.documentElement.scrollTop | document.body.scrollTop;
        if(osTop>=clientHeight){
            obth.style.display = 'block';
        }else{
            obth.style.display = 'none';
        }
        if(!isTop){
            clearInterval(timer);
        }
        isTop = false;
    };
    obth.onclick=function(){
        timer = setInterval(function(){
            var osTop = document.documentElement.scrollTop | document.body.scrollTop;
            var isspeed = Math.floor(-osTop/6);
            document.documentElement.scrollTop = document.body.scrollTop = osTop+isspeed;
            isTop = true;
            if(osTop == 0){
                clearInterval(timer)
            }
        },30);
    };

   };