<!DOCTYPE html>
<html>
    <head>
        
    </head>

    <body>
    <!-- special case since we use Mamp-->    
    <?php include $_SERVER['DOCUMENT_ROOT'] . "/eBlackboard/navigation.php"; ?>
    
    <form action="/eBlackboard/interface/course.php" method="get">
        <select name="course">
            <option value="TDA517">TDA517</option>
            <option value="saab">Saab</option>
            <option value="DAT076">Mercedes</option>
            <option value="audi">Audi</option>
        </select>
        <input type="submit" value="sbba">
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

