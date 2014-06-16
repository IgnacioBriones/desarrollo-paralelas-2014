function changeClass(x,y){

	if(document.getElementById('a_'+ x + '_' + y).className == "non_match") 
		document.getElementById('a_'+ x + '_' + y).className = "match";
	else
		document.getElementById('a_'+ x + '_' + y).className = "non_match"; 	
}
//función que dadas las coordenadas del match, cambia el selector de "non_match" a "match"
