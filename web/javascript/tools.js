function changeClass(match) {

	for ( var m in match) {
		for ( var p in match[m].position) {
			for ( var l in match[m].position[p]) {
				var i = match[m].page;
				var j = match[m].position[p][l][0];
				var k = match[m].position[p][l][1];
				$('#letra_' + i + '_' + j + '_' + k).addClass('match').removeClass('non_match');

			}
		}
	}

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
	return '<div class = "libro owl-carousel">' + libro + '</div>';
}

var fila = function(sheetId, i) {
	var columnas = '';
	for ( var j = 0; j < 30; j++) {
		columnas += '<div class = "letra non_match" id = "letra_' + sheetId
				+ '_' + i + '_' + j + '">' + '</div>';
	}
	return columnas;
};
