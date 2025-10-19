var DONT = false;
var FIRST = true;
var STOP = false;

$(window).on( 'load', function(){
    counter = 0;
    
    if (navigator.userAgent.indexOf('Firefox') > -1) {
	document.getElementById('notSupported').style.display = 'block';
	document.getElementById('startupute').style.display = 'none';
	document.getElementById('questions').style.display = 'none';
	document.getElementById('output').style.display = 'none';
	document.querySelector('.video-container').style.display = 'none';
    } else {
	const output = document.getElementById('output');
	const button = document.getElementById('start');
	const record = document.getElementById('record');
	window.output = output;
	
	const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
	
	
	
	
	var init = function()
	{
	    recognition = new SpeechRecognition();
	    
	    window.recognition = recognition;
	    
	    recognition.lang = 'hr-HR'; // Croatian
	    recognition.continuous = true;
	    recognition.interimResults = false;
	    
	    recognition.onresult = (event) => {
		const current = event.resultIndex;
		const transcript = event.results[current][0].transcript;
		
		window.recognition.stop();
		STOP = true;
		output.innerHTML = transcript + ' ';
		window.ws.send( transcript );
	    };
	    
	    recognition.onspeechend = () => {
		window.recognition.stop();
	    };
	    
	    recognition.onerror = (event) => {
		window.recognition.stop();
	    };
	}
	init();
	
	button.onclick = () => {
	    if (document.documentElement.requestFullscreen) {
		document.documentElement.requestFullscreen();
	    } else if (document.documentElement.mozRequestFullScreen) { // Firefox
		document.documentElement.mozRequestFullScreen();
	    } else if (document.documentElement.webkitRequestFullscreen) { // Chrome, Safari and Opera
		document.documentElement.webkitRequestFullscreen();
	    } else if (document.documentElement.msRequestFullscreen) { // IE/Edge
		document.documentElement.msRequestFullscreen();
	    }
	    document.querySelector('.video-container').style.display = 'block';
	    if( !isMobileBrowser() )
	    	recognition.start();
	    document.getElementById('startupute').style.display = 'none';
	    document.getElementById('questions').style.display = 'block';
	    play_part( 'tisina' );
	    question( 'bok' );
	    if( isMobileBrowser() )
	    {
		document.getElementById('record').style.display = 'block';
	    }
	};
    }

    record.onclick = () => {
	window.recognition.start();
    }

    $( '#agent' )[0].ontimeupdate = function(){
	var agent = $( '#agent' )[0];
	var the_time = agent.currentTime;
	if( the_time >= END )
	{
	    agent.pause();
	    play_part( 'tisina' );
	    if( !FIRST )
		DONT = true;
	}
	else
	{
	    DONT = false;
	}
    }
    $( '#agent' )[0].loadedmetadata = function(){
	DONT = false;
	play_part( 'tisina' );
    }
});


function connect() {
    ws = new WebSocket( 'wss://dragon.foi.hr/wsiva/' );
    window.ws = ws;
    ws.onopen = function() {
	ws.send( 'connect' );
	DONT = false;
	play_part( 'tisina' );
    };
    
    
    
    ws.onmessage = function( msg ) {
	console.log( msg.data );
	console.log( msg.data.toString() );
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

LAST_PART = ''
CUR_PART = 'tisina';
END = 278;

function play_part( part )
{
    LAST_PART = CUR_PART;
    CUR_PART = part;
    var agent = $( '#agent' )[ 0 ];
    var end = 0;
    
    agent.play()
    
    DONT = (part !== 'tisina')? true : false;
    if( part === 'tisina' ) FIRST = !FIRST
    
    recognition.stop();
    switch( part )
    {
	case '01':
	    agent.currentTime = 0;
	    end = 3;
	    break;
	case '02':
	    agent.currentTime = 3.5;
	    end = 10.5;
	    break;
	case '03':
	    agent.currentTime = 11;
	    end = 20;
	    break;
	case '04':
	    agent.currentTime = 20.5;
	    end = 33;
	    break;
	case '05':
	    agent.currentTime = 33.5;
	    end = 72;
	    break;
	case '06':
	    agent.currentTime = 72.5;
	    end = 111;
	    break;
	case '07':
	    agent.currentTime = 111.5;
	    end = 146;
	    break;
	case '08':
	    agent.currentTime = 146.5;
	    end = 150;
	    break;
	case '09':
	    agent.currentTime = 150.5;
	    end = 165;
	    break;
	case '10':
	    agent.currentTime = 165.5;
	    end = 182;
	    break;
	case '11':
	    agent.currentTime = 182.5;
	    end = 197;
	    break;
	case '12':
	    agent.currentTime = 197.5;
	    end = 210;
	    break;
	case '13':
	    agent.currentTime = 210.5;
	    end = 219;
	    break;
	case '14':
	    agent.currentTime = 219.5;
	    end = 230;
	    break;
	case '15':
	    agent.currentTime = 230.5;
	    end = 252;
	    break;
	case '16':
	    agent.currentTime = 252.5;
	    end = 284;
	    break;
	case '17':
	    agent.currentTime = 284.5;
	    end = 315;
	    break;
	case '18':
	    agent.currentTime = 315.5;
	    end = 324;
	    break;
	case '19':
	    agent.currentTime = 324.5;
	    end = 335;
	    break;
	case '20':
	    agent.currentTime = 335.5;
	    end = 376;
	    break;
        case '21':
            agent.currentTime = 376.5;
            end = 450;
            break;
        case '22':
            agent.currentTime = 450.5;
            end = 495;
            break;
        case '23':
            agent.currentTime = 495.5;
            end = 502;
            break;
        case '24':
            agent.currentTime = 502.5;
            end = 508;
            break;
        case '25':
            agent.currentTime = 508.5;
            end = 552;
            break;
        case '26':
            agent.currentTime = 552.5;
            end = 558;
            break;
	case 'dobro':
	    agent.currentTime = 558.5;
	    end = 562;
	    break;
	case 'hvala':
	    agent.currentTime = 562.5;
	    end = 572;
	    break;
	case 'izvoli':
	    agent.currentTime = 572.5;
	    end = 574;
	    break;
	case 'ponovi':
	    agent.currentTime = 574.5;
	    end = 580.5;
	    break;
	case 'predstavljanje-dugo':
	    agent.currentTime = 580.7;
	    end = 597;
	    break;
	case 'predstavljanje-kratko':
	    agent.currentTime = 597.5;
	    end = 601;
	    break;
	default: // 'tisina'
	    agent.currentTime = 601.5;
	    end = 622;
	    try
	    {
		if( !isMobileBrowser() )
			window.recognition.start();
	    }
	    catch( e ){}
	    break;
    }
    
    END = end;
}


function question( q ) {
    window.recognition.stop();
    window.output.innerHTML = q + ' ';
    window.ws.send( q );
}


function isMobileBrowser() {
  return /Mobi|Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

