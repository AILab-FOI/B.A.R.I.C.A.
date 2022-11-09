<!DOCTYPE HTML>
<!--
	Forty by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>{{program}} - {{version}}</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="assets/css/main.css" />
		<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
	</head>
	<body>

		<!-- Wrapper -->
			<div id="wrapper">

				% include('templates/header.tpl')

				<!-- Banner -->
				<!-- Note: The "styleN" class below should match that of the header element. -->
					<section id="banner" class="style1">
						<div class="inner">
							<span class="image">
								<img src="images/pic01.png" alt="" />
							</span>
							<header class="major">
								<h1>Games</h1>
							</header>
							<div class="content">
								<p>Play your favorite games.</p>
							</div>
						</div>
					</section>

				<!-- Main -->
					<div id="main">


						<!-- Two -->
							<section id="two" class="spotlights">
								% for name, game in games.items():
								<section>
									<a href="#one" class="image">
										<img src="images/games/{{name}}.png" alt="" data-position="center center" />
									</a>
									<div class="content">
										<div class="inner">
											<header class="major">
												<h3>{{game['title']}}</h3>
											</header>
											<p>{{game['description']}} <br /><br />

											<ul>
												<li> <b>Developer</b>: {{game['developer']}}</li>
												<li> <b>Website</b>: <a href="http://{{game['website']}}">{{game['website']}}</a></li>	
												<li> <b>Players</b>: Up to {{game['players']}}</li>
											</ul>
											<ul class="actions">
												<li><a href="/game/{{name}}/start" class="button next scrolly">Start game</a></li>
												<li><a href="#one" class="button next scrolly">Join game</a></li>
											</ul>
											</p>
										</div>
									</div>
								</section>
								% end
								
					</div>

				

				% include('templates/footer.tpl')

	</body>
</html>
