<H4><span class="label label-black">Välj en kurs</span></H4>
<div class="list-group">

	<?php 
		$database = new MyDb();

		$course=$database->get_Courses();
		$course_count = count($course);
		for($i=0; $i<$course_count; $i++){
			print '<a href="/course/?course='.$course[$i].'" class="list-group-item">'.$course[$i].'</a>';
		}
	?>

</div>	
