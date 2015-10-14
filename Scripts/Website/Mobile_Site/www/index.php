<html>
   <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="http://172.18.20.41/jquery/jquery.mobile-1.4.2.min.css">
      <script src="http://172.18.20.41/jquery/jquery-1.10.2.min.js"></script>
      <script src="http://172.18.20.41/jquery/jquery.mobile-1.4.2.min.js"></script>
      <script>
         $(document).ready(function() {
             $("#led1").change(function() {
             var isChecked = $("#led1").is(":checked") ? 1:0; 
	     if(isChecked){ 
                     $.ajax({
                             url: 'switch/led1_on.php',
                             type: 'POST',
                           });
             }
	     else{
                     $.ajax({
                             url: 'switch/led1_off.php',
                             type: 'POST',
                           });            
                  }
          });

             $("#led2").change(function() {
             var isChecked = $("#led2").is(":checked") ? 1:0; 
	     if(isChecked){ 
                     $.ajax({
                             url: 'switch/led2_on.php',
                             type: 'POST',
                           });
             }
	     else{
                     $.ajax({
                             url: 'switch/led2_off.php',
                             type: 'POST',
                           });            
                  }
          });
             $("#led3").change(function() {
             var isChecked = $("#led3").is(":checked") ? 1:0; 
	     if(isChecked){ 
                     $.ajax({
                             url: 'switch/led3_on.php',
                             type: 'POST',
                           });
             }
	     else{
                     $.ajax({
                             url: 'switch/led3_off.php',
                             type: 'POST',
                           });            
                  }
          });
             $("#led4").change(function() {
             var isChecked = $("#led4").is(":checked") ? 1:0; 
	     if(isChecked){ 
                     $.ajax({
                             url: 'switch/led4_on.php',
                             type: 'POST',
                           });
             }
	     else{
                     $.ajax({
                             url: 'switch/led4_off.php',
                             type: 'POST',
                           });            
                  }
          });
             $("#led5").change(function() {
             var isChecked = $("#led5").is(":checked") ? 1:0; 
	     if(isChecked){ 
                     $.ajax({
                             url: 'switch/led5_on.php',
                             type: 'POST',
                           });
             }
	     else{
                     $.ajax({
                             url: 'switch/led5_off.php',
                             type: 'POST',
                           });            
                  }
          });
     });
      </script>

   </head>
   <body>
      </div>
      <div data-role="page" id="mpho">
         <div data-role="header">
         </div>
         <div data-role="main" class="ui-content">
            <form>
               <div>
                  <div class="ui-field-contain">
                     <label for="switchwit">Kitchen Lights</label>
                     <input type="checkbox" data-role="flipswitch" name="switchred" id="led1" >
                  </div>

                  <div class="ui-field-contain">
                     <label for="switchwit">Dining Room Lights</label>
                     <input type="checkbox" data-role="flipswitch" name="switchred" id="led2" >
		  </div>

                  <div class="ui-field-contain">
                     <label for="switchwit">Sitting Room Lights</label>
                     <input type="checkbox" data-role="flipswitch" name="switchred" id="led3" >
		  </div>

                  <div class="ui-field-contain">
                     <label for="switchwit">Bedroom Lights</label>
                     <input type="checkbox" data-role="flipswitch" name="switchred" id="led4" >
		  </div>

                  <div class="ui-field-contain">
                     <label for="switchwit">All Lights</label>
                     <input type="checkbox" data-role="flipswitch" name="switchred" id="led5" >
		  </div>

                  <div class="ui-field-contain">
                      <p class="about-author">
                           &copy; 2015 <a href="http://mpho112.wordpress.com" target="_blank">Mpho Mphego</a></br>
                           <a href="http://172.18.20.41:8000" target="_blank">Web-based Home Ctrl</a>
                      </p>
                  </div>
            </form>
            </div>
         </div>
      </div>
      </body>
</html>
