<?php
      class MyDB
      {
        private $link;

         function __construct()
         {
            $this -> link = mysqli_connect('localhost', 'tomas', 'abc', 'eblackboard');
            if (!($this -> link)) {
              die('Could not open database ' . mysqli_error());
            }
            echo 'Connected successfully ';
         }
         
         function __destruct() {
          mysqli_close($this -> link); 
          echo "Database connection closed";
         }

// THE ADD DATA FUNCTION
      function add_data()
      {
        $sql = "INSERT INTO LectureNotes VALUES (NULL, '../img/2014-02-26.2.png', '2014-03-05', 'TDA517')";
          
          $ret = mysqli_query($sql);
          if(!$ret){
            echo mysqli_error() . " errormsg when inserting data";
          } else {
            echo "Records created successfully<br />";
          }
        }

//THE SHOW DATA FUNCTION      
      function show_data()
      {
        $sql ="SELECT * FROM LectureNotes";
        $ret = mysqli_query($this->link,$sql);
        while($row = mysqli_fetch_array($ret)){
          echo "ID = ". $row['ID'] . "<br />";
          echo "PATH = ". $row['PATH'] ."<br />";
          echo "DATE = ". $row['DATE'] ."<br />";
          echo "COURSE =  ".$row['COURSE'] ."<br /><br />";
        }
      }

//COUNT DATABASE ENTRIES
      function count_entries($course)
      {
      	$sql = "SELECT COUNT(*) as count FROM LectureNotes WHERE COURSE = '".$course."'";
      	$ret = mysqli_query($this->link,$sql);
      	$row = mysqli_fetch_array($ret);
        return $row['count'];
      }

//GET DATE FUNCTION
      function get_date($course)
      {
        $sql ="SELECT DATE as date FROM LectureNotes WHERE COURSE = '".$course."'";
        $ret = mysqli_query($this->link,$sql);
        $i = 0;
        $res = [];
        while($row = mysqli_fetch_array($ret)){
          $res [$i] = $row['date'];
          $i++;
        }
        return $res;
      }

//GET PATH FUNCTION
      function get_path($course, $date)
      {
        $sql ="SELECT PATH as path FROM LectureNotes WHERE COURSE = '".$course."' AND DATE ='".$date."'";
        $ret = mysqli_query($this->link,$sql);
        $i = 0;
        $res = [];
        while($row = mysqli_fetch_array($ret)){
          $res [$i] = $row['path'];
          $i++;
        }
        return $res;
      }
    }
   ?>        




