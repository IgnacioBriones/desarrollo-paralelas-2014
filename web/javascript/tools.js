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

function addScatter(info){
	$(function () {
	    $('#scatter').highcharts({
	        chart: {
	            type: 'scatter',
	            zoomType: 'xy'
	        },
	        title: {
	            text: 'Tiempo de busqueda en función del largo de la palabra'
	        },
	        subtitle: {
	            text: 'Fuente: Desempeño del software del código secreto de la biblia'
	        },
	        xAxis: {
	            title: {
	                enabled: true,
	                text: 'largo de la palabra'
	            },
	            startOnTick: true,
	            endOnTick: true,
	            showLastLabel: true
	        },
	        yAxis: {
	            title: {
	                text: 'tiempo (s)'
	            }
	        },
	        legend: {
	            layout: 'vertical',
	            align: 'left',
	            verticalAlign: 'top',
	            x: 100,
	            y: 70,
	            floating: true,
	            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
	            borderWidth: 1
	        },
	        plotOptions: {
	            scatter: {
	                marker: {
	                    radius: 5,
	                    states: {
	                        hover: {
	                            enabled: true,
	                            lineColor: 'rgb(100,100,100)'
	                        }
	                    }
	                },
	                states: {
	                    hover: {
	                        marker: {
	                            enabled: false
	                        }
	                    }
	                },
	                tooltip: {
	                    headerFormat: '<b>{series.name}</b><br>',
	                    pointFormat: '{point.x} , {point.y} s'
	                }
	            }
	        },
	        series: [{name: 'costo temporal',
            color: 'rgba(223, 83, 83, .5)',
            data:info.scatter}]
	    });
	});
	    

}

function addPerformance(info){
	$(function () {
	    $('#tiempo_rank').highcharts({
	        chart: {
	            type: 'scatter',
	            zoomType: 'xy'
	        },
	        title: {
	            text: 'Tiempo de busqueda en función de la cantidad de procesadores'
	        },
	        subtitle: {
	            text: 'Fuente: Desempeño del software del código secreto de la biblia'
	        },
	        xAxis: {
	            title: {
	                enabled: true,
	                text: 'espacio entre letras asociada a la cantidad de procesadores'
	            },
	            startOnTick: true,
	            endOnTick: true,
	            showLastLabel: true
	        },
	        yAxis: {
	            title: {
	                text: 'tiempo promedio (s)'
	            }
	        },
	        legend: {
	            layout: 'vertical',
	            align: 'left',
	            verticalAlign: 'top',
	            x: 100,
	            y: 70,
	            floating: true,
	            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
	            borderWidth: 1
	        },
	        plotOptions: {
	            scatter: {
	                marker: {
	                    radius: 5,
	                    states: {
	                        hover: {
	                            enabled: true,
	                            lineColor: 'rgb(100,100,100)'
	                        }
	                    }
	                },
	                states: {
	                    hover: {
	                        marker: {
	                            enabled: false
	                        }
	                    }
	                },
	                tooltip: {
	                    headerFormat: '<b>{series.name}</b><br>',
	                    pointFormat: '{point.x} , {point.y} s'
	                }
	            }
	        },
	        series: [{name: 'costo temporal',
            color: 'rgba(223, 83, 83, .5)',
            data:info.performance}]
	    });
	});
	    

}