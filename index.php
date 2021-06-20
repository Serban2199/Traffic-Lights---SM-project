<html>
<head>
<?php
if (isset($_POST['Working']))
{
exec('pkill -2 -f "/var/www/defect.py"');
exec('pkill -2 -f "/var/www/count.py"');
exec('python /var/www/count.py');
}
if (isset($_POST['NotWorking']))
{
exec('pkill -2 -f "/var/www/count.py"');
exec('pkill -2 -f "/var/www/defect.py"');
}
if (isset($_POST['Yellow']))
{
exec('pkill -2 -f "/var/www/count.py"');
exec('pkill -2 -f "/var/www/defect.py"');
exec('python /var/www/defect.py');
}
?>

  <title>Semafor de pe strada Viitorului</title>
</head>
<body background="FX3.png">
<center>
<table witdh="400" border="1" bgcolor="silver">
<td>

<Font color='blue'><b>
<center>
Universitatea Tehnica 'Gh.Asachi' Iasi - Fac. Automatica si Calculatoare<br> 
<br> 	
<img src="poza.jpg" width="200" height="200"> </center>
</Font><b>
<center> <h1> <Font color='navy'>
Semafor <br> Strada Viitorului <br>

</h1></font>
<center>

<form method="post">
  <table
 style="width: 50%; text-align: left; margin-left: auto; margin-right: auto;"
 border="1" cellpadding="2" cellspacing="2">
      <tr>
        <td style="text-align: center;"><button name="Working"><font color="black"><b>Working</button></td>
        <td style="text-align: center;"><button name="NotWorking"><font color="red"><b>Not Working</button></td>
      <tr>
        <td style="text-align: center; vertical-align: middle;"><button name="Yellow"><font color="yellow"><b>Yellow Light Only</button></td>
      </tr></font>
    </tbody>
  </table>

</form>
<font color="navy">
<br>
&copy 2021 Fac. Automatica si Calculatoare
 
</td>
</table>

</body>
</html>


