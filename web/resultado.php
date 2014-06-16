<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.min.js"></script>

<title>Computaci&oacute;n Paralela</title>
<link href="style.css" rel="stylesheet" type="text/css" />

<script> </script>

</head>

<body>
<div class="content">
  <div id="header">
    <div class="title">
      <h1>Computaci&oacute;n Paralela</h1>
      <br /> 
      <h3>Proyecto final: "Procesamiento de Texto"</h3>
    </div>
  </div>
  <div id="main">
    <div class="center">
<h1>Resultado</h1>
<br /> 
<br />

<div id="Resultado">

<?php
 
/*if( !isset($_FILES['archivo']) ){
  echo 'Ha habido un error, tienes que elegir un archivo<br/>';
  echo '<a href="index.html">Subir archivo</a>';

}else{
 
  $nombre = $_FILES['archivo']['name'];
  $nombre_tmp = $_FILES['archivo']['tmp_name'];
  $tipo = $_FILES['archivo']['type'];
 
  $ext_permitidas = array('pdf');
  $partes_nombre = explode('.', $nombre);
  $extension = end( $partes_nombre );
  $ext_correcta = in_array($extension, $ext_permitidas);
 
  $tipo_correcto = preg_match('/^(application\/(doc|pdf|docx)$/',$tipo);
 
  /*$limite = 500 * 1024;*/
 
  /*if( $ext_correcta && $tipo_correcto){
    
      if( $_FILES['archivo']['error'] > 0 ){

            echo 'Error: ' . $_FILES['archivo']['error'] . '<br/>';
     
      }else{

      echo 'Nombre: ' . $nombre . '<br/>';
      echo 'Tipo: ' . $tipo . '<br/>';
      echo 'Tamaño: ' . ($tamano / 1024) . ' Kb<br/>';
      }
}*/

if (isset($_FILES['archivo']) && !empty($_FILES['archivo']['name']) && !empty($_POST['tipo_busqueda']) && !empty($_POST['tipo_ejecucion']))
	{
		
		//variables para la carga de archivo
		$nombre = $_FILES['archivo']['name'];
		$nombre_tmp = $_FILES['archivo']['tmp_name'];
		$tipo = $_FILES['archivo']['type'];
		$tamano = $_FILES['archivo']['size'];
		
		$nombre = str_replace(" ", "_", $nombre);

		$caracteres = array('(', ')',"'", "\"","");
		$nombre = str_replace($caracteres, "", $nombre);
		
		$nombre = time()."_".$nombre;
		
		//cargando archivo
		move_uploaded_file($nombre_tmp, "subidas/" . $nombre);
		
		
		if($_POST['tipo_ejecucion'] == "Secuencial")
		{
			if($_POST['tipo_busqueda'] == "Explicita")
			{
				//Secuencial Explicito
				$consulta_secuencial_explicita = "python /mpi/desarrollo-paralelas-2014/shellSerialExplicit.py"." "."/mpi/desarrollo-paralelas-2014/web/subidas/".$nombre." '".$_POST['frases']."'";
				$salida = shell_exec($consulta_secuencial_explicita);
				#echo $consulta_secuencial_explicita;
				echo nl2br($salida);
			}
			else
			{
				//Secuencial Implicito
				$consulta_secuencial_implicita = "python /mpi/desarrollo-paralelas-2014/shellSerialImplicit.py"." "."/mpi/desarrollo-paralelas-2014/web/subidas/".$nombre;
				$salida = shell_exec($consulta_secuencial_implicita);
				#echo $consulta_secuencial_implicita;
				echo nl2br($salida);
			}
		}
		else
		{
			if($_POST['tipo_busqueda'] == "Explicita")
			{
				//Paralelo Explicito
				$consulta_paralela_explicita = "mpiexec "."-n ".$_POST['NumeroProcesadores']." --hostfile /mpi/desarrollo-paralelas-2014/hostfile"." python /mpi/desarrollo-paralelas-2014/shellParallelExplicit.py"." "."/mpi/desarrollo-paralelas-2014/web/subidas/".$nombre." '".$_POST['frases']."'";
				$salida = shell_exec($consulta_paralela_explicita);
				#echo $consulta_paralela_explicita;
				echo nl2br($salida);
				echo shell_exec("echo $USER");
			}
			else
			{
				//Paralelo Implicito
				$consulta_paralela_implicita = "mpiexec "."-n ".$_POST['NumeroProcesadores']." --hostfile /mpi/desarrollo-paralelas-2014/hostfile"." python /mpi/desarrollo-paralelas-2014/shellParallelImplicit.py"." "."/mpi/desarrollo-paralelas-2014/web/subidas/".$nombre;
				$salida = shell_exec($consulta_paralela_implicita);	
				#echo $consulta_paralela_implicita;
				echo nl2br($salida);
			}
		}
		
    echo "<br /><br />";
	}
?>

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
 <div id="prefooter">
 </div>
  <div id="footer">
    <div class="padding"> Copyright Curso Computaci&oacute;n Paralela 2014 / Primer Semestre, UTEM </div>
  </div>
</div>
</body>
</body>
</html>
