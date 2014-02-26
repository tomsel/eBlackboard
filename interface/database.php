<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
    <?php
      class MyDB extends SQLite3
      {
         function __construct()
         {
            $this->open('test.db');
         }
      }
      $db = new MyDB();
      if(!$db){
         echo "this is wroooong\n";
      } else {
         echo "Opened database successfully\n";
      }

      $sql =<<<EOF
        CREATE TABLE LECTURENOTES
        (ID INT PRIMARY KEY       NOT NULL,
        PATH            TEXT      NOT NULL,
        DATE            DATETIME  NOT NULL,
        COURSE        CHAR(50));
EOF;

      $ret = $db->exec($sql);
      if(!$ret){
         echo "this is wroooong\n";
      } else {
         echo "Table created successfully\n";
      }
      $db->close();
   ?>        
   <p> what the fuck</p>
   </body>
</html>




