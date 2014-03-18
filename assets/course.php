<?php
/* Templete name: php course.php*/
?>
<ul class="nav nav-pills nav-stacked">
        <?php 


        $database = new MyDb();

        $lecture_date=$database->get_date($_GET["course"]);
        $date_count = count($lecture_date);
        for($i=0; $i<$date_count; $i++){
        	print '<li><a href="index.php?p=97&course='.$_GET["course"].'&date='.$lecture_date[$i].'">'.$lecture_date[$i].'</a></li>';
        }
        ?>
</ul>