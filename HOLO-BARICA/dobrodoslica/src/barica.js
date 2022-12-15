$(window).on( 'load', function(){
	 // autoplay="autoplay"
	$( '.step' ).css( right );
	$( '.header' ).css( right );
	$( '.footer' ).css( right );
	$( '.footer' ).css({
		'position': 'absolute',
		'bottom': '0'
	})
	$( '#barica' )[0].ontimeupdate = function(){
		var barica = $( '#barica' )[0];
		var the_time = barica.currentTime;
		console.log( the_time );
		if( the_time >= END )
		{
			barica.pause();
			play_part( 'tisina' );
		}
	}
	$( '#barica' )[0].loadedmetadata = function(){
		play_part( 'tisina' );
	}
	document.body.addEventListener("mouseclick", function () {
		play_part( 'tisina' );
		document.body.removeEventListener( "mousclick", this );
	});
});


function connect() {
	var ws = new WebSocket('ws://localhost:8009');
	ws.onopen = function() {
		// subscribe to some channels
		ws.send( 'connect' );
 	};

	ws.onmessage = function( msg ) {
		console.log( msg.data );
		play_part( msg.data.toString() );
	};

	ws.onclose = function(e) {
		console.log( 'Socket is closed. Reconnect will be attempted in 1 second.', e.reason );
		setTimeout(function() {
			connect();
		}, 1000);
	};

	ws.onerror = function(err) {
		console.error( 'Socket encountered error: ', err.message, 'Closing socket' );
		ws.close();
	};
}

connect();

right = { 
	'text-align': 'right',
	'width': '1000px',
	'margin-right': '-400px auto'
};

CUR_PART = 'tisina';
END = 40;
STARTED = false;

function play_part( part )
{
	CUR_PART = part;
	var barica = $( '#barica' )[ 0 ];
	var end = 0;
	barica.play()
	switch( part )
	{
		case 'dobrodosli':
			barica.currentTime = 0;
			end = 1.5;
			break;
		case 'dobrodosli na dan fakulteta':
			barica.currentTime = 1.5;
			end = 4;
			break;
		case 'lijepo vas je vidjeti':
			barica.currentTime = 4;
			end = 6.5;
			break;
		case 'dobrodosli na dan FOI':
			barica.currentTime = 6.5;
			end = 11;
			break;
		case 'dobar dan, dobrodosli':
			barica.currentTime = 11;
			end = 13.5;
			break;
		case 'kako ste':
			barica.currentTime = 13.5;
			end = 15;
			break;
		case 'tisina':
			barica.currentTime = 20;
			end = 40;
			break;
		case 'drago mi je vas pozdraviti':
			barica.currentTime = 15;
			end = 17.5;
			break;
	}
	END = end;
}





