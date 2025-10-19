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
		//setTimeout(function(){ recognition.start(); }, 400);
	    };
	    
	    recognition.onerror = (event) => {
		window.recognition.stop();
		//setTimeout(function(){ recognition.start(); }, 400);
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
    ws = new WebSocket( 'wss://dragon.foi.hr/wsmmmbn/' );
    window.ws = ws;
    ws.onopen = function() {
	ws.send( 'connect' );
	DONT = false;
	play_part( 'tisina' );
    };
    
    
    
    ws.onmessage = function( msg ) {
	    console.log( msg.data );
        var part = msg.data.toString();
	    console.log( part );
        /*if( part === 'predstavljanje-kratko' )
        {
            play_part( 'predstavljanje-kratko-baltazar' );
            console.log( 'baltazar' );
            setTimeout(function(){
                play_part( 'predstavljanje-kratko-jimi' );
                console.log( 'jimi' );
            }, 7000);
        }
        else*/
	        play_part( part );
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
    
    try{
	recognition.stop();
    }
    catch(e){}
    switch( part )
    {
	case '01':
	    agent.currentTime = 0;
	    end = 3.5;
	    break;
	case '02':
	    agent.currentTime = 3.6;
	    end = 8;
	    break;
	case '03':
	    agent.currentTime = 8;
	    end = 13.6;
	    break;
	case '04':
	    agent.currentTime = 13.7;
	    end = 21.6;
	    break;
	case '05':
	    agent.currentTime = 21.7;
	    end = 29.7;
	    break;
	case '06':
	    agent.currentTime = 29.8;
	    end = 37;
	    break;
	case '07':
	    agent.currentTime = 37.3;
	    end = 44.5;
	    break;
	case '08':
	    agent.currentTime = 44.5;
	    end = 59.5;
	    break;
	case '09':
	    agent.currentTime = 59.5;
	    end = 65.8;
	    break;
	case '10':
	    agent.currentTime = 65.8;
	    end = 70.4;
	    break;
	case '11':
	    agent.currentTime = 70.4;
	    end = 77.5;
	    break;
	case '12':
	    agent.currentTime = 77.5;
	    end = 83.9;
	    break;
	case '13':
	    agent.currentTime = 83.9;
	    end = 92.5;
	    break;
	case '14':
	    agent.currentTime = 92.5;
	    end = 100.6;
	    break;
	case '15':
	    agent.currentTime = 100.6;
	    end = 108.8;
	    break;
	case '16':
	    agent.currentTime = 108.8;
	    end = 115.7;
	    break;
	case '17':
	    agent.currentTime = 115.7;
	    end = 119.3;
	    break;
	case '18':
	    agent.currentTime = 119.3;
	    end = 123.2;
	    break;
	case '19':
	    agent.currentTime = 123.2;
	    end = 128.8;
	    break;
	case '20':
	    agent.currentTime = 128.8;
	    end = 133.1;
	    break;
	case 'dobro':
	    agent.currentTime = 133.1;
	    end = 139.3;
	    break;
	case 'hvala':
	    agent.currentTime = 139.3;
	    end = 141.4;
	    break;
	case 'izvoli':
	    agent.currentTime = 141.4;
	    end = 142.7;
	    break;
	case 'lijepo':
	    agent.currentTime = 142.7;
	    end = 149.9;
	    break;
        case 'ponovi':
            agent.currentTime = 149.9;
            end = 154.6;
            break;
	case 'predstavljanje-dugo':
	    agent.currentTime = 154.6;
	    end = 172.7;
	    break;
	case 'predstavljanje-kratko':
	    agent.currentTime = 172.7;
	    end = 181;
	    break;
	default: // 'tisina'
	    agent.currentTime = 181;
	    end = 202;
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

