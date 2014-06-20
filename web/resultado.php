<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
<script src="./matriz en javascript.js"></script>
<title>Computaci&oacute;n Paralela</title>
<link href="style.css" rel="stylesheet" type="text/css" />

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script>
<script src="./javascript/tools.js"></script>
<script >
	var info 
	$(document).ready(function() {
		$("#ajax_loading").show();
		$.ajax({
        url: "json.php",
        type: "POST",
        
        data: ({
				nombre : <?php echo "'".$_FILES['archivo']['name']."'"; ?>,
				frases : <?php echo "'".$_POST['frases']."'"; ?>,
				tipo_ejecucion : <?php echo "'".$_POST['tipo_ejecucion']."'"; ?>,
				tipo_busqueda : <?php echo "'".$_POST['tipo_busqueda']."'"; ?>,
				NumeroProcesadores : <?php echo "'".$_POST['NumeroProcesadores']."'"; ?>,
			  }),
		success: function(data){
					info = jQuery.parseJSON(data);
					$("#ajax_loading").hide();
					alert(data);
					alert("Finalizado...");
		},
		});
	});
</script>

</head>

<body>
<div class="content">
  <div id="header">
    <div class="title">
      <h1>Computaci&oacute;n Paralela</h1>
      <br /> 
      <h3>Proyecto final: "Código secreto de la Biblia"</h3>
    </div>
  </div>
  <div id="main">
    <div class="center">

<h1>Resultado</h1>
<img src="/images/ajax.gif" id="ajax_loading" width="100" />
<div id="Resultado">

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

<script>
	// la informacion ya esta en la variable info
	libro = info.sheets;
	match = info.match;
	
</script>

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
    <div class="padding"> Copyright Curso Computaci&oacute;n Paralela 2014 / Primer Semestre, UTEM </div>
</div>

</div>

</body>
</html>
