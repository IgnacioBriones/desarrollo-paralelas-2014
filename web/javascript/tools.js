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
	for ( var j = 0; j < 60; j++) {
		columnas += '<div class = "letra non_match" id = "letra_' + sheetId
				+ '_' + i + '_' + j + '">' + '</div>';
	}
	return columnas;
};

function addPlot(info){
	$(function () {
        $('#performance').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: 'Histograma'
            },
            subtitle: {
                text: 'Frecuencia de palabras'
            },
            xAxis: {
                categories: []
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Cantidad'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: info.series
        });
    });
}
