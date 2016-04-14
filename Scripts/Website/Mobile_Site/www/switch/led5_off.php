<?php
// set to output
system ( "gpio mode 0 out" );
system ( "gpio mode 2 out" );
system ( "gpio mode 21 out" );
system ( "gpio mode 22 out" );
// turns on the led
system ( "gpio write 0 1" );
system ( "gpio write 2 1" );
system ( "gpio write 21 1" );
system ( "gpio write 22 1" );
//system ( "sudo python /home/pi/Scripts/Temp_Relay_Cont/Python/Rpi_I2C_Ard.py 50" );
?>
