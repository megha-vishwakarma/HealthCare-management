<?php
$severname='localhost';
$username='root';
$password='';
$dbname="register";
$conn=mysqli_connect($severname,$username,$password,$dbname);

if(!$conn)
{	die('Could not connect to sql'.mysql_error());
  }

?>