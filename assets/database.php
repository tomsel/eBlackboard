<?php
      class MyDB
      {
        private $link;
        
//A "magic" PHP function that is called once the object is created.
//Used here to establish a connection with our MySQL database.
         function __construct()
         {
            /*Use this if you want to run local server XAMP or MAMP
            $this -> link = mysqli_connect('localhost', 'tomas', 'abc', 'eblackboard');*/
            //Use this if you want to run at the webhotel binero
            $this -> link = mysqli_connect('eblackboard-193040.mysql.binero.se', '193040_vn74392', 'u55MZngO4Z', '193040-eblackboard');
            if (!($this -> link)) {
              die('Could not open database ' . mysqli_error());
            }
            echo 'Connected successfully ';
         }
         
//Also a "magic" PHP function. This one is called as soon as the object is destroyed.
//All objects created by PHP code is destroyed once the end of the PHP code is reached.
         function __destruct() {
          mysqli_close($this -> link); 
          echo "Database connection closed";
         }
//THE SHOW DATA FUNCTION
//Retrieve all the data from the table in the database.
//Used for development purpouses.
      function show_data()
      {
        $sql ="SELECT * FROM Images";
        $ret = mysqli_query($this-> link,$sql);
        while($row = mysqli_fetch_array($ret)){
          echo "ID = ". $row['ID'] . "<br />";
          echo "PATH = ". $row['PATH'] ."<br />";
          echo "DATE = ". $row['DATE'] ."<br />";
          echo "COURSE =  ".$row['COURSE'] ."<br /><br />";
        }
      }

//COUNT DATABASE ENTRIES
//A simple function used to count the amount of entries in the table where
//the course matches the input variable.
      function count_entries($course)
      {
      	$sql = "SELECT COUNT(*) as count FROM Images WHERE COURSE = '".$course."'";
      	$ret = mysqli_query($this-> link,$sql);
      	$row = mysqli_fetch_array($ret);
        return $row['count'];
      }

//GET DATE FUNCTION
//A function to return the dates of the classes for where
//the course matches the input variable.
      function get_date($course)
      {
        $sql ="SELECT DATE as date FROM Images WHERE COURSE = '".$course."' GROUP BY DATE";
        $ret = mysqli_query($this-> link,$sql);
        $i = 0;
        $res = array();
        while($row = mysqli_fetch_array($ret)){
          $res [$i] = $row['date'];
          $i++;
        }
        return $res;
      }

      function get_Courses()
      {
        $sql = "SELECT COURSE as course FROM Images GROUP BY COURSE ORDER BY COURSE";
        $ret = mysqli_query($this-> link,$sql);
        $i = 0;
        $res = array();
        while($row = mysqli_fetch_array($ret)){
          $res [$i] = $row['course'];
          $i++;
        }
        return $res;

      }
//GET PATH FUNCTION
//A function to return an array of paths to pictures associated with a certain
//course and a certain date.
      function get_path($course, $date)
      {
        $sql ="SELECT PATH as path FROM Images WHERE COURSE = '".$course."' AND DATE ='".$date."'";
        $ret = mysqli_query($this->link,$sql);
        $i = 0;
        $res = array();
        while($row = mysqli_fetch_array($ret)){
          $res [$i] = $row['path'];
          $i++;
        }
        return $res;
      }
    }
   ?>        




