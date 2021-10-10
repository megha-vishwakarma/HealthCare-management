//code --> to use uploaded image
<?php
// Include the database configuration file
include 'database.php';

// Get images from the database
$query = $db->query("SELECT * FROM files ORDER BY uploaded_on test");

if($query->num_rows > 0){
    while($row = $query->fetch_assoc()){
        $imageURL = 'uploads/'.$row["file_name"];
?>
    <img src="<?php echo $imageURL; ?>" alt="" />
<?php }
}else{ ?>
    <p>No image(s) found...</p>
<?php } ?>