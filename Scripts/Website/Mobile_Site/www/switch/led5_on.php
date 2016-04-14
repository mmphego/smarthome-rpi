<?php
// set to output
system ( "gpio mode 0 out" );
system ( "gpio mode 2 out" );
system ( "gpio mode 21 out" );
system ( "gpio mode 22 out" );
// turns on the led
system ( "gpio write 0 0" );
system ( "gpio write 2 0" );
system ( "gpio write 21 0" );
system ( "gpio write 22 0" );
//system ( "sudo python /home/pi/Scripts/Temp_Relay_Cont/Python/Rpi_I2C_Ard.py 50" );
?>
