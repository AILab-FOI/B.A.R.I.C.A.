<html>
	<head>
		<title>Brain4Games Controller</title>
		<link rel="manifest" href="manifest.json">
		<script src="/js/jquery-3.1.0.min.js"></script>
		<script src="/js/hammer.js"></script>
		<script src="/js/NoSleep.js"></script>
		<script type="text/javascript">

window.onload = function () {
	var ws = new WebSocket("{{wsadd}}");
	last_event_lr = 0;
	last_event_ud = 0;

	screen.orientation.lock('landscape');
	nosleepon = false;
	var noSleep = new NoSleep();

	function enableNoSleep() {
		noSleep.enable();
		document.removeEventListener('touchstart', enableNoSleep, false);
	}
		
	function send( ctrl, context )
	{
		ws.send( JSON.stringify( { "cmd":ctrl, "context":context, "game":"{{game}}" } ) )
	}

	if( window.DeviceMotionEvent )
	{
		window.addEventListener("devicemotion", motion, false);
	}
	else
	{
		console.log("DeviceMotionEvent is not supported");
	}


	function motion( event )
	{
		var l = "Accelerometer: "
			+ event.accelerationIncludingGravity.x + ", "
			+ event.accelerationIncludingGravity.y + ", "
			+ event.accelerationIncludingGravity.z;
		console.log( l ); 
	}
	//var window = new Hammer( window );

	if( window.DeviceOrientationEvent )
	{
		window.addEventListener("deviceorientation", orientation, false);
		if( !nosleepon )
		{
			document.addEventListener('touchstart', enableNoSleep, false);
			nosleepon = true;
		}
	}
	else
	{
		console.log("DeviceOrientationEvent is not supported");
	}

	function orientation( event )
	{
		var l = "Magnetometer: "
			+ event.alpha + ", "
			+ event.beta + ", "
			+ event.gamma;
		console.log( l );

		var TH = 10;
		

		if( Math.round( event.beta ) < -TH )
		{
			if( last_event_lr != 'LEFT' )
			{
				last_event_lr = 'LEFT';
				send( "RIGHT", 'stop' );
				/*document.getElementById( 'left' ).innerHTML = "YES";
				document.getElementById( 'right' ).innerHTML = "NO";*/
				send( "LEFT", 'start' );
			}
		}
		else if( Math.round( event.beta ) > TH )
		{
			if( last_event_lr != 'RIGHT' )
			{
				last_event_lr = 'RIGHT';
				send( "LEFT", 'stop' );
				/*document.getElementById( 'left' ).innerHTML = "NO";
				document.getElementById( 'right' ).innerHTML = "YES";*/
				send( "RIGHT", 'start' );
			}
		}
		else
		{
			if( last_event_lr != 0 )
			{
				last_event_lr = 0;
				send( "LEFT", 'stop' );
				/*document.getElementById( 'left' ).innerHTML = "NO";
				document.getElementById( 'right' ).innerHTML = "NO";*/
				send( "RIGHT", 'stop' );
			}
		}

		if( Math.round( event.gamma ) > TH )
		{
			if( last_event_ud != 'UP' )
			{
				last_event_ud = 'UP';
				send( "DOWN", 'stop' );
				/*document.getElementById( 'up' ).innerHTML = "YES";
				document.getElementById( 'down' ).innerHTML = "NO";*/
				send( "UP", 'start' );
			}
		}
		else if( Math.round( event.gamma ) < -TH )
		{
			if( last_event_ud != 'DOWN' )
			{
				last_event_ud = 'DOWN';
				send( "UP", 'stop' );
				/*document.getElementById( 'up' ).innerHTML = "NO";
				document.getElementById( 'down' ).innerHTML = "YES";*/
				send( "DOWN", 'start' );
			}
		} else
		{
			if( last_event_ud != 0 )
			{
				last_event_ud = 0;
				send( "UP", 'stop' );
				/*document.getElementById( 'up' ).innerHTML = "NO";
				document.getElementById( 'down' ).innerHTML = "NO";*/
				send( "DOWN", 'stop' );
			}
		}
		
		/*document.getElementById( 'alpha' ).innerHTML = event.alpha;
		document.getElementById( 'beta' ).innerHTML = event.beta;
		document.getElementById( 'gama' ).innerHTML = event.gamma;*/

	}

}
	</script>
	<style>
html{
    min-height:100%;/* make sure it is at least as tall as the viewport */
    position:relative;
}
body{
    height:100%; /* force the BODY element to match the height of the HTML element */
}
#cloud-container{
    position:absolute;
    top:0;
    bottom:0;
    left:0;
    right:0;
    overflow:hidden;
    z-index:-1; /* Remove this line if it's not going to be a background! */
}
	</style>
	</head>
	<body>
		<div id="cloud-container">
			<button id="left" width="50%" height="100%" style="border:1px solid #000000;width: 50%; height: 100%">A</button>
			<button id="right" width="50%" height="100%" style="border:1px solid #000000;width: 50%; height: 100%">B</button>
		</div>
		<!--<div id="alpha"></div>
		<div id="beta"></div>
		<div id="gama"></div>

		UP: <div id="up">NO</div><br />
		DOWN: <div id="down">NO</div><br />
		LEFT: <div id="left">NO</div><br />
		RIGHT: <div id="right">NO</div><br />-->
	</body>
</html>

