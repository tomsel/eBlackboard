
    <?php
      class MyDB extends SQLite3
      {
         function __construct()
         {
            $this->open('test.db');

         }
       
         function create_database()
         {
            $db = new MyDB();
            if(!$db){
              echo "this is wroooong\n";
            } else {
               echo "Opened database successfully\n";
            }

            $sql =<<<EOF
              CREATE TABLE IF NOT EXISTS LECTURENOTES
              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
              PATH            TEXT      NOT NULL,
              DATE            TEXT  NOT NULL,
              COURSE        CHAR(50));
EOF;

            $ret = $db->exec($sql);
            if(!$ret){
               echo "this is wroooong\n";
            } else {
               echo "Table created successfully\n";
            }     
          } 



      
      //$db->close();
      
      //__insert("aaa", CURRENT_DATE, "TDA517")
      function add_data()
      {
        
            $sql =<<<EOF
              INSERT INTO LECTURENOTES (PATH,DATE,COURSE)
              VALUES ('sss/sss', 'date', 'TDA517');
EOF;
          
          $ret = $db->exec($sql);
          if(!$ret){
            echo $db->lastErrorMsg() . " errormsg when inserting data";
          } else {
            echo "Records created successfully\n";
          }
        }
      
      function show_data()
      {
        $sql =<<<EOF
              SELECT * FROM LECTURENOTES;
EOF;
        $ret = $db->query($sql);
        while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
          echo "ID = ". $row['ID'] . "\n";
          echo "PATH = ". $row['PATH'] ."\n";
          echo "DATE = ". $row['DATE'] ."\n";
          echo "COURSE =  ".$row['COURSE'] ."\n\n";
        } 
        $db->close();
      }
    }
   ?>        




