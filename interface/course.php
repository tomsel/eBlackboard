<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <?php include $_SERVER['DOCUMENT_ROOT'] . "/eBlackboard/navigation.php";
        include ('database.php');
        $database = new MyDb();
        //$database ->create_table();
	    $database ->add_data();
        echo "test";
	echo '<br />';
        $database ->show_data();
        echo "test2";        
        
        /*$lectures=$database->count_entries($_GET["course"]);
        $lecture_date=$database->get_date($_GET["course"]);
	for($i=0; $i<$lectures; $i++){
		echo '<a href="display.php?course='.$_GET["course"].'&date='.$lecture_date[$i].'">'.$lecture_date[$i].'</a><br />';
	}
	$database ->close()*/
      	?>
    </body>
</html>
