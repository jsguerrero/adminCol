function validar_contrasena(contrasena2) {
    if (contrasena2.value != document.getElementById('contrasena1').value) {
        contrasena2.setCustomValidity('Las contraseñas no coinciden');
    } else {
        // input is valid -- reset the error message
        contrasena2.setCustomValidity('');
    }
}

function validar_codigo_postal(codigo_postal){
    var url = $("#formulario_registro").attr("url_datos_colonias");  // get the url of the `load_cities` view
    //var codigo_postal = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        typ:'get',
        data: {
            'codigo_postal': codigo_postal // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_cities` view function
            $("#id_colonia").html(data);  // replace the contents of the city input with the data that came from the server
        }
    });
}
