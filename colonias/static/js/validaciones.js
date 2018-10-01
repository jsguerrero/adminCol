function validar_contrasena(contrasena2) {
    if (contrasena2.value != document.getElementById('contrasena1').value) {
        contrasena2.setCustomValidity('Las contraseñas no coinciden');
    } else {
        // input is valid -- reset the error message
        contrasena2.setCustomValidity('');
    }
}

var response_cache = {};

function validar_codigo_postal(){
    var codigo_postal = $("#id_codigo_postal").val();
    var url = $("#formulario_registro").attr("url_datos_colonias");  // get the url of the `load_cities` view

    if (codigo_postal){
        $("#id_codigo_postal").html("")
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            type:'GET',
            data: {
                'codigo_postal': codigo_postal // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_cla_asentamiento").html(data);  // replace the contents of the city input with the data that came from the server
            }
        });
    }
}

$(document).ready(function() {
    $("#id_codigo_postal").on("change", validar_codigo_postal);
});

/*
validar_codigo_postal($(this).val()));
function getMunicipios() {
    var estadoId = $("#id_estado").val();
    if (estadoId) {
        // Eliminamos las opciones anteriores del select
        $("#id_municipio").html("");
        var request = $.ajax({
            type: "GET",
            url: "{% url 'get_municipios' %}",
            data: {
                "estado_id": estadoId,
            },
        });
        request.done(function(response) {
            // Agregamos los resultados al select
            $("#id_proceso").html(response.municipios);
            $("#id_localidad").html("<option value='' selected='selected'>---------</option>");
            $("#id_municipio, #id_localidad").trigger("change");
        });
    } else {
        $("#id_municipio").html("<option value='' selected='selected'>---------</option>");
        $("#id_localidad").html("<option value='' selected='selected'>---------</option>");
        $("#id_municipio, #id_localidad").trigger("change");
    }
}*/
