<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.min.js"></script>	
<title>Computaci&oacute;n Paralela</title>
<link href="style.css" rel="stylesheet" type="text/css" />

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script>
<script src="./javascript/tools.js"></script>


</head>
<?php

if (isset($_FILES['archivo']) && !empty($_FILES['archivo']['name']) && !empty($_POST['tipo_busqueda']) && !empty($_POST['tipo_ejecucion'])){
		
		//variables para la carga de archivo
		$nombre = $_FILES['archivo']['name'];
		$nombre_tmp = $_FILES['archivo']['tmp_name'];
		$tipo = $_FILES['archivo']['type'];
		$tamano = $_FILES['archivo']['size'];
		
		$nombre = str_replace(" ", "_", $nombre);
		$nombre = time()."_".$nombre;
		
		//cargando archivo
		$absPath = realpath(dirname(__FILE__));
		move_uploaded_file($nombre_tmp, $absPath."/subidas/".$nombre);    
}



?>

<script language="javascript">
	
	var info;
	
	window.onbeforeunload = function (e) {
	        alert("hola");
	};
	
	$(document).ready(function() {
		$("#ajax_loading").show();
		$.ajax({
        url: "json.php",
        type: "POST",
        
        data: ({
				nombre : <?php echo "'".$nombre."'"; ?>,
				frases : <?php echo "'".$_POST['frases']."'"; ?>,
				tipo_ejecucion : <?php echo "'".$_POST['tipo_ejecucion']."'"; ?>,
				tipo_busqueda : <?php echo "'".$_POST['tipo_busqueda']."'"; ?>,
				NumeroProcesadores : <?php echo "'".$_POST['NumeroProcesadores']."'"; ?>,
			  }),
		success: function(data){
					info = jQuery.parseJSON(data);
					$("#ajax_loading").hide();

					$('#Resultado').html(book(info.nhojas));
					
					for(var i=0; i<info.sheets.length ;i++){
						for(var j=0; j<info.sheets[i].length; j++){
							for(var k=0; k<60 ; k++){
								$('#letra_'+i+'_'+j+'_'+k).html(info.sheets[i][j][k]);
							}
						}
					}

					changeClass(info.match);
					
					$(".libro").owlCarousel({
					        stopOnHover : true,
					        singleItem : true,
					        transitionStyle:"fade",
					        pagination: true,
					        paginationNumbers: true,
					        scrollPerPage: false,
					        autoHeight: true,
					        navigation: true
     				 	});
		},
		});
	});
</script>
<body>
<div class="content">
  <div id="header">
    <div class="title">
      <h1>Computaci&oacute;n Paralela</h1>
      <br /> 
      <h3>Proyecto final: "El código secreto de La Biblia"</h3>
    </div>
  </div>
  <div id="main">
    <div class="center">

<h1>Resultado</h1>
<img src="/images/ajax.gif" id="ajax_loading" width="100" />
<div id="Resultado">

</div>
</div>
    <div class="leftmenu">
      <div class="nav">
        <ul>
           <li><a href="index.html">Inicio</a></li>
           <li><a href="curso.php">Curso</a></li>
           <li><a href="herramientas.php">Herramientas</a></li>
        </ul>
      </div>
    </div>
</div>

<div id="prefooter"></div>

<div id="footer">
    <div class="padding"> Copyright Curso Computaci&oacute;n Paralela 2014 / Primer Semestre, UTEM  </div>
</div>

</div>

</body>
</html>
