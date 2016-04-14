<?php
// set to output
system ( "gpio mode 21 out" );
// turns on the led
system ( "gpio write 21 1" );
//system ( "sudo python /home/pi/Scripts/Temp_Relay_Cont/Python/Rpi_I2C_Ard.py 30" );
?>
