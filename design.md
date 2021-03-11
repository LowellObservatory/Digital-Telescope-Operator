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

  <lorax-mount-pointing>
    <objctra>123.56</objctra>
    <objctdec>56</objctdec>
  </lorax-mount-pointing>
 ```

- DTO-Main
- Camera/Filter Wheel Control
- Mount/Focus/Dome Control
- 
