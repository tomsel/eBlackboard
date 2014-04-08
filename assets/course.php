<?php
/* Templete name: php course.php*/
?>

        <?php 


        $database = new MyDb();

        $lecture_date=$database->get_date($_GET["course"]);
        $date_count = count($lecture_date);
        $monthArray = array( 1=> 'Januari', 2=> 'Februari', 3=> 'Mars', 4=> 'April', 
                5=> 'Maj', 6=> 'Juni', 7=> 'Juli', 8=> 'Augusti', 9=> 'September', 
                10=> 'Oktober', 11=> 'November', 12=> 'December');
        $tmp = explode('-', $lecture_date[0]);
        $year = $tmp[0];
        $month = $tmp[1];

        print '<H4><span class="label label-black">'.$monthArray[intval($tmp[1])].' '.$tmp[0].'</span></H4></br>';
        for($i=0; $i<$date_count; $i++){
                $date = explode('-', $lecture_date[$i]);
                if ($year <= $date[0]) {
                        if ($year < $date[0]) {
                               changeVariable($date, $year, $month);       
                        } else if ($month < $date[1]) {
                               changeVariable($date, $year, $month);       
                        }
                }
        //print '<ul class="nav nav-pills nav-stacked">';        
        //print '<li><a href="/?page_id=97&course='.$_GET["course"].'&date='.$lecture_date[$i].'">'.$lecture_date[$i].'</a></li>';                
            print '<div class="list-group">'; 
            print '<a href="/?page_id=97&course='.$_GET["course"].'&date='.$lecture_date[$i].'" class="list-group-item">'.$lecture_date[$i].'</a>';
        }
        function changeVariable($date, $year, $month) 
        {       
                //montharray declared at the beginning of the file isn´t visible from here. suck! :(
                $monthArray = array( 1=> 'Januari', 2=> 'Februari', 3=> 'Mars', 4=> 'April', 
                5=> 'Maj', 6=> 'Juni', 7=> 'Juli', 8=> 'Augusti', 9=> 'September', 
                10=> 'Oktober', 11=> 'November', 12=> 'December');
                print '</div>';
                print '<H4><span class="label label-black">'.$monthArray[intval($tmp[1])].' '.$tmp[0].'</span></H4></br>';
                $year = $date[0];
                $month = $date[1];        
        }
        
        ?>