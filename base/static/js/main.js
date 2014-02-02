
$(document).ready(
    function(){
	$.get( "/api/hospital/2013/03", function( data ) {
	    $( "#results" ).html( data );
	});

	console.log("hello");
    }
) 

