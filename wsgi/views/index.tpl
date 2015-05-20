<!DOCTYPE html>
<!--
	Transit by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Transit by TEMPLATED</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<!--[if lte IE 8]><script src="js/html5shiv.js"></script><![endif]-->
		<script src="static/js/jquery.min.js"></script>
		<script src="static/js/skel.min.js"></script>
		<script src="static/js/skel-layers.min.js"></script>
		<script src="static/js/init.js"></script>
		<noscript>
			<link rel="stylesheet" href="static/css/skel.css" />
			<link rel="stylesheet" href="static/css/style.css" />
			<link rel="stylesheet" href="static/css/style-xlarge.css" />
		</noscript>
	</head>
	<body class="landing">


		<!-- Banner -->
			<section id="banner">
				<h2>Map Search</h2>
				<p>Esto es un un buscador de destinos</p>
				<ul class="actions">
					<li>
						<a href="#one" class="button big">Buscador</a>
					</li>
				</ul>
			</section>
<!-- One -->
			<section id="one" class="wrapper style1 special">
				<div class="container">
					<header class="major">
						<h2>Buscador</h2>
						<p>Introduce los datos en el formulario</p>
					</header>
					<div>
						<form action="busqueda" method="post">
							Tu ubicacion: <input name="ubicacion" type="text" /></br>
							Lugar:
							<select name="lugar">
								<option value="restaurant">Restaurante</option>
								<option value="museum">Museo</option>
								<option value="shopping_mall">Centro comercial</option>
								<option value="movie_theater">Cine</option>
								<option value="hospital">Hospital</option>
								<option value="police">Policia</option>
							</select></br>
							Radio: <input name="radio" type="text" /></br>
							<input value="Enviar" type="submit" />
						</form>
					</div>
				</div>
			</section>

		<!-- Footer -->
			<footer id="footer">
				<div class="container">
					<div class="8u 12u$(medium)">
						<ul class="copyright">
							<li>&copy; Untitled. All rights reserved.</li>
							<li><a href="index.tpl">HOME</a></li>
							<li>Images: <a href="http://unsplash.com">Unsplash</a></li>
						</ul>
					</div>
					</div>
				</div>
			</footer>

	</body>
</html>