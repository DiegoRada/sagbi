function permite(elEvento, permitidos) {
    // Variables que definen los caracteres permitidos
    var numeros = "0123456789";
    var caracteres = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ_-.,:@";
    var numeros_caracteres = numeros + caracteres;
    var teclas_especiales = [8, 9, 13, 16, 18, 39];
    // 8 = BackSpace, 46 = punto, 39 = flecha derecha
    //var teclas_especiales = [8, 9, 13, 16, 18, 37, 39, 46, 64];
   
    // Seleccionar los caracteres a partir del parámetro de la función
    switch(permitidos) {
        case 'num':
            permitidos = numeros;
            break;
        case 'car':
            permitidos = caracteres;
            break;
        case 'num_car':
            permitidos = numeros_caracteres;
            break;
    }
   
    // Obtener la tecla pulsada 
    var evento = elEvento || window.event;
    var codigoCaracter = evento.charCode || evento.keyCode;
    var caracter = String.fromCharCode(codigoCaracter);
   
    // Comprobar si la tecla pulsada es alguna de las teclas especiales
    // (teclas de borrado y flechas horizontales)
    var tecla_especial = false;
    for(var i in teclas_especiales) {
        if(codigoCaracter == teclas_especiales[i]) {
            tecla_especial = true;
            break;
        }
    }
   
    // Comprobar si la tecla pulsada se encuentra en los caracteres permitidos o si es una tecla especial
    
    return permitidos.indexOf(caracter) != -1 || tecla_especial;
}

/* Funciones Nuevas */ 

function validar_cedula(cedula){

    var cedula = cedula;
    if (cedula.length < 7){
        $("#resultado_cedula_invalida").html('<div class="alert alert-danger text-center" role="alert"><b>La cedula debe tener un minimo de 7 digitos, por favor verifique sus datos.</b></div>');
        document.getElementById("cedula").focus();
        return false;
    }

    return true;

}

function validar_cedula_login(cedula){

    var cedula = cedula;
    if (cedula.length < 7){
        $("#resultado_cedula_invalida_login").html('<div class="alert alert-danger text-center" role="alert"><b>La cedula debe tener un minimo de 7 digitos, por favor verifique sus datos.</b></div>');
        document.getElementById("cedula_login").focus();
        return false;
    }

    return true;

}

