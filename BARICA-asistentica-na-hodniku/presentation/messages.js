window.onload=function(){
	
	$('body').append( '<div class="barica" id="div_barica"><video 200="width" height="375" id="barica"><source src="video_barica.mp4" type="video/mp4"></video></div>' );
	$( '.step' ).css( right );
	$( '.header' ).css( right );
	$( '.footer' ).css( right );
	$( '.footer' ).css({
		'position': 'absolute',
		'bottom': '0'
	})
	
	var promise = document.querySelector('video').play();

	if (promise !== undefined) {
		promise.then(_ => {
			promise[0].play();
		}).catch(error => {
			$('body').append('<div id="btn_play" onclick="clickPlayVideo()"></div>')
			$("#btn_play").css("background-image","url(http://image.flaticon.com/icons/svg/10/10430.svg)");
		});
	}
	
	$( '#barica' )[0].ontimeupdate = function(){
		var barica = $( '#barica' )[0];
		var the_time = barica.currentTime;
		//console.log( the_time );
		if( the_time >= END )
		{
			barica.pause();
			play_part( 'TISINA' );
		}
	}
	$( '#barica' )[0].loadedmetadata = function(){
		play_part( 'TISINA' );
	}

}

function clickPlayVideo(){
		
	if( $("video").prop('muted') ) {
          $("video").prop('muted', false);
    }
		
	play_part( 'TISINA' );
	
	$('#btn_play').hide();
	
}

function connect() {
	var ws = new WebSocket('ws://localhost:8009');
	ws.onopen = function() {
		// subscribe to some channels
		ws.send( 'connect' );
		toggleMute();
 	};

	ws.onmessage = function( msg ) {
		console.log( msg.data );
		var message_split = msg.data.toString().split(" ");
		if( msg.data.toString() == 'IZVOLI' )
		{
			play_part( 'IZVOLI' );
		}
		else if( msg.data.toString() == 'FOI' )
		{
			play_part( 'FOI' );
		}
		else if( msg.data.toString() == 'KOJA_DVORANA' )
		{
			play_part( 'KOJA_DVORANA' );
		}
		else if( msg.data.toString() == 'KOJI_PROFESOR' )
		{
			play_part( 'KOJI_PROFESOR' );
		}
		else if( msg.data.toString() == 'KOJA_VRSTA_STUDIJA' )
		{
			play_part( 'KOJA_VRSTA_STUDIJA' );
		}
		else if( msg.data.toString() == 'KOJA_GODINA' )
		{
			play_part( 'KOJA_GODINA' );
		}
		else if( msg.data.toString() == 'RASPORED_NE_POSTOJI' )
		{
			play_part( 'RASPORED_NE_POSTOJI' );
		}
		else if( message_split[0] == 'PROFESOR' )
	        {
			if($('#podaci-o-profesoru').next().is('#theImg')){
				$( '#theImg' ).replaceWith('<img id="theImg" style="width: 130%; height: 130%" src="images/professors/'  + message_split[1] + '.png" />');
			}else{
				$('#podaci-o-profesoru').after('<img id="theImg" style="width: 130%; height: 130%" src="images/professors/' + message_split[1] + '.png" />');
			}
			play_part( 'PROFESOR' );
		}
		else if(message_split[0] == 'GROUPS')
		{
			if($('#grupa').next().is('blockquote')){
				$('blockquote').replaceWith(message_split[1]);
			}else{
				$('#grupa').after(message_split[1]);
			}
			play_part( 'KOJA_GRUPA' );
		}
		else if( message_split[0] == 'DVORANA' )
		{
			play_part( message_split[1] );
		}
		else if( msg.data.toString() == 'RASPORED' )
		{
			play_part( 'RASPORED' );
		}
		else if( msg.data.toString() == 'PONOVI' )
		{
			play_part( 'PONOVI' );
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

CUR_PART = 'TISINA';
END = 71;

function play_part( part )
{
	CUR_PART = part;
	var barica = $( '#barica' )[ 0 ];
	var end = 0;
	barica.play()
	switch( part )
	{
		case 'IZVOLI':
			barica.currentTime = 1.2;
			end = 1.7;
			break;
		case 'FOI':
			barica.currentTime = 1.8;
			end = 26;
			break;
		case 'KOJA_DVORANA':
			barica.currentTime = 26;
			end = 27.3;
			break;
		case 'KOJI_PROFESOR':
			barica.currentTime = 27.3;
			end = 28.8;
			break;
		case 'KOJA_VRSTA_STUDIJA':
			barica.currentTime = 29;
			end = 31.8;
			break;
		case 'KOJA_GODINA':
			barica.currentTime = 153.5;
			end = 156.5;
			break;
		case 'KOJA_GRUPA':
			barica.currentTime = 156.8;
			end = 159;
			break;
		case 'RASPORED_NE_POSTOJI':
			barica.currentTime = 159.3;
			end = 163.4;
			break;
		case 'RASPORED_NEDOSTUPAN':
			barica.currentTime = 163.4;
			end = 165.5;
			break;
		case 'PROFESOR':
			barica.currentTime = 165.5;
			end = 167.8;
			break;
		case 'RASPORED':
			barica.currentTime = 168;
			end = 169.2;
			break;
		case 'PONOVI':
			barica.currentTime = 169.5;
			end = 190.5;
			break;
		case 'TISINA':
			barica.currentTime = 171.1;
			end = 190.6;
			break;
		case 'd9':
			barica.currentTime = 32;
			end = 36.3;
			break;
		case 'info':
			barica.currentTime = 36.5;
			end = 41.4;
			break;
		case 'knjiznica':
			barica.currentTime = 41.4;
			end = 45.6;
			break;
		case 'd10':
			barica.currentTime = 45.8;
			end = 50.3;
			break;
		case 'referada':
			barica.currentTime = 50.5;
			end = 54.9;
			break;
		case 'lab5':
			barica.currentTime = 55;
			end = 59.5;
			break;
		case 'skriptarnica':
			barica.currentTime = 59.7;
			end = 64.3;
			break;
		case 'foto':
			barica.currentTime = 64.5;
			end = 69.3;
			break;
		case 'd6':
			barica.currentTime = 69.5;
			end = 73.9;
			break;
		case 'd7':
			barica.currentTime = 78.5;
			end = 82.8;
			break;
		case 'lab12':
			barica.currentTime = 83;
			end = 88;
			break;
		case 'lab13':
			barica.currentTime = 88.2;
			end = 93;
			break;
		case 'lab14':
			barica.currentTime = 93.2;
			end = 98.1;
			break;
		case 'lab15':
			barica.currentTime = 98.3;
			end = 103.2;
			break;
		case 'dekanat':
			barica.currentTime = 103.4;
			end = 108.5;
			break;
		case 'CPSRK':
			barica.currentTime = 108.5;
			end = 116;
			break;
		case 'racunovodstvo':
			barica.currentTime = 116.4;
			end = 121;
			break;
		case 'd4':
			barica.currentTime = 121.2;
			end = 127.2;
			break;
		case 'd11':
			barica.currentTime = 127.3;
			end = 132.2;
			break;
		case 'd1':
			barica.currentTime = 132.3;
			end = 137.5;
			break;
		case 'd2':
			barica.currentTime = 137.7;
			end = 142.5;
			break;
		case 'd8':
			barica.currentTime = 142.6;
			end = 148.6;
			break;
		case 'd3':
			barica.currentTime = 148.8;
			end = 153.5;
			break;
		
	}
	END = end;
}

function toggleMute() {

  var video=document.getElementById("barica");

  if(video.muted){
    video.muted = false;
  } else {
    video.muted = true;
  }

}








