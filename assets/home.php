
<form action="http://eblackboard.se.preview.binero.se/wordpress/"  method="get">
<input type='hidden' name='page_id' value='50'>
	<div class="col-xs-4 col-md-3">
 		<select class="form-control col-lg-10" name="course">
 	

	<?php 
		$database = new MyDb();

		$course=$database->get_Courses();
		$course_count = count($course);
		for($i=0; $i<$course_count; $i++){
			print "<option value=".$course[$i].">".$course[$i]."</option>";
		}

	?>
		</select>
	</div>
	<!--div class="col-xs-2 col-md-1"-->
		<input type="submit" value="submit" class="btn btn-default">
	<!--/div-->	
</form>