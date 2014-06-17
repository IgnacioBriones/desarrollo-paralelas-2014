function changeClass(x,y){
	document.getElementById('a_'+ x + '_' + y).className = "match";
}
// función que dadas las coordenadas del match, cambia el selector de
// "non_match" a "match"

setSheet = function(sheets){
// a cada hoja del html le asigna la hoja del json
	for(var nhoja=0; nhoja < sheets.lengh;nhoja++){
		var sheet = getElementById("sheet"+nhoja)
		for(var nfila=0; nfila<sheets[nhoja].lengh; nfila++){
			for(var ncol=0;ncol<60,ncol++){
				sheet.getElementById('a_'+ nfila + '_' + ncol).innerHTML = sheets[nhoja][nfila,ncol]
			}
		}
	}
}

setMatch = function(matchs){
	//cambia el estilo de las coordenadas en cada hoja en donde existe una ocurrencia
}

