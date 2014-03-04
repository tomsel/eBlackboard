<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <?php 
        include $_SERVER['DOCUMENT_ROOT'] . "/eBlackboard/webinterface/navigation.php";
        include ('database.php');
        
        $database = new MyDb();
        
        //the next couple of lines simply output a bunch of links pointing to a page which will display pictures associated with a certain
        //class and a certain date. The link text is the date when a lecture took place.
        $lecture_count=$database->count_entries($_GET["course"]);
        $lecture_date=$database->get_date($_GET["course"]);
	for($i=0; $i<$lecture_count; $i++){
		echo '<a href="display.php?course='.$_GET["course"].'&date='.$lecture_date[$i].'">'.$lecture_date[$i].'</a><br />';
	}
      	?>
    </body>
</html>
