## End to End design decisions.

- Input Commands File
  - This file will be the output of the Lorax Scheduler
  - This file will be the input to the Digital Telescope Operator
  - This file will be formatted using XML

  <camera>
    <image-type>"light"</image-type>
    <filter>"Halpha"</filter>
    <exptime>100</exptime>
    <binning>”2x2”</binning>
    <target-name>"Crab Nebula"</target-name>
  </camera>

  <point-mount>
    <rightascension>123.56</rightascension>
    <decination>56</declination>
  </point-mount>

- DTO-Main
- Camera/Filter Wheel Control
- Mount/Focus/Dome Control
- 
