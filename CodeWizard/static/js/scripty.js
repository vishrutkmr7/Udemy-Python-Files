$(document).ready(function(){
    console.log("loaded");
//    $.material.init();


    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        console.log("Submitted", e);
        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });

    $(document).on('submit', '#login-form', function(e){
        e.preventDefault()

        let form = $(this).serialize()
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == 'error'){
                    alert("Can't login");
                } else {
                    console.log("Logged in as " + res);
                    window.location.href = "/";
                }
            }
        })
    });

    $(document).on('click', '#logout-link', function(e){
        e.preventDefault()
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(res){
                if(res == 'success'){
                    window.location.href = '/login';
                } else {
                    alert("Something went wrong");
                    console.log(res)
                }
            }
        })
    });

    $(document).on('submit', '#post-activity', function(e){
        e.preventDefault()
        form = $(this).serialize()
        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function(res){
                console.log(res)
            }
        })
    });

    $(document).on('submit', '#settings-form', function(e){
        e.preventDefault()
        form = $(this).serialize()
        $.ajax({
            url: '/update-settings',
            type: 'POST',
            data: form,
            success: function(res){
                if (res == 'success'){
                    window.location.href = window.location.href;
                } else {
                    alert(res)
                }
            }
        })
    });

    $(document).on('submit', '.comment-form', function(e){
        e.preventDefault()
        form = $(this).serialize()
        $.ajax({
            url: '/submit-comment',
            type: 'POST',
            data: form,
            dataType: 'json',
            success: function(res){
                console.log(res)
            }
        })
    });
});