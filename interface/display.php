<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <?php include $_SERVER['DOCUMENT_ROOT'] . "/eBlackboard/navigation.php"; ?>
        
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
