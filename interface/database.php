<?php
      class MyDB
      {
        private $link;

         function __construct()
         {
            $this -> link = mysql_connect('localhost', 'tomas', 'abc');
            if (!($this -> link)) {
              die('Could not open database ' . mysql_error());
            }
            echo 'Connected successfully ';
            if (!mysql_select_db('eblackboard')) {
              die('Could not open database eblackboard ' . mysql_error());
            }
            echo ' eblackboard is successfully connected ';
            /*$this->open('test.db');
            echo "test.db opened<br />";*/
         }
         
         function __destruct() {
          mysql_close($this -> link); 
         }
         
// THE CREATE TABLE FUNCTION
         function create_table()
         {
            $sql =<<<EOF
              CREATE TABLE IF NOT EXISTS LECTURENOTES
              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
              PATH            TEXT      NOT NULL,
              DATE            TEXT  NOT NULL,
              COURSE        CHAR(50));
EOF;

            $ret = $this->exec($sql);
            if(!$ret){
               echo "this is wroooong<br />";
            } else {
               echo "Table created successfully<br />";
            }     
          }

// THE ADD DATA FUNCTION
      function add_data()
      {
        $sql = "INSERT INTO LectureNotes VALUES ('../img/2014-02-26.2.png', '2014-03-05', 'TDA517')";
          
          
          $ret = mysql_query($this -> link, $sql);
          if(!$ret){
            echo mysql_error() . " errormsg when inserting data";
          } else {
            echo "Records created successfully<br />";
          }
        }

//THE SHOW DATA FUNCTION      
      function show_data()
      {
        $sql ="SELECT * FROM LECTURENOTES";
        $ret = $this->query($sql);
        while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
          echo "ID = ". $row['ID'] . "<br />";
          echo "PATH = ". $row['PATH'] ."<br />";
          echo "DATE = ". $row['DATE'] ."<br />";
          echo "COURSE =  ".$row['COURSE'] ."<br /><br />";
        }
      //$this->close(); // connection closed from course-php instead
      }

//COUNT DATABASE ENTRIES
      function count_entries($course)
      {
      	$sql = "SELECT COUNT(*) as count FROM LECTURENOTES WHERE COURSE = '".$course."'";
      	$ret = $this->query($sql);
      	$row = $ret->fetchArray(SQLITE3_ASSOC);
        return $row['count'];
      }

//GET DATE FUNCTION
      function get_date($course)
      {
        $sql ="SELECT DATE as date FROM LECTURENOTES WHERE COURSE = '".$course."'";
        $ret = $this->query($sql);
        $i = 0;
        $res = [];
        while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
          $res [$i] = $row['date'];
          $i++;
        }
        return $res;
      }

//GET PATH FUNCTION
      function get_path($course, $date)
      {
        $sql ="SELECT PATH as path FROM LECTURENOTES WHERE COURSE = '".$course."' AND DATE ='".$date."'";
        $ret = $this->query($sql);
        $i = 0;
        $res = [];
        while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
          $res [$i] = $row['path'];
          $i++;
        }
        return $res;
      }
    }
   ?>        




