<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <?php include $_SERVER['DOCUMENT_ROOT'] . "/eBlackboard/navigation.php"; ?>
        <?php
        echo "this is wrong ";
        include ('database.php');
		echo "database.php is included<br />";
        $database = new MyDb();
        $database ->create_table();
	    //$database ->add_data();
	echo '<br />';
        //$database ->show_data();
        
        
        $lectures=$database->count_entries($_GET["course"]);
        $lecture_date=$database->get_date($_GET["course"]);
	for($i=0; $i<$lectures; $i++){
		echo '<a href="display.php?course='.$_GET["course"].'&date='.$lecture_date[$i].'">'.$lecture_date[$i].'</a><br />';
	}
	$database ->close()
      	?>
    </body>
</html>
