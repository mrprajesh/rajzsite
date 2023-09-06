Title: GPU Stats!
Date: 05.31.2018 15:49:38
Category: Learning Curve
Status: draft

Hello ! 
This is for displaying stats of my GPU implementations! 
There are several implementations for SSP and Steiner tree problem[coming soon!].
The below is a sample stats. Real data will be updated soon!
<div class="container">
	<div class="table-responsive spacious-container fl-scrolls-hoverable">
		<div align="center">
		 <button type="button" name="load_data" id="load_data" class="btn btn-info">Refresh Stats</button>
		</div>
		<br />
		<div id="employee_table" style="overflow-x:auto;">
		</div>
	</div>
</div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<style>
table th {
	background-color: #444444;
	color: white;
}
table, th , td  {
  border: 1px solid grey;
  border-collapse: collapse;
  padding: 5px;
}
table tr:nth-child(odd) {
  background-color: #f1f1f1;
}
table tr:nth-child(even) {
  background-color: #ffffff;
}
</style>

<script>
$(document).ready(function(){
 $('#load_data').click(function(){
	$.ajax({
   url:"csvs/marks.csv",
   dataType:"text",
   success:function(data)
   {
    var employee_data = data.split(/\r?\n|\r/);
    var table_data = '<table class="table table-bordered table-striped">';
    for(var count = 0; count<employee_data.length; count++)
    {
     employee_data[count].trim();
     if(employee_data[count].length ==0)
		continue;
     var cell_data = employee_data[count].split(",");
     table_data += '<tr>';
     for(var cell_count=0; cell_count<cell_data.length; cell_count++)
     {
      if(count === 0)
      {
       table_data += '<th>'+cell_data[cell_count]+'</th>';
      }
      else
      {
       table_data += '<td>'+cell_data[cell_count]+'</td>';
      }
     }
     table_data += '</tr>';
    }
    table_data += '</table>';
    $('#employee_table').html(table_data);
   }
  });
  
 });
 
});
</script>

