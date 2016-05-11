from locals_info import get_ip
from temp_log import varHum, varTemp

def html():
    html = """
<!DOCTYPE html>
<html>
<head>
<meta name='HandheldFriendly' content='true'>
<meta name='viewport' content='width=device-width, height=device-height, user-scalable=yes'>
<meta http-equiv='refresh' content ='300; url = http://IP_Here:8000/'  charset='UTF-8'>
<TITLE>Mpho's Home Automation Control Center</TITLE>
<link rel='stylesheet' href='http://IP_Here/Images/css/style.css' media='screen' type='text/css' />
<style type='text/css'></style></head>

    <body background='http://IP_Here/Images/stars.jpg';>
            <style>
            h1{
                color:white;
                font-family:Arial,Helvetica,sans-serif;
            }
<!--
            div{
                float:left;
                color:white;
                font-family:Arial,Helvetica,sans-serif;
                margin-top:3px;
                margin-right:50px;
                margin-left:50px;
                margin-bottom:10px;
                border:2px solid #a1a1a1;
                padding:10px 10px;
                background:#1A334C;
                border-radius:25px;
                -moz-border-radius:25px;
            }
-->

            strong{
                float:right;
                color:white;
                font-family:Arial,Helvetica,sans-serif;
                margin-top:3px;
                margin-right:50px;
                margin-left:50px;
                margin-bottom:10px;
                border:2px solid #a1a1a1;
                padding:10px 10px;
                background:#1A334C;
                border-radius:25px;
                -moz-border-radius:25px;
            }
            p{
                color:white;
                font-family:Arial,Helvetica,sans-serif;
            }
            .Image{
                border:2px solid #a1a1a1;
                padding:1px 1px;
                background:#1A334C;
                border-radius:15px;
                -moz-border-radius:15px;
                -webkit-border-radius:15px;
            }
            </style>

    <div id='Header' style='float:left;height:140px;width:1760px;font-size: 20pt'>
            <img src='http://IP_Here/Images/download.jpg' width='450' height='135' class ='Image'>
            <p id='time' style='float:right;'>DATE:      <br>TIME:     <br>DOY:      </p>
            </div>

<!--
    <div id='Arduin' style='height:290px;width:330px;'>
    <center>
            <section>
      <div id='content'>
        <div id='thermometer'>
          <div class='track'>
            <div class='goal'>
              <div class='amount'>40</div>
            </div>
          <div class='progress'>
            <div class='amount'>
                <p id='curTemp'>
                </p>
            </div>
          </div>
        </div>
       </div>
      <a class='btm-btn' target='_blank' >Room Temp</a>
    </div>
    </section>
    </center>
    </div>
    <script>
    var xName = """ + str(varTemp) + """
    var varName = xName;
    document.getElementById('curTemp').innerHTML = varName;

    </script>
-->

    <script src='http://IP_Here/Images/js/jquery.js'></script>
    <script src='http://IP_Here/Images/js/index.js'></script>

<div style='height:270px;width:460px;right:1%;top:18%;position:absolute;text-align:center;'>
 <!--
    style="background-color:#eee; height:270px;width:460px;float:right;right: 100; text-align: center; ">

     <a href="https://plot.ly/~MphoMphego/64/" target="_blank" title="" style="display: block; text-align: center;"><img src="https://plot.ly/~MphoMphego/64.png" alt="" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="MphoMphego:64"  src="https://plot.ly/embed.js" async></script>
    -->
    <iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/103450/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Temp&type=spline"></iframe>


</div>
<!--
<div  style="background-color:#eee; height:270px;width:460px;float:left;">
-->
<div style='height:270px;width:460px;left:0%;top:18%;position:absolute;text-align:center;'>
<!--
style="background-color:#eee; height:270px;width:460px;float:left; text-align: center; ">
-->
    <iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/103450/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Humidity&type=spline"></iframe>

</div>


    <div id='Buttons'
    style='height:340px;width:380px;right:37%;top:32%;position:absolute;text-align:center;border:2px solid #a1a1a1;font-size:25pt'>
<!--
        style='height:290px;width:330px;font-size:20pt;text-align:center;border:2px solid #a1a1a1'>
-->

    <form method='get' action='parsing_get.wsgi'>
    <p><center>
            <TABLE>
                <TR><TD>Kitchen Light       <TD><button type='submit' style='background-color:rgba(255,255,255,0.0); border:none;' name='led1' value='Led 1'>
                    <img src='http://IP_Here/Images/on.jpg' width='30' height='30' class ='Image' /></button>

                <TR><TD>Dining Room Light       <TD><button type='submit' style='background-color:rgba(255,255,255,0.0); border:none;' name='led2' value='Led 2'>
                    <img src='http://IP_Here/Images/on.jpg' width='30' height='30' class ='Image' /></button>

                <TR><TD>Sitting Room Light      <TD><button type='submit' style='background-color:rgba(255,255,255,0.0); border:none;' name='led3' value='Led 3'>
                    <img src='http://IP_Here/Images/on.jpg' width='30' height='30' class ='Image' /></button>

                <TR><TD>Bedroom Light           <TD><button type='submit' style='background-color:rgba(255,255,255,0.0); border:none;' name='led4' value='Led 4'>
                    <img src='http://IP_Here/Images/on.jpg' width='30' height='30' class ='Image' /></button>

                <TR><TD>All Lights                      <TD><button type='submit' style='background-color:rgba(255,255,255,0.0); border:none;' name='led5' value='Led 5'>
                    <img src='http://IP_Here/Images/on.jpg' width='30' height='30' class ='Image' /></button>
            </TABLE>
    </center>
    </p></form>
    </div>

    <div id='RPi CPU Usage' style='height:270px;width:460px;left:0%;top:48%;position:absolute;text-align:center;'>
        <iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/103450/charts/3?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=CPU+Temp&type=spline"></iframe>
    </div>

    <div style='height:270px;width:460px;right:1%;top:48%;position:absolute;text-align:center;'>
        <iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/103450/charts/6?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Gas+Sensor&type=spline&yaxis=Gas+Level"></iframe>

    </div>


    <!--
        <div id='Network Bandwidth' style='height:180px;width:820px;'>
            <img src='http://IP_Here:8080/render/?width=810&height=180&_salt=1419807028.849&fgcolor=000000&bgcolor=FFFFFF&hideLegend=true&minorY=4&title=Network%20Speed&from=-9hours&target=collectd.graph_host.interface-eth0.if_packets.rx&target=collectd.graph_host.interface-eth0.if_packets.tx&lineMode=connected&areaMode=stacked' width='815' height='175' class ='Image'>
            </div>
    -->

    <div id='Network Bandwidth' style='height:200px;width:860px;right:0;position:fixed;text-align:center;bottom:0;'>
    <iframe width="850" height="190" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/103450/charts/7?average=10&bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=1000&type=spline"></iframe>
    </div>

    <div id='Weather' style='height:200px;width:860px;left: 0; position: fixed;text-align: center; bottom: 0;'>
    <img src='http://www.yr.no/place/South_Africa/Western_Cape/Cape_Town/meteogram.png' width='850' height='190' class='Image'>
    </div>
</body>

    <script>
            var currentTime = new Date()
            var month = currentTime.getMonth() + 1
            var day = currentTime.getDate()
            var year = currentTime.getFullYear()
            var hours = currentTime.getHours()
            var minutes = currentTime.getMinutes()

            var start = new Date(currentTime.getFullYear(), 0, 0);
            var diff = currentTime - start;
            var oneDay = 1000 * 60 * 60 * 24;
            var doy = Math.floor(diff / oneDay)

            if (hours < 10){
                    hours = '0' + hours
            }
            if (minutes < 10){
                    minutes = '0' + minutes
            }
            x=document.getElementById('time');  // Find the element
            x.innerHTML='DATE: ' + day + '-' + month + '-' + year + '<br>'+'TIME: ' + hours + ':'+ minutes + '<br>'+' DOY: ' + doy;    // Change the content
            </script>
    </html>

    """
    return html.replace('IP_Here',get_ip())
