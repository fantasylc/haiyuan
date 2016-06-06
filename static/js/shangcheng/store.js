/**
 * Created by liuchao on 16-5-20.
 */
$(document).ready(function(){

    $(".img-thum").mouseover(function(){

        $(".product-img-main img").attr('src',$(this).children('img').attr('src'));
    });

    $("#product-add").click(function(){
        $("#pd-quantity").val(String(Number($("#pd-quantity").val())+1))
    });

    $("#product-sub").click(function(){
        if($("#pd-quantity").val()>1){
        $("#pd-quantity").val(String(Number($("#pd-quantity").val())-1))
        }
    });

    $("#add-to-cart").click(function(){
        var pd_id = $("#pd-id").val();
        var pd_quantity = $("#pd-quantity").val();
        if(pd_id && pd_quantity){
            $.ajax({
                type:'POST',
                url:'/add_cart/',
                data:{'pd_id':pd_id,'pd_quantity':pd_quantity},
                dataType:'json',
                beforeSend:function(xhr){
                    xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                },
                success:function(data,textStatus){
                    var status = data['status'];
                    var message = data['message'];
                    if(status == 'error'){
                        alert(message);
                    }
                    else if(status == 'success'){
                        alert(message);
                        location.reload();
                    }
                },
                error:function(XMLHttpRequest, textStatus, errorThrown){
                    alert(XMLHttpRequest.responseText);
                }
            })
        }
    });

    $("#cart-clear").click(function(){
       $.ajax({
                type:'POST',
                url:'/clearcart/',
                dataType:'json',
                beforeSend:function(xhr){
                    xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                },
                success:function(data,textStatus){
                    var status = data['status'];
                    var message = data['message'];
                    if(status == 'error'){
                        alert(message)
                    }
                    else if(status == 'success'){
                        location.reload();
                    }
                },
                error:function(XMLHttpRequest, textStatus, errorThrown){
                    alert(XMLHttpRequest.responseText);
                }
            })
    });

    $(".cart-del").click(function(){
        var index = $(this).attr("data-index");
        if(index){
            $.ajax({
                    type:'POST',
                    url:'/delcart/',
                    data:{"index":index},
                    dataType:'json',
                    beforeSend:function(xhr){
                        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                    },
                    success:function(data,textStatus){
                        var status = data['status'];
                        var message = data['message'];
                        if(status == 'error'){
                            alert(message)
                        }
                        else if(status == 'success'){
                            location.reload();
                        }
                    },
                    error:function(XMLHttpRequest, textStatus, errorThrown){
                        alert(XMLHttpRequest.responseText);
                    }
                })
            }

    });

    $("#cart-submit").click(function(){
        $.ajax({
                    type:'POST',
                    url:'/submitorder/',
                    dataType:'json',
                    beforeSend:function(xhr){
                        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                    },
                    success:function(data,textStatus){
                        var status = data['status'];
                        var message = data['message'];
                        if(status == 'error'){
                            alert(message)
                        }
                        else if(status == 'success'){

                            location.replace('/submitorder/');
                        }
                    },
                    error:function(XMLHttpRequest, textStatus, errorThrown){
                        alert(XMLHttpRequest.responseText);
                    }
                })
    });

    $('.order-item-main-b').each(function(){
        $(this).css('height',$(this).prev().height()+8);
    });

    $('.order-item-main-c').each(function(){
        $(this).css('height',$(this).prev().height()+8);
    });

    $('.order-item-main-d').each(function(){
        $(this).css('height',$(this).prev().height());
    });
});

