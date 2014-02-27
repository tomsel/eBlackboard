<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Stu Dent's Home Page + Date and Time</title>
        
    </head>
    <body>
        <h1>E - blackBoard page 2</h1>
        <?php 
        include ('database.php');
		echo "database.php is included<br />";
        $database = new MyDb();
	echo '<br />';
        
        $pictures=$database->get_path($_GET["course"], $_GET["date"]);
	foreach($pictures as $path){
		echo '<img src="'.$path.'">';
	}
	$database ->close()
      	?>
    </body>
</html>
