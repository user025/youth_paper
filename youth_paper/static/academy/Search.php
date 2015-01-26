
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>FD_Youth</title>

    <!-- Bootstrap core CSS -->
    <link href="../../css/bootstrap.min.css" rel="stylesheet">
    <link href="../../css/bootstrap-datetimepicker.css" rel="stylesheet">
    <link href="../../css/bootstrap-datetimepicker.min.css" rel="stylesheet">

    <script src="../../js/jquery.min.js"></script>
    <script src="../../js/bootstrap.min.js"></script>
    <script src="../../js/bootstrap-datetimepicker.js" charset=UTF-8></script>

    <!-- Custom styles for this template -->
    <link href="../../css/dashboard.css" rel="stylesheet">

  <style id="holderjs-style" type="text/css"></style></head>

  <body>
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="Academy.html">Academy Centre</a>
        </div>
        </div>
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li><a href="Academy Centre">Overview</a></li>
</ul>
<ul class="nav nav-sidebar">
<li> <a><b>学术思想中心</b></a> </li>
<li><a href="AddArticle.html">添加</a></li>
<li class="active"><a href="Search.html">查找</a></li>
<li><a href="Update.html">更改</a></li>
</ul>
        </div>
      </div>
    </div>

    <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
        <h1 class="page-header">在稿库中查找</h1>
	<label for="conditions">查询条件</label>


<?php
	$from="from `fdyouth_academy` where "; $condition = "1";
	if (isset($_POST['title']))
	{
		$title=$_POST['title'];
		if ($title != "") $condition=$condition . " AND `title` LIKE '%$title%'";
	}
	if (isset($_POST['author']) && ($_POST['author']))
	{
		$author=$_POST['author'];
		$condition = $condition . " AND `author` = '%$author%'";
	}
	if (isset($_POST['field']) && ($_POST['field']))
	{
		$field = $_POST['field'];
		$condition = $condition . " AND `field` LIKE '%$field%'";
	}
	if (isset($_POST['beginIssue'])&&($_POST['beginIssue']!="")) 
	{
		$issue=$_POST['beginIssue'];
		$condition = $condition . " AND `issue`>= $issue";
	}
	if (isset($_POST['endIssue']) && ($_POST['endIssue']!="")) 
	{
		$issue=$_POST['endIssue'];
		$condition = $condition . " AND `issue` <= $issue";
	}
	if (isset($_POST['beginDate']) && ($_POST['beginDate'])) 
	{
		$date=$_POST['beginDate'];
		$condition = $condition . " AND `date` >= '$date'";
	}
	if (isset($_POST['endDate']) && ($_POST['endDate'])) 
	{
		$date=$_POST['endDate'];
		$condition = $condition . " AND `date` <= '$date'";
	}
	if (isset($_POST['keyword']) && ($_POST['keyword'])) 
	{
		$keyword=$_POST['keyword'];
		$condition = $condition . " AND `keyword` LIKE '%$keyword%'";
	}
        $sql="select * " . $from . $condition;	
	$con=mysql_connect("10.73.4.40:3306","youthpaper","youthpaper@516");
	mysql_select_db("youth_youthpaper",$con);
	$result=mysql_query($sql,$con);
	if (!$result)
	{
		die('Error: '.mysql_error());
	}
	echo "<textarea class=\"form-control\" >" . $sql . "</textarea>";
	echo "<br/> <br/> ";
	echo "<label> 总共" . mysql_num_rows($result) . "条查询结果˚ </label>";
	echo "&nbsp;&nbsp;&nbsp;&nbsp";
	echo "<a href=\"Search.html\">". " 继续查找". "</a>";
	echo "<table class=\"table table-striped table-hover\">";
	echo "<thead> <tr> <th> 期号 </th> <th> 作者 </th> <th> 标题 </th> <th>关键词</th> </tr></thead>";
	echo "<tbody>";
	while ($row=mysql_fetch_object($result))
	{
		echo "<tr>";
		echo "<td>" . $row->issue . "</td>";
		echo "<td>" . $row->author . "</td>";
		echo "<td><a href=\"../../php/showResult.php?id=". $row->id . "&dep=academy\" " . "target=\"_blank\">" . $row->title . "</a></td>";
		echo "<td>" . $row->keyword . "</td>";

	        echo "</tr>";

	}
	echo "</tbody> </table>";
	mysql_close($con);
	
?>
	
    </div>

</body></html>

