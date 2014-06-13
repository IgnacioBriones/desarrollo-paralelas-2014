var Sheet = function(nfilas){
var html = '';
var pagina = '';
var filas = '';
var columnas = '';
var row = '';
/*formula para calcular las filas de la matriz*/

for (var i = 0; i < nfilas; i++){
	row = row+'<div class = "fila" id = "a_'+i+'">'+fila(i)+'</div>';
}
return row;

}

var fila = function(i){
	var columnas = '';
	for (var j = 0; j < 60; j++){
		columnas+='<div class = "letra" id = "a_'+i+'_'+j+'">'+'</div>';  
	}
	return columnas;
}
