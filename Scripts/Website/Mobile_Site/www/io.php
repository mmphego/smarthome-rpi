<html>
<head>
<meta charset="UTF-8" />
  <link rel="stylesheet" type="text/css" href="css/style.css">
</head>


<?php
if (isset($_POST['LightON']))
{
exec("sudo python /home/pi/Scripts/Temp_Relay_Cont/Python/Rpi_I2C_Ard.py 1");
}
if (isset($_POST['LightOFF']))
{
exec("sudo python /home/pi/Scripts/Temp_Relay_Cont/Python/Rpi_I2C_Ard.py 1");
}
?>

<form method="post">
<button class="btn" name="LightON">Light ON</button>&nbsp;
<button class="btn" name="LightOFF">Light OFF</button><br><br>
</form> 

<style type="text/css">
.toggleSwitch {
    width: ...;
    height: ...;
    /* add other styling as appropriate to position element */
    position: relative;
}
.slider {
    background-image: url(...);
    position: absolute;
    width: ...;
    height: ...;
}
.slider.on {
    right: 0;
}
.slider.off {
    left: 0;
}
</style>
<script type="text/javascript">
function replaceClass(elt, oldClass, newClass) {
    var oldRE = RegExp('\\b'+oldClass+'\\b');
    elt.className = elt.className.replace(oldRE, newClass);
}
function toggle(elt, on, off) {
    var onRE = RegExp('\\b'+on+'\\b');
    if (onRE.test(elt.className)) {
        elt.className = elt.className.replace(onRE, off);
    } else {
        replaceClass(elt, off, on);
    }
}
</script>
<div class="toggleSwitch" onclick="toggle(this.firstChild, 'on', 'off');"><div class="slider off" /></div>
</html>
