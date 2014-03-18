
    <?php 
        
        $database = new MyDb();
	echo '<br />';
        
        //These lines will pull the paths for the images associated with a class and a date and
        //present them to the user.
        $picture_paths=$database->get_path($_GET["course"], $_GET["date"]);
        echo $_GET["course"];
	foreach($picture_paths as $path){
        
		echo '<img src="'.$path.'">';
	}
      	?>
