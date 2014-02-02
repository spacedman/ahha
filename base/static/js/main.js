
$(document).ready(
    function(){
	showTable(2013,"03")
	console.log("hello");
    }
) 

function showTable(year, month){
    $.get( "/api/hospital/"+year+"/"+month, function( data ) {
	$( "#results" ).html( "fnord" );
    });
    

}