function validar_cedula_registro(cedula){

    var cedula = cedula;
    if (cedula.length < 7){
        $("#resultado_cedula_invalida").html('<div class="alert alert-danger text-center" role="alert"><b>La cedula debe tener un minimo de 7 digitos, por favor verifique sus datos.</b></div>');
        document.getElementById("cedula_validacion").focus();
    }

    else {        

        $.ajaxSetup({
            beforeSend: function(xhr, settings){
                $("#resultado_cedula_invalida").html('<p class="msg-azul">Procesando, espere por favor...</p>');
                function getCookie(name){
                    var cookieValue = null;
                    if (document.cookie && document.cookie != '') {
                        var cookies = document.cookie.split(';');
                        for (var i = 0; i < cookies.length; i++){
                            var cookie = jQuery.trim(cookies[i]);
                            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            }
        });

        var parametros = {
            "cedula" : cedula
        };

        $.ajax({
            data:  parametros,
            url:   '/registro-usuario/',
            type:  'post',
            /*beforeSend: function(){
                $("#resultado_cedula_invalida").html('<p class="msg-azul">Procesando, espere por favor...</p>');                       
            },*/
            success:  function (response) {
                $("#resultado_cedula_invalida").html(response);
            }
        });
    }
}

function validar_claves(password, passwordConfirma){

    var password = password;
    var passwordConfirma = passwordConfirma;

    if (password.length < 6){
        $("#resultado_password_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>La clave debe tener un minimo de 6 caracteres, por favor verifique sus datos.</b></div>');
        document.getElementById("inputPassword").focus();
        return false;
    }

    if(password != passwordConfirma){
        $("#resultado_password_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>Las claves no coinciden, por favor verifique sus datos.</b></div>');
        document.getElementById("inputPassword").focus();
        return false;
    }

    return true;

}

function validar_registro_usuario(){

    var cedula = document.getElementById("cedula").value;
    if (cedula.length < 7){
        $("#resultado_form_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>La cedula debe tener un minimo de 7 digitos, por favor verifique sus datos.</b></div>');
        document.getElementById("cedula").focus();
        return false;
    }

    var password = document.getElementById("inputPassword").value;
    var passwordConfirma = document.getElementById("inputPasswordConfirma").value;
    if (password.length < 6){
         $("#resultado_form_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>La clave debe tener un minimo de 6 caracteres, por favor verifique sus datos.</b></div>');
        document.getElementById("inputPassword").focus();
        return false;
    }

    if(password != passwordConfirma){
        $("#resultado_form_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>Las claves no coinciden, por favor verifique sus datos.</b></div>');
        document.getElementById("inputPassword").focus();
        return false;
    }

    return true;
}

function validar_email(email){

    var parametros = {
        "email" : email
    };

    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            $("#resultado_email_invalido").html('<p class="msg-azul">Procesando, espere por favor...</p>');
            function getCookie(name){
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++){
                        var cookie = jQuery.trim(cookies[i]);
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        data:  parametros,
        url:   '/restablecer-password/',
        type:  'post',
        success:  function (response) {
            $("#resultado_email_invalido").html(response);
        }
    });
}

function agregar_pais(pais){

    var parametros = {
        "pais" : pais
    };

    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            $("#resultado_invalido").html('<p class="msg-azul">Procesando, espere por favor...</p>');
            function getCookie(name){
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++){
                        var cookie = jQuery.trim(cookies[i]);
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        data:  parametros,
        url:   '/agregar-pais/',
        type:  'post',
        success:  function (response) {
            $("#resultado_invalido").html(response);
        }
    });
}

function modificar_pais(){

    var parametros = {
        "pais" : $('#pais_modificar').val(),
        "pais_id" : $('#pais_id').val()
    };

    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            $("#resultado_invalido_plus").html('<p class="msg-azul">Procesando, espere por favor...</p>');
            function getCookie(name){
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++){
                        var cookie = jQuery.trim(cookies[i]);
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        data:  parametros,
        url:   '/guardar-modificar-pais/',
        type:  'post',
        success:  function (response) {
            $("#resultado_invalido_plus").html(response);
        }
    });
}

function agregar_director(director){

    var parametros = {
        "director" : director
    };

    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            $("#resultado_invalido").html('<p class="msg-azul">Procesando, espere por favor...</p>');
            function getCookie(name){
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++){
                        var cookie = jQuery.trim(cookies[i]);
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        data:  parametros,
        url:   '/agregar-director/',
        type:  'post',
        success:  function (response) {
            $("#resultado_invalido").html(response);
        }
    });
}

function modificar_director(){

    var parametros = {
        "director" : $('#director_modificar').val(),
        "director_id" : $('#director_id').val()
    };

    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            $("#resultado_invalido_plus").html('<p class="msg-azul">Procesando, espere por favor...</p>');
            function getCookie(name){
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++){
                        var cookie = jQuery.trim(cookies[i]);
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        data:  parametros,
        url:   '/guardar-modificar-director/',
        type:  'post',
        success:  function (response) {
            $("#resultado_invalido_plus").html(response);
        }
    });
}

function agregar_autor(autor){

    var parametros = {
        "autor" : autor
    };

    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            $("#resultado_invalido").html('<p class="msg-azul">Procesando, espere por favor...</p>');
            function getCookie(name){
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++){
                        var cookie = jQuery.trim(cookies[i]);
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        data:  parametros,
        url:   '/agregar-autor/',
        type:  'post',
        success:  function (response) {
            $("#resultado_invalido").html(response);
        }
    });
}

function modificar_autor(){

    var parametros = {
        "autor" : $('#autor_modificar').val(),
        "autor_id" : $('#autor_id').val()
    };

    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            $("#resultado_invalido_plus").html('<p class="msg-azul">Procesando, espere por favor...</p>');
            function getCookie(name){
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++){
                        var cookie = jQuery.trim(cookies[i]);
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        data:  parametros,
        url:   '/guardar-modificar-autor/',
        type:  'post',
        success:  function (response) {
            $("#resultado_invalido_plus").html(response);
        }
    });
}

function validar_pelicula(){

    if(document.getElementById("pais").value == 0){
        $("#resultado_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>Debe seleccionar un país, por favor verifique sus datos.</b></div>');
        document.getElementById("pais").focus();
        return false;
    }

    if(document.getElementById("director").value == 0){
        $("#resultado_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>Debe seleccionar un director, por favor verifique sus datos.</b></div>');
        document.getElementById("director").focus();
        return false;
    }

    $("#resultado_invalido").html('<p class="msg-azul">Procesando, espere por favor...</p>');

    return true;
}

function validar_libro(){

    if(document.getElementById("autor").value == 0){
        $("#resultado_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>Debe seleccionar un Autor, por favor verifique sus datos.</b></div>');
        document.getElementById("autor").focus();
        return false;
    }

    $("#resultado_invalido").html('<p class="msg-azul">Procesando, espere por favor...</p>');

    return true;
}

function validar_valoracion_pelicula(){

    if(document.getElementById("valoracion_pelicula").value == 0){
        $("#resultado_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>Debe seleccionar una valoracion, por favor verifique sus datos.</b></div>');
        document.getElementById("valoracion_pelicula").focus();
        return false;
    }

    $("#resultado_invalido").html('<p class="msg-azul">Procesando, espere por favor...</p>');

    return true;
}

function validar_valoracion_libro(){

    if(document.getElementById("valoracion_libro").value == 0){
        $("#resultado_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>Debe seleccionar una valoracion, por favor verifique sus datos.</b></div>');
        document.getElementById("valoracion_libro").focus();
        return false;
    }

    $("#resultado_invalido").html('<p class="msg-azul">Procesando, espere por favor...</p>');

    return true;
}

function validar_filtro_pelicula(){

    if(document.getElementById("pais").value == 0 && document.getElementById("director").value == 0 && document.getElementById("anio").value == ''){
        $("#resultado_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>Debe seleccionar un parametro para filtrar, por favor verifique sus datos.</b></div>');
        return false;
    }

    return true;
}

function validar_filtro_libro(){

    if(document.getElementById("autor").value == 0){
        $("#resultado_invalido").html('<div class="alert alert-danger text-center" role="alert"><b>Debe seleccionar un parametro para filtrar, por favor verifique sus datos.</b></div>');
        document.getElementById("autor").focus();
        return false;
    }

    return true;
}

$(document).ready(function() {

    $('#form-login').submit(function(){ 
        return validar_cedula_login($('#cedula_login').val()); 
    });

    $('#form-modificar-perfil').submit(function(){ 
        return validar_cedula($('#cedula').val()); 
    });

    $('#form-cambiar-clave').submit(function(){ 
        return validar_claves($('#inputPassword').val(), $('#inputPasswordConfirma').val()); 
    });

    $('#form-pre-registro').submit(function(){ 
        return validar_cedula($('#cedula').val()); 
    });

    $('#form-cedula-registro').submit(function(){
        event.preventDefault();
        validar_cedula_registro($('#cedula_validacion').val()); 
    });

    $('#form-email').submit(function(){ 
        event.preventDefault();
        validar_email($('#email_recupera').val()); 
    });

    $('#form-pais').submit(function(){ 
        event.preventDefault();
        agregar_pais($('#pais').val());
    });

    $('#form-director').submit(function(){ 
        event.preventDefault();
        agregar_director($('#director').val());
    });

    $('#form-autor').submit(function(){ 
        event.preventDefault();
        agregar_autor($('#autor').val());
    });

    $('#form-pelicula').submit(function(){ 
        return validar_pelicula(); 
    });

    $('#form-libro').submit(function(){ 
        return validar_libro(); 
    });

    $('#form-pelicula-valorar').submit(function(){ 
        return validar_valoracion_pelicula(); 
    });

    $('#form-filtro-pelicula').submit(function(){ 
        return validar_filtro_pelicula(); 
    });

    $('#form-filtro-libro').submit(function(){ 
        return validar_filtro_libro(); 
    });



 });