<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
         <script type="text/javascript" src="library/jquery-1.11.0.js"></script>
        <!-- Bootstrap -->
        <link href="library/bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <script type="text/javascript" src="library/bootstrap/js/bootstrap.min.js"></script>
    </head>
    <body>
        <?php
         if (function_exists('sqlite_open')) {
          echo 'Sqlite PHP extension loaded';
        } else {
          echo 'it doesnt suppport sqlite3';
        }
        ?>
        <h1>E- blackBoard</h1>
        <form action="interface/course.php" method="get">
            <select name="course">
                <option value="volvo">Volvo</option>
                <option value="saab">Saab</option>
                <option value="mercedes">Mercedes</option>
                <option value="audi">Audi</option>
            </select>
            <input type="submit" value="Submit">
        </form>

            <!--div class="btn-group">
                <form action="interface/course.php" name="course" method="get" >
                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                    Which course are you studying?
                    <span class="caret"></span>
               </button>
                <ul class="dropdown-menu" role="menu">
                    <li><a href="#">TDA517</a></li>
                    <li><a href="#">DAT076</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li><a href="#">Separated link</a></li>
                </ul>
                 <input type="submit" value="Submit" name="course">
                 </form>
            </div-->
        
    </body>
</html>

