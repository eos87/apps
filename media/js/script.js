function enviar() {
    nombre = $('#id_poster').val();
    wsite = $('#id_website').val();
    comentario = $('#id_coment').val();
    date = obtenerFecha();
    hour = obtenerHora();
    if(document.postF.poster.value.length!=0 && document.postF.coment.value.length!=0){
        $.post("/add/",	{
            poster: nombre,
            website: wsite,
            coment: comentario,
            fecha: date,
            hora: hour
        },

        function(data) {
            if (data != "ERROR") {
                var item = '<p class="test"><a href="';
                item += data.poster;
                item += '">'
                item += data.poster;
                item += '</a><span id="dots"> :</span><br />'
                item += data.coment;
                item += '<br /><span class="fecha_hora"><small>';
                item += data.fecha;
                item += '&nbsp;&nbsp;';
                item += data.hora;
                item += '</small></span></p>';
                $("#saved").prepend(item);
                $("#comment-form")[0].reset();
                $('#tracker').html('140');
            }
        }, "json");
    }/*cierro IF*/
    else{
        alert("Introduzca un nombre y un mensaje!");
        return false;
    }
    return false;
}/*cierro la funcion enviar*/

$(document).ready(function () {
    $('#id_poster').val('Nombre');
    $('#id_coment').val('Escribi tu mensaje');

    $('#id_poster').focus(function(){
        if ( $(this).val() == 'Nombre'){
            $(this).val('');
        }
    });
    $('#id_poster').blur(function(){
        if ( $(this).val() == ''){
            $(this).val('Nombre');
        }
    });
    $('#id_coment').focus(function(){
        if ( $(this).val() == 'Escribi tu mensaje'){
            $(this).val('');
        }
    });
    $('#id_coment').blur(function(){
        if ( $(this).val() == ''){
            $(this).val('Escribi tu mensaje');
        }
    });
    $("#comment-form").submit(enviar);
});

function obtenerFecha(){
    var mydate=new Date();
    var anio=mydate.getYear();
    if (anio < 1000)
        anio+=1900;
    var mes=mydate.getMonth()+1;
    if (mes<10)
        mes="0"+mes;
    var dia=mydate.getDate();
    if (dia<10)
        dia="0"+dia;
    fechaTotal = anio + "-" + mes + "-" + dia;
    return fechaTotal;
}

function obtenerHora(){
    var mydate = new Date();
    var hora = mydate.getHours();
    var minuto = mydate.getMinutes();
    var ampm = "";

    if(minuto<10)
        minuto = "0"+minuto;

    if(hora>12){
        hora -= 12;
        ampm = " PM";
    }else ampm = " AM";

    if(hora<10)
        hora = "0"+hora;

    horaTotal = hora + ":" + minuto + ampm;

    return horaTotal;
}

