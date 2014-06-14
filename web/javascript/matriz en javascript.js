/*tareas
 * 
 * hacer una función que tome una matriz de
 * 
 * */

var PrintPage = function(sheet) {
	/*
	 * toma un array llamado sheet y la pinta en el html
	 * 
	 * mediante la asignacion de la forma
	 * 
	 * 
	 */
	var m = sheet.lenth;
	var n = sheet[0].lenth;
	for ( var i = 0; i < n; i++) {
		for ( var j = 0; j < m; j++) {
			document.getElementById('a_' + i + '_' + j).value = sheet[i][j];
		}

	}

}

var PrintMatch=function(match){
	/*toma un conjunto de letras en donde ocurre el match y las cambia de estilo*/
	
	var jump = match.jump;
	var position = match.position;
	var page = match.page;
	
	/*seleccionar la página del dom*/
	var p = document.getElementById('page');
	/*convertir la posicion a las coordenadas de una página*/
	
	/*convertirlo en una lista de coordenadas*/
	
	/*a cada elemento de la coordenada cambiar la clase de non_match a match*/
	}


var Sheet = function(nfilas) {
	var html = '';
	var pagina = '';
	var filas = '';
	var columnas = '';
	var row = '';
	/* formula para calcular las filas de la matriz */

	for ( var i = 0; i < nfilas; i++) {
		row = row + '<div class = "fila" id = "a_' + i + '">' + fila(i)
				+ '</div>';
	}
	return row;

}

var fila = function(i) {
	var columnas = '';
	for ( var j = 0; j < 60; j++) {
		columnas += '<div class = "letra" id = "a_' + i + '_' + j + '">'
				+ '</div>';
	}
	return columnas;
}
