$(window).on( 'load', function(){
	$('body').append( '<div class="barica"><video 300="width" height="450" id="barica" preload="true"><source src="sve-1.2.mp4"  type="video/mp4"></video></div>' ); // autoplay="autoplay"
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
});


function connect() {
	var ws = new WebSocket('ws://localhost:8009');
	ws.onopen = function() {
		// subscribe to some channels
		ws.send( 'connect' );
 	};

	ws.onmessage = function( msg ) {
		console.log( msg.data );
		if( msg.data.toString() == 'da?' )
		{
			console.log( 'da' );
			play_part( 'da profesore' );
		}
		else if( msg.data.toString() == 'dakako' )
		{
			console.log( 'dakako' );
			play_part( 'dakako' );
		}
		else if( msg.data.toString() == 'govor' )
		{
			console.log( 'govor' );
			play_part( 'govor' );
		}
		else if( msg.data.toString() == 'moze' )
		{
			console.log( 'moze' );
			play_part( 'moze' );
		}
		else if( msg.data.toString() == 'nema na cemu' )
		{
			console.log( 'nema na cemu' );
			play_part( 'nema na cemu' );
		}
		else if( msg.data.toString() == 'nema problema' )
		{
			console.log( 'nema problema' );
			play_part( 'nema problema' );
		}
		else if( msg.data.toString() == 'cool projekti' )
		{
			console.log( 'cool projekti' );
			play_part( 'cool projekti' );
		}
		else if( msg.data.toString() == 'predstavljanje' )
		{
			console.log( 'predstavljanje' );
			play_part( 'predstavljanje' );
		}
		else if( msg.data.toString() == 'ucite' )
		{
			console.log( 'ucite' );
			play_part( 'ucite' );
		}
		else if( msg.data.toString() == 'za vas uvijek' )
		{
			console.log( 'za vas uvijek' );
			play_part( 'za vas uvijek' );
		}

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
END = 71;

function play_part( part )
{
	CUR_PART = part;
	var barica = $( '#barica' )[ 0 ];
	var end = 0;
	barica.play()
	switch( part )
	{
		case 'da profesore':
			barica.currentTime = 0;
			end = 3;
			break;
		case 'dakako':
			barica.currentTime = 4;
			end = 5.5;
			break;
		case 'moze':
			barica.currentTime = 6;
			end = 9;
			break;
		case 'nema na cemu':
			barica.currentTime = 10;
			end = 13;
			break;
		case 'nema problema':
			barica.currentTime = 14;
			end = 17;
			break;
		case 'govor':
			barica.currentTime = 20;
			end = 53;
			break;
		case 'tisina':
			barica.currentTime = 53;
			end = 71;
			break;
		case 'cool projekti':
			barica.currentTime = 71;
			end = 76;
			break;
		case 'predstavljanje':
			barica.currentTime = 78;
			end = 93;
			break;
		case 'ucite':
			barica.currentTime = 94;
			end = 98;
			break;
		case 'za vas uvijek':
			barica.currentTime = 100;
			end = 102;
			break;
	}
	END = end;
}





