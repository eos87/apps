function enviar() {
		nombre1 = $('#id_nombre').val();
		e_mail = $('#id_email').val();
		comentario = $('#id_mensaje').val();
		if(document.sugF.nombre.value.length!=0 && document.sugF.mensaje.value.length!=0 && document.sugF.email.value.length!=0)
		{
			$.post("/enviar/",	{
				nombre: nombre1,
				email: e_mail,
    			mensaje: comentario},

    		function(data) {
				if (data != "ERROR") {
                    parent.jQuery.modal.close();
        			//parent.dialog.modal('close');
        			/*top.location.href = document.referrer;*/
            	}
			}, "json");
		}/*cierro IF*/
		else{
			alert("Debe llenar los campos requeridos!");
			return false;
		}
		return false;
    }/*cierro la funcion enviar*/

$(document).ready(function () {
	$("#comment-form").submit(enviar);
	//alert(parent.$.modal);
});

/*Funciones necesarios para el uso del campo webite*/
$(function(){
	$('#id_site').click(function() {
		var site = $('#id_site').val();
  			if(site == 'www.tu-web.com'){
  				$('#id_site').val('');
  			}
	});
});

$(function(){
	$('#id_site').blur(function() {
		var site = $('#id_site').val();
  			if(site == ''){
  				$('#id_site').val('www.tu-web.com');
  			}
	});
});

