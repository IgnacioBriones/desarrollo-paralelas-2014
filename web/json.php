<?php

$nombre = $_POST['nombre'];
$nombre = str_replace(" ", "_", $nombre);
$nombre = time()."_".$nombre;
//echo $_POST['tipo_busqueda'].' '.$nombre.' '.$_POST['frases'].' '.$_POST['tipo_ejecucion'].' '.$_POST['NumeroProcesadores'];

		if($_POST['tipo_ejecucion'] == "Secuencial")
		{
			if($_POST['tipo_busqueda'] == "Explicita")
			{
				//Secuencial Explicito
				$consulta_secuencial_explicita = "python ./../shellSerialExplicit.py"."  "."./../web/subidas/".$nombre." '".$_POST['frases']."'";
				$salida = shell_exec($consulta_secuencial_explicita);
				//echo $consulta_secuencial_explicita;
				echo $salida;
			}
			else
			{
				//Secuencial Implicito
				$consulta_secuencial_implicita = "python ./../shellSerialImplicit.py"."  "."./../web/subidas/".$nombre;
				$salida = shell_exec($consulta_secuencial_implicita);
				//echo $consulta_secuencial_implicita;
				echo $salida;
			}
		}
		else
		{
			if($_POST['tipo_busqueda'] == "Explicita")
			{
				//Paralelo Explicito
				$consulta_paralela_explicita = "sudo -u cluster mpiexec "."-n ".$_POST['NumeroProcesadores']." --hostfile ./../hostfile"."  "."python ./../shellParallelExplicit.py"." "."./../web/subidas/".$nombre." '".$_POST['frases']."'";
				$salida = shell_exec($consulta_paralela_explicita);
				//echo $consulta_paralela_explicita;
				echo $salida;
			}
			else
			{
				//Paralelo Implicito
				$consulta_paralela_implicita = "sudo -u cluster mpiexec "."-n ".$_POST['NumeroProcesadores']." --hostfile ./../hostfile"."  "."python ./../shellParallelImplicit.py"." "."./..//web/subidas/".$nombre;
				$salida = shell_exec($consulta_paralela_implicita);	
				//echo $consulta_paralela_implicita;
				echo $salida;
			}
		}
?>
