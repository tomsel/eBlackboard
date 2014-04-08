
    <?php 
        
        $database = new MyDb();
	echo '<br />';
        
        //These lines will pull the paths for the images associated with a class and a date and
        //present them to the user.
          
        
    $picture_paths=$database->get_path($_GET["course"], $_GET["date"]);
    if (count($picture_paths) > 1) {
        $i = "bilder";
    } else {
        $i = "bild";
    }

    print '<H4><span class="label label-black">Nedan visas '.count($picture_paths).' '.$i.' </span></H4>';
	foreach($picture_paths as $path){
        
		echo   '<div class="viewer">
                    <img src="'.$path.'"/>
                </div>';
	}
          
    ?>