<?php
// set to output
//system ( "gpio mode 4 out" );
// turns on the led
//system ( "gpio write 4 1" );
system ( "sudo python /home/pi/Scripts/Temp_Relay_Cont/Python/Rpi_I2C_Ard.py 41" );
?>