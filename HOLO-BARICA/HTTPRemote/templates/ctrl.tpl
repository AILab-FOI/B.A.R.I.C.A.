<html>
	<head>
		<title>Brain4Games Controller</title>
	</head>
	<script src="/js/jquery-3.1.0.min.js"></script>
	<script src="/js/hammer.js"></script>
	<script src="/js/NoSleep.js"></script>
	<script type="text/javascript">
window.onload = function () {
    var ImageMap = function (map) {
            var n,
                areas = map.getElementsByTagName('area'),
                len = areas.length,
                coords = [],
                previousWidth = 344;
            for (n = 0; n < len; n++) {
                coords[n] = areas[n].coords.split(',');
            }
            this.resize = function () {
                var n, m, clen,
                    x = document.body.clientWidth / previousWidth;
                for (n = 0; n < len; n++) {
                    clen = coords[n].length;
                    for (m = 0; m < clen; m++) {
                        coords[n][m] *= x;
                    }
                    areas[n].coords = coords[n].join(',');
                }
                previousWidth = document.body.clientWidth;
                return true;
            };
            window.onresize = this.resize;
        },
        imageMap = new ImageMap(document.getElementById('ctrls'));
		imageMap.resize();
	
	
	
		var ws = new WebSocket("{{wsadd}}");
		
		function send( ctrl, context )
		{
			ws.send( JSON.stringify( { "cmd":ctrl, "context":context, "game":"{{game}}" } ) )
		}
		
		$('.cbutton').on( 'mousedown touchstart', function( event ){
			event.stopPropagation();
			event.preventDefault();
			if(event.handled !== true) {

				send( $( this ).attr('alt'), 'start' );
				window.navigator.vibrate(100); 

				event.handled = true;
			} else {
				return false;
			}
		});
		
		$('.cbutton').on( 'mouseup click touchend touchcancel', function( event ){
			event.stopPropagation();
			event.preventDefault();
			if(event.handled !== true) {

				send( $( this ).attr('alt'), 'stop' );

				event.handled = true;
			} else {
				return false;
			}
		});
		
		var img = document.getElementById('imgctrl');
		var mc = new Hammer(img);
		
		var UP = new Hammer( document.getElementById('UP') );
		UP.on( "tap", function( ev ){
			event.stopPropagation();
			event.preventDefault();
			send( "UP", 'start' );
			send( "UP", 'stop' );
		});
		UP.on( "press", function( ev ){
			event.stopPropagation();
			event.preventDefault();
			send( "UP", 'start' );
		});
		
		var DOWN = new Hammer( document.getElementById('DOWN') );
		DOWN.on( "tap", function( ev ){
			event.stopPropagation();
			event.preventDefault();
			send( "DOWN", 'start' );
			send( "DOWN", 'stop' );
		});
		DOWN.on( "press", function( ev ){
			event.stopPropagation();
			event.preventDefault();
			send( "DOWN", 'start' );
		});
		
		var LEFT = new Hammer( document.getElementById('LEFT') );
		LEFT.on( "tap", function( ev ){
			event.stopPropagation();
			event.preventDefault();
			send( "LEFT", 'start' );
			send( "LEFT", 'stop' );
		});
		LEFT.on( "press", function( ev ){
			event.stopPropagation();
			event.preventDefault();
			send( "LEFT", 'start' );
		});
		
		var RIGHT = new Hammer( document.getElementById('RIGHT') );
		RIGHT.on( "tap", function( ev ){
			event.stopPropagation();
			event.preventDefault();
			send( "RIGHT", 'start' );
			send( "RIGHT", 'stop' );
		});
		RIGHT.on( "press", function( ev ){
			event.stopPropagation();
			event.preventDefault();
			send( "RIGHT", 'start' );
		});
		
		var SELECT = new Hammer( document.getElementById('SELECT') );
		SELECT.on( "tap", function( ev ){
			send( "SELECT", 'start' );
			send( "SELECT", 'stop' );
		});
		SELECT.on( "press", function( ev ){
			send( "SELECT", 'start' );
		});
		
		var START = new Hammer( document.getElementById('START') );
		START.on( "tap", function( ev ){
			send( "START", 'start' );
			send( "START", 'stop' );
		});
		START.on( "press", function( ev ){
			send( "START", 'start' );
		});
		
		var A = new Hammer( document.getElementById('A') );
		A.on( "tap", function( ev ){
			send( "A", 'start' );
			send( "A", 'stop' );
		});
		A.on( "press", function( ev ){
			send( "A", 'start' );
		});
		
		var B = new Hammer( document.getElementById('B') );
		B.on( "tap", function( ev ){
			send( "B", 'start' );
			send( "B", 'stop' );
		});
		B.on( "press", function( ev ){
			send( "B", 'start' );
		});
		
		
	}
	</script>
	<body bgcolor="#000000"  style="-webkit-touch-callout: none !important;" oncontextmenu="return false" >
	<img id="imgctrl" src="/images/nes-ctrl.png" width="100%" usemap="#ctrls" style="-webkit-touch-callout: none !important;" /><!-height="181"-->
	<map name="ctrls" id="ctrls">
		<area class="cbutton" shape="rect" coords="40,50,74,81" href="javascript:void(0)"  alt="UP" id="UP"/>
		<area class="cbutton" shape="rect" coords="40,107,74,129" href="javascript:void(0)"  alt="DOWN" id="DOWN"/>
		<area class="cbutton" shape="rect" coords="15,77,47,110" href="javascript:void(0)"  alt="LEFT" id="LEFT"/>
		<area class="cbutton" shape="rect" coords="73,77,105,110" href="javascript:void(0)"  alt="RIGHT" id="RIGHT"/>
		<area class="cbutton" shape="rect" coords="119,102,160,119" href="javascript:void(0)"  alt="SELECT" id="SELECT"/>
		<area class="cbutton" shape="rect" coords="163,102,204,119" href="javascript:void(0)"  alt="START" id="START"/>
		<area class="cbutton" shape="rect" coords="273,91,309,129" href="javascript:void(0)"  alt="A" id="A"/>
		<area class="cbutton" shape="rect" coords="227,91,265,129" href="javascript:void(0)"  alt="B" id="B"/>
	</map>
	</body>
</html>
