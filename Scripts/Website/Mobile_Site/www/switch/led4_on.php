<?php
// set to output
system ( "gpio mode 22 out" );
// turns on the led
system ( "gpio write 22 0" );
//system ( "sudo python /home/pi/Scripts/Temp_Relay_Cont/Python/Rpi_I2C_Ard.py 41" );
?>
