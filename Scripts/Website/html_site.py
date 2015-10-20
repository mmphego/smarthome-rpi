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
            span{
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

    <span id='Header' style='float:left;height:140px;width:1760px;font-size: 20pt'>
            <img src='http://IP_Here/Images/download.jpg' width='450' height='135' class ='Image'>
            <p id='time' style='float:right;'>DATE:      <br>TIME:     <br>DOY:      </p>
            </span>

    <span id='Arduino Int Temp' style='height:290px;width:590px;border:2px solid #a1a1a1'>
            <img src='http://IP_Here:8080/render/?width=586&height=290&yMin=50&yMax=&lineMode=connected&hideLegend=true&bgcolor=000000&fgcolor=FFFFFF&minorY=4&title=Arduino%20Internal%20Temp&from=-9hours&fontSize=12&target=rpi.data.internalTemp' class ='Image'>
            </span>

    <span id='Arduin' style='height:290px;width:330px;'>
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
    </span>
    <script>
    var xName = """ + str(varTemp) + """
    var varName = xName;
    document.getElementById('curTemp').innerHTML = varName;
    </script>

    <script src='http://IP_Here/Images/js/jquery.js'></script>
    <script src='http://IP_Here/Images/js/index.js'></script>

    <span id='Room Temp' style='height:290px;width:590px;'>
            <img src='http://IP_Here:8080/render/?width=586&height=290&_salt=1420028512.521&yMax=30&minorY=4&lineMode=connected&fgcolor=FFFFFF&bgcolor=000000&colorList=green%2Cred&title=Room%20Temp&from=-9hours&lineWidth=2&fontSize=12&target=rpi.data.roomTemp&vtitle=Temperature(C)&hideLegend=true' class ='Image'>
            </span>


    <span id='RPi Temperature' style='height:290px;width:590px;'>
            <img src='http://IP_Here:8080/render/?width=586&height=290&_salt=1419628583.929&minorY=4&from=-9hours&connectedLimit=&fgcolor=FFFFFF&bgcolor=000000&lineWidth=2&title=RPi%20Temp&hideLegend=true&yMax=&fontSize=12&areaMode=first&lineMode=connected&drawNullAsZero=false&graphOnly=false&yStep=&colorList=green&target=rpi.data.internalRPiTemp' class='Image'>
            </span>

    <span id='Buttons' style='height:290px;width:330px;font-size: 20pt;border:2px solid #a1a1a1'>
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
    </span>
    <span id='RPi CPU Usage' style='height:290px;width:590px;'>
            <img src='http://IP_Here:8080/render/?width=586&height=290&from=-9hours&fgcolor=FFFFFF&bgcolor=000000&fontSize=13&title=RPi%20CPU&minorY=4&connectedLimit=&hideLegend=true&lineMode=connected&areaMode=stacked&target=carbon.rpi.system.loadAvg_15min&target=carbon.rpi.system.loadAvg_5min&target=carbon.rpi.system.loadAvg_1min' class ='Image'>
            </span>

    </body>
    <span id='Network Bandwidth' style='height:180px;width:820px;'>
            <img src='http://IP_Here:8080/render/?width=810&height=180&_salt=1419807028.849&fgcolor=000000&bgcolor=FFFFFF&hideLegend=true&minorY=4&title=Network%20Speed&from=-9hours&target=collectd.graph_host.interface-eth0.if_packets.rx&target=collectd.graph_host.interface-eth0.if_packets.tx&lineMode=connected&areaMode=stacked' width='815' height='175' class ='Image'>
            </span>

    <span id='Weather' style='height:180px;width:820px;'>
    <img src='http://IP_Here/Images/weather.png' width='815' height='180' class='Image'>
    </span>
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
