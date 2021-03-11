## End to End design decisions.

- Input Commands File
  - This file will be the output of the Lorax Scheduler
  - This file will be the input to the Digital Telescope Operator
  - This file will be formatted using XML, ie.:

```
  <lorax-camera-command>
    <image-type>"light"</image-type>
    <filter>"Halpha"</filter>
    <exptime>100</exptime>
    <xbinning>2</xbinning>
    <ybinning>2</ybinning>
    <xorgsubf>0</xorgsubf>
    <yorgsubf>0</yorgsubf>
    <target-name>"Crab Nebula"</target-name>
  </lorax-camera-command>

  <lorax-telescope-pointing>
    <ra_pnt>123.56</ra_pnt>
    <dec_pnt>56</dec_pnt>
  </lorax-telescope-pointing>
 ```

- DTO-Main
  - Reads the ICF, check status, issues commands via broker
  - Status will (eventually) include hardware status and weather status
  - Maintain log file and send alerts as needed
- Camera/Filter Wheel Control
  - Connect to camera/filter wheel via INDI
  - receive commands from broker, report status when queried
- Mount/Focus/Dome Control
  - Communicate with Mount/Focus/Dome via html api to PWI4
  - receive commands from broker report status when queried
