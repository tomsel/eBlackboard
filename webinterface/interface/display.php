<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <?php 
        include $_SERVER['DOCUMENT_ROOT'] . "/navigation.php";
        include ('database.php');
        
        $database = new MyDb();
	echo '<br />';
        
        //These lines will pull the paths for the images associated with a class and a date and
        //present them to the user.
        $picture_paths=$database->get_path($_GET["course"], $_GET["date"]);
	foreach($picture_paths as $path){
		echo '<img src="'.$path.'">';
	}
      	?>
    </body>
</html>
