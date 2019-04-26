<?php
if(isset($_FILES['abc'])){
	$names=$_FILES['abc']['tmp_name']
	$len=count($_FILES['abc']['tmp_name']);
	for($i=0;$i<$len;$i++){
		move_uploaded_file($names[$i], '$names[$i]');
	}
}
?>