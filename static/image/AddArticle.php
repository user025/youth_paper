<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="">
<meta name="author" content="">
<body>
<?php
	$title=$_POST['title'];
	$date=$_POST['date'];
	$keyword=$_POST['keyword'];
	$issue=$_POST['issue'];
	$author=$_POST['author'];
	$field=$_POST['field'];
	$location='../../Article/Academy/' . $issue;
	if (!file_exists($location))
	{
		mkdir($location);
	}
	$location = $location . '/' . $_FILES['file']['name'];
	move_uploaded_file($_FILES["file"]["tmp_name"],$location);
	$con=mysql_connect("10.73.4.40:3306","youthpaper","youthpaper@516"); 
	mysql_select_db("youth_youthpaper",$con);
	$sql = "SELECT COUNT(*) AS TOTAL FROM `fdyouth_academy`";
	$result = mysql_query($sql,$con);
	$result = mysql_fetch_array($result);
	$count = $result['TOTAL']+1;
	$sql = "INSERT INTO `fdyouth_academy`(`id`, `title`, `date`, `author`, `field`, `keyword`, `issue`, `location`) VALUES ('$count','$title','$date','$author','$field','$keyword','$issue','$location')";
	if (!mysql_query($sql,$con))
	{
		die('Error: '. mysql_error());
	}
	mysql_close($con);
	echo "<script>alert('提交成功!')</script>";
	echo "<script> window.location.href='AddArticle.html' </script>";
?>
</body>
</html>
