<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Stu Dent's Home Page + Date and Time</title>
    </head>
    <body>
        <h1>E - blackBoard page 2</h1>
        <?php 
		$lessons = 2; //hämta antal lektioner från databas
		$lesson_date = '2014-02-25';
		echo $_GET["course"]."</br>";
		for($i=0; $i<$lessons; $i++){
			echo '<a href="display.php">'.$lesson_date."</a></br>";
		}
			
      	?>
    </body>
</html>
