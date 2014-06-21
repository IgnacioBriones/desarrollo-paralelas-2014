function changeClass(x, y) {
	document.getElementById('a_' + x + '_' + y).className = "match";
}
// función que dadas las coordenadas del match, cambia el selector de
// "non_match" a "match"

function changeClass(sheetId, i, j) {
	$('#letra_' + sheetId + '_' + i + '_' + j).className = "letra match";

}

var Sheet = function(sheetId, nfilas) {
	var html = '';
	var pagina = '';
	var filas = '';
	var columnas = '';
	var row = '';
	/* formula para calcular las filas de la matriz */

	for ( var i = 0; i < nfilas; i++) {
		row = row + '<div class = "fila" id = "fila_' + i + '">'
				+ fila(sheetId, i) + '</div>';
	}

	return row;

};

function book(nfilas) {
	libro = '';
	for (i = 0; i < nfilas.length; i++) {
		libro = libro + '<div class = "hoja" id = "hoja_' + i + '">'
				+ Sheet(i, nfilas[i]) + '</div>';
	}
	return '<div class = "libro">' + libro + '</div>';
}

var fila = function(sheetId, i) {
	var columnas = '';
	for ( var j = 0; j < 60; j++) {
		columnas += '<div class = "letra" id = "letra_' + sheetId + '_' + i
				+ '_' + j + '">' + '</div>';
	}
	return columnas;
};
