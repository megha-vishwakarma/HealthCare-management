<?php
$severname='localhost';
$username='root';
$password='';
$dbname="test";
$conn=mysqli_connect($severname,$username,$password,$dbname);

if(!$conn)
{	die('Could not connect to sql'.mysql_error());
  }

?>