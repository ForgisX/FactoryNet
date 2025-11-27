## Computer Numerical Controls

<!-- image -->

B-70254EN/01

## GE Fanuc Automation Europe

Laser-Model   C1000 i A

Operator's Manual

<!-- image -->

- No part of this manual may be reproduced in any form.
- All specifications and designs are subject to change without notice.

The  products  in  this  manual  are  controlled  based  on  Japan's  'Foreign  Exchange  and Foreign Trade Law'. The export from Japan may be subject to an export license by the government of Japan.

Further, re-export to another country may be subject to the license of the government of the country from where the product is re-exported. Furthermore, the product may also be controlled by re-export regulations of the United States government.

Should you wish to export or re-export these products, please contact FANUC for advice.

In this manual we have tried as much as possible to describe all the various matters. However, we cannot describe all the matters which must not be done, or which cannot be done, because there are so many possibilities.

Therefore, matters which are not especially described as possible in this manual should be regarded as 'impossible'.

This manual contains the program names or device names of other companies, some of which  are  registered  trademarks  of  respective  owners.  However,  these  names  are  not followed by ® or ™ in the main body.

## TABLE OF CONTENTS

| /G2/G3/G4/G5/G3/G6/G4/G7/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G1                      | /G2/G3/G4/G5/G3/G6/G4/G7/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G1                      | /G2/G3/G4/G5/G3/G6/G4/G7/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G1                      | /G2/G3/G4/G5/G3/G6/G4/G7/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G1                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /G1/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G1/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G9/G10/G11/G12/G10/G13/G14/G15/G2/G11/G16/G4/G11/G16/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G18                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| /G1/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G1/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G10/G19/G19/G13/G6/G15/G10/G20/G13/G4/G14/G9/G2/G21/G4/G13/G17/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                     | /G22                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| /G1/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G1/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G5/G4/G13/G10/G16/G4/G21/G14/G9/G10/G11/G12/G10/G13/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                  | /G23                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| /G1/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G1/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G24/G2/G5/G14/G17/G10/G24/G4/G14/G2/G19/G4/G5/G10/G16/G6/G2/G11/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                       | /G25                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| /G18 /G17/G10/G24/G4/G16/G26 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27 | /G18 /G17/G10/G24/G4/G16/G26 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27 | /G18 /G17/G10/G24/G4/G16/G26 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27 | /G18 /G17/G10/G24/G4/G16/G26 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27 |
| /G3/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G3/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G7/G10/G5/G11/G6/G11/G28 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                        | /G29                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| /G3/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G3/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G15/G10/G12/G16/G6/G2/G11 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                          | /G1/G30                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G3/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G3/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G11/G2/G16/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                 | /G1/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| /G3/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G3/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G7/G10/G5/G11/G6/G11/G28/G14/G13/G10/G20/G4/G13/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                   | /G1/G18                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G22 /G6/G11/G16/G4/G5/G11/G10/G13/G14/G17/G16/G5/G12/G15/G16/G12/G5/G4/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                      | /G22 /G6/G11/G16/G4/G5/G11/G10/G13/G14/G17/G16/G5/G12/G15/G16/G12/G5/G4/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                      | /G22 /G6/G11/G16/G4/G5/G11/G10/G13/G14/G17/G16/G5/G12/G15/G16/G12/G5/G4/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                      | /G1/G27                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G4/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G4/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G2/G12/G16/G13/G6/G11/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                           | /G1/G29                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G4/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G4/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G15/G2/G9/G19/G2/G11/G4/G11/G16/G14/G21/G4/G16/G10/G6/G13/G17/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                               | /G1/G31                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G23 /G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                     | /G23 /G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                     | /G23 /G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                     | /G18/G23                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /G5/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G5/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G21/G10/G6/G13/G26/G14/G6/G11/G17/G19/G4/G15/G16/G6/G2/G11 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                  | /G18/G25                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /G5/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G5/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G19/G4/G5/G6/G2/G21/G6/G15/G14/G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                                          | /G18/G27                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /G5/G2/G4 /G21/G4/G16/G10/G6/G13/G17/G14/G2/G24/G14/G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                                  | /G5/G2/G4 /G21/G4/G16/G10/G6/G13/G17/G14/G2/G24/G14/G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                                  | /G5/G2/G4 /G21/G4/G16/G10/G6/G13/G17/G14/G2/G24/G14/G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                                  | /G18/G29                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /G5/G2/G4/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G5/G2/G4/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G6/G7/G8/G9/G10/G11/G9/G10/G12/G13/G7/G14/G12/G15/G16/G17/G18/G19/G12/G20/G21/G19/G22/G14/G17/G12/G23/G11/G21 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2 /G2                                                                   | /G3/G24                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G5/G2/G4/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G5/G2/G4/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G6/G7/G8/G9/G10/G11/G9/G10/G12/G13/G7/G14/G12/G25/G26/G7/G8/G16/G27/G13/G12/G28/G16/G29/G30/G12/G23/G11/G21 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2                                                                            | /G3/G31                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G5/G2/G4/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G5/G2/G4/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G32/G14/G30/G21/G8/G33/G11/G9/G10/G12/G13/G7/G14/G12/G25/G26/G7/G8/G16/G27/G13/G12/G28/G16/G29/G30/G12/G34/G11/G21/G13/G14/G17 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2                                                                        | /G4/G35                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G5/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G5/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4/G14/G19/G10/G5/G16/G17/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                              | /G22/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G5/G2/G36 /G15/G2/G2/G13/G6/G11/G28/G14/G7/G10/G16/G4/G5 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                        | /G5/G2/G36 /G15/G2/G2/G13/G6/G11/G28/G14/G7/G10/G16/G4/G5 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                        | /G5/G2/G36 /G15/G2/G2/G13/G6/G11/G28/G14/G7/G10/G16/G4/G5 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                        | /G22/G18                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /G5/G2/G36/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G5/G2/G36/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G6/G19/G19/G21/G11/G9/G10/G12/G37/G8/G13/G14/G17/G12/G38/G30/G14/G33/G11/G39/G11/G33/G8/G13/G11/G19/G9 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2                                                                        | /G2/G2/G2/G2/G2 /G4/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| /G5/G2/G36/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G5/G2/G36/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G40/G9/G13/G11/G33/G19/G17/G17/G19/G27/G11/G41/G14 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2                                    | /G4/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| /G5/G2/G36/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G5/G2/G36/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G6/G21/G14/G8/G9/G11/G9/G10/G12/G40/G10/G14/G9/G13 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2                                                | /G4/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| /G5/G2/G36/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G5/G2/G36/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G40/G9/G13/G11/G39/G17/G14/G14/G42/G11/G9/G10/G12/G38/G19/G21/G16/G13/G11/G19/G9/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2                                              | /G4/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| /G5/G2/G36/G2/G36                                                                                                                                                                                                                                                                                                                                                                                                                                                            | /G5/G2/G36/G2/G36                                                                                                                                                                                                                                                                                                                                                                                                                                                            | /G28/G16/G17/G14/G12/G37/G8/G13/G14/G17/G12/G38/G16/G30/G30/G21/G43/G12/G44/G9/G11/G13/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2 /G2/G2/G2/G2/G2/G2                                                        | /G4/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| /G5/G2/G45 /G13/G10/G17/G4/G5/G14/G28/G10/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                | /G5/G2/G45 /G13/G10/G17/G4/G5/G14/G28/G10/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                | /G5/G2/G45 /G13/G10/G17/G4/G5/G14/G28/G10/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                | /G22/G25                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /G5/G2/G45/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G5/G2/G45/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G46/G8/G27/G14/G17/G12/G47/G8/G27/G12/G38/G30/G14/G33/G11/G39/G11/G33/G8/G13/G11/G19/G9 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2 /G2/G2/G2/G2/G2/G2/G2/G2                                                  | /G4/G36                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G5/G2/G45/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G5/G2/G45/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G47/G8/G27/G12/G28/G11/G30/G14/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2 /G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2/G2                                 | /G4/G36                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /G25 /G16/G5/G2/G12/G20/G13/G4/G17/G32/G2/G2/G16/G6/G11/G28 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                  | /G25 /G16/G5/G2/G12/G20/G13/G4/G17/G32/G2/G2/G16/G6/G11/G28 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                  | /G25 /G16/G5/G2/G12/G20/G13/G4/G17/G32/G2/G2/G16/G6/G11/G28 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                  | /G22/G27                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /G36/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | /G16/G5/G2/G12/G20/G13/G4/G17/G32/G2/G2/G16/G6/G11/G28/G14/G19/G5/G2/G15/G4/G21/G12/G5/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /c1                                                                                                 | /G16/G5/G2/G12/G20/G13/G4/G17/G32/G2/G2/G16/G6/G11/G28/G14/G19/G5/G2/G15/G4/G21/G12/G5/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /c1                                                                                                 | /G22/G29                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /G36/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | /G10/G13/G10/G5/G9/G14/G9/G4/G17/G17/G10/G28/G4 /G13/G6/G17/G16/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                              | /G10/G13/G10/G5/G9/G14/G9/G4/G17/G17/G10/G28/G4 /G13/G6/G17/G16/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                              | /G22/G33                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

| /G36/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G36/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G5/G4/G17/G19/G2/G11/G21/G6/G11/G28/G14/G16/G2/G14/G10/G13/G10/G5/G9/G14/G9/G4/G17/G17/G10/G28/G4/G17/G14/G2/G11/G14/G16/G32/G4/G14/G17/G15/G5/G4/G4/G11 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G31                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /G10/G19/G19/G4/G11/G21/G6/G34                                                                                                                                                                                                                                                                                                                                                                                                                            | /G10/G19/G19/G4/G11/G21/G6/G34                                                                                                                                                                                                                                                                                                                                                                                                                            | /G10/G19/G19/G4/G11/G21/G6/G34                                                                                                                                                                                                                                                                                                                                                                                                                   |
| /G10                                                                                                                                                                                                                                                                                                                                                                                                                                                      | /G4/G34/G16/G4/G5/G11/G10/G13/G14/G3/G6/G4/G7/G14/G2/G24/G14/G13/G10/G17/G4/G5/G14/G2/G17/G15/G6/G13/G13/G10/G16/G2/G5/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G25                                                                           | /G4/G34/G16/G4/G5/G11/G10/G13/G14/G3/G6/G4/G7/G14/G2/G24/G14/G13/G10/G17/G4/G5/G14/G2/G17/G15/G6/G13/G13/G10/G16/G2/G5/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G25                                                                  |
| /G20                                                                                                                                                                                                                                                                                                                                                                                                                                                      | /G17/G19/G4/G15/G6/G24/G6/G15/G10/G16/G6/G2/G11/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G27            | /G17/G19/G4/G15/G6/G24/G6/G15/G10/G16/G6/G2/G11/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G27   |
| /G15                                                                                                                                                                                                                                                                                                                                                                                                                                                      | /G19/G10/G5/G10/G9/G16/G4/G5/G14/G13/G6/G17/G16 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G29          | /G19/G10/G5/G10/G9/G16/G4/G5/G14/G13/G6/G17/G16 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G29 |
| /G6/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                 | /G6/G2/G1                                                                                                                                                                                                                                                                                                                                                                                                                                                 | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G4/G11/G10/G20/G13/G6/G11/G28/G35/G21/G6/G17/G10/G20/G13/G6/G11/G28/G14/G3/G10/G5/G6/G2/G12/G17/G14/G24/G12/G11/G15/G16/G6/G2/G11/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G33                                                                                                                                         |
| /G6/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                 | /G6/G2/G3                                                                                                                                                                                                                                                                                                                                                                                                                                                 | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G21/G6/G17/G15/G32/G10/G5/G28/G4/G14/G16/G12/G20/G4/G14/G17/G4/G13/G4/G15/G16/G6/G2/G11/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27/G25                                                                                                    |
| /G6/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                 | /G6/G2/G4                                                                                                                                                                                                                                                                                                                                                                                                                                                 | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G15/G2/G11/G16/G2/G12/G5/G6/G11/G28/G14/G15/G2/G11/G21/G6/G16/G6/G2/G11/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27/G27                                                                                                |
| /G6/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                 | /G6/G2/G5                                                                                                                                                                                                                                                                                                                                                                                                                                                 | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G4/G21/G28/G4/G14/G9/G10/G15/G32/G6/G11/G6/G11/G28/G14/G15/G2/G11/G21/G6/G16/G6/G2/G11/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27/G29                                                                                                            |
| /G6/G2/G36                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G6/G2/G36                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G19/G6/G4/G5/G15/G6/G11/G28/G14/G15/G2/G11/G21/G6/G16/G6/G2/G11/G17/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27/G31                                                                                 |
| /G6/G2/G45                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G6/G2/G45                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G19/G2/G7/G4/G5/G14/G15/G2/G11/G16/G5/G2/G13/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G29/G1                                                                        |
| /G6/G2/G24                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G6/G2/G24                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G10/G17/G17/G6/G17/G16/G14/G28/G10/G17/G14/G19/G5/G4/G17/G17/G12/G5/G4/G14/G10/G11/G21/G14/G16/G6/G9/G4/G14/G17/G4/G16/G16/G6/G11/G28 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G29/G23                                                                                                                             |
| /G6/G2/G48                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G6/G2/G48                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G13/G10/G17/G4/G5/G14/G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4/G14/G16/G6/G9/G6/G11/G28/G14/G6/G11/G21/G6/G15/G10/G16/G6/G2/G11/G14/G24/G12/G11/G15/G16/G6/G2/G11/G17/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G29/G29                                                                                                                                                                          |
| /G6/G2/G31                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G6/G2/G31                                                                                                                                                                                                                                                                                                                                                                                                                                                | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G16/G32/G4/G14/G2/G17/G15/G6/G13/G13/G10/G16/G2/G5/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G29/G31                                                                 |
| /G6/G2/G1/G35                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G6/G2/G1/G35                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G21/G6/G17/G15/G32/G10/G5/G28/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G33/G22                                                    |
| /G6/G2/G1/G1                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G6/G2/G1/G1                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G28/G10/G17/G14/G15/G2/G11/G16/G5/G2/G13/G14/G36/G1/G37 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G33/G23                                                           |
| /G6/G2/G1/G3                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G6/G2/G1/G3                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G32/G6/G28/G32/G13/G26/G14/G5/G4/G24/G13/G4/G15/G16/G6/G3/G4/G14/G9/G10/G16/G4/G5/G6/G10/G13/G14/G10/G13/G10/G5/G9/G17/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G33/G29                                                                                                                                    |
| /G6/G2/G1/G4                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G6/G2/G1/G4                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G13/G10/G17/G4/G5/G14/G19/G2/G7/G4/G5/G35/G3/G2/G13/G16/G10/G28/G4/G14/G21/G5/G2/G19 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G33/G33                                                                                                         |
| /G6/G2/G1/G5                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G6/G2/G1/G5                                                                                                                                                                                                                                                                                                                                                                                                                                              | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G19/G2/G7/G4/G5/G14/G16/G10/G20/G13/G4/G14/G17/G4/G16/G16/G6/G11/G28/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G33/G31                                                                                   |
| /G6/G2/G1/G36                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G6/G2/G1/G36                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G10/G12/G16/G2/G9/G10/G16/G6/G15/G14/G10/G28/G6/G11/G28/G14/G24/G12/G11/G15/G16/G6/G2/G11/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G31/G1                                               |
| /G6/G2/G1/G45                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G6/G2/G1/G45                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G19/G2/G7/G4/G5/G14/G15/G2/G11/G16/G5/G2/G13/G14/G36/G18/G37 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G31/G23                 |
| /G6/G2/G1/G24                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G6/G2/G1/G24                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G13/G10/G17/G4/G5/G14/G28/G10/G17/G14/G9/G6/G34/G4/G5/G14/G24/G12/G11/G15/G16/G6/G2/G11 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G31/G25                                         |
| /G6/G2/G1/G48                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G6/G2/G1/G48                                                                                                                                                                                                                                                                                                                                                                                                                                             | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G28/G10/G17/G14/G19/G5/G4/G17/G17/G12/G5/G4/G14/G15/G2/G11/G16/G5/G2/G13/G14/G36/G18/G37 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G31/G29                                                                                         |
| /G21 /G28/G13/G2/G17/G17/G10/G5/G26 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 | /G21 /G28/G13/G2/G17/G17/G10/G5/G26 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 | /G31/G33                                                                                                                                                                                                                                                                                                                                                                                                                                         |

B-70254EN/01

## 1 OVERVIEW

This manual describes how to handle the FANUC LASER-MODEL C1000 i A for those users who operate laser oscillators.

In this manual, we have tried as for as possible to address all issues. However,  space  restrictions  prevent  us  from  describing  everything that must not be done, or which cannot be done, because there are so many possibilities.

Therefore,  all  matters  which  are  not  specifically  described  as  being possible should be regarded as being "impossible".

B-70254EN/01

## 1.1 MANUAL CONTENTS

This manual consists of the following chapters and appendixes:

## 1. OVERVIEW

Chapter  1  covers  the  configuration  of  the  manual,  applicable models,  related  manuals,  and  provides  notes  on  reading  the manual.

## 2.    SAFETY

Chapter 2 covers the  warnings  and  precautions  related  to  laser beams, high voltages, high temperatures, and a toxic substances. To ensure safe operation, read this chapter first.

## 3.    FUNCTIONS

Chapter  3  describes  the  structure  and  operation  of  the  laser oscillator.

## 4.    MAINTENANCE

Chapter  4  describes  the  periodic  maintenance  of  the  laser oscillator.

## 5.    TROUBLESHOOTING

Chapter  5  describes  the  actions  to  be  taken  if  the  oscillator malfunctions.

## APPENDIX

- A.    EXTERNAL VIEW
- B.    FANUC LASER C SERIES SPECIFICATIONS
- C.    ERROR CODE LIST
- D.    GLOSSARY

B-70254EN/01

## 1.2 APPLICABLE MODELS

This manual covers the following models:

| Model                       | Abbreviation   |
|-----------------------------|----------------|
| FANUC LASER-MODEL C1000 i A | C1000 i A      |

1

.

OVERVIEW

1

.

OVERVIEW

B-70254EN/01

## 1.3 RELATED MANUALS

The  following  manuals  are  available  for  the  FANUC  LASERMODEL C1000 i A:

| FANUC Series 16 i -LA       | DESCRIPTIONS                    | B-63192EN   |
|-----------------------------|---------------------------------|-------------|
| FANUC Series 16 i -LA       | CONNECTION MANUAL               | B-63193EN   |
| FANUC Series 16 i -LA       | OPERATOR'S MANUAL               | B-63194EN   |
| FANUC Series 16 i -LA       | MAINTENANCE MANUAL              | B-63195EN   |
| FANUC Series 16 i -LA       | PARAMETER MANUAL                | B-63200EN   |
| FANUC LASER-MODEL C1000 i A | DESCRIPTIONS                    | B-70252EN   |
| FANUC LASER-MODEL C1000 i A | OPERATOR'S MANUAL (This manual) | B-70254EN   |
| FANUC LASER-MODEL C1000 i A | MAINTENANCE MANUAL              | B-70255EN   |

B-70254EN/01

## 1.4 FOR SAFE OPERATION

This  manual  contains  precautions  which  must  be  observed  during operation  of  the  laser  oscillator,  to  ensure  the  operator' s  safety  and prevent  damage  to  the  oscillator.    Each  precaution  is  indicated  by "Warning" or "Caution" according to its severity.

Supplementary information is indicated by "Note".

Read the contents of each "Warning", "Caution", and "Note" before attempting to use the oscillator.

## WARNING

Precautions to be applied in those situations where there is a danger of the operator being killed or seriously injured.

## CAUTION

Precautions to be applied in those situations where there is a danger of the operator being slightly injured or the oscillator being damaged.

## NOTE

Supplementary information other than precautions.

The  functions  of  a  laser  machining  system  depend  not  only  on  the laser  oscillator,  but  also  on  the  machine,  power  magnetics  cabinet, servo  system,  CNC,  and  operator' s  panel.    This  manual  describes only the laser oscillator.    For a description of the other components, refer  to  the  corresponding  manuals,  supplied  by  the  machine  tool builder.

- Read this manual thoroughly and store it in a safe place.

B-70254EN/01

## 2 SAFETY

This chapter describes precautions to be observed to ensure the safe operation of the laser oscillator.

Read  this  chapter  thoroughly  before  attempting  to  use  the  laser oscillator.

Also, read the safety precautions in the operator' s manual supplied by the machine tool builder.

The laser oscillator may present a danger not only to the operator but also to other people working around the oscillator, up to a considerable distance away.    The laser oscillator must, therefore, be operated only by a person who has received appropriate training.

Only persons who have understood the internal structure of the laser oscillator  and  have  received  appropriate  training  can  maintain  the laser oscillator.

A  warning  label  is  put  on  each  dangerous  position  of  the  laser oscillator. Be extremely careful about the labeled positions.

B-70254EN/01

## 2.1 WARNING

- (1) It is extremely dangerous to expose your eyes to direct, scattered, or  reflected  CO2  laser  light.  Always  wear  protective  glasses while the laser is operating.

Exposure  to  laser  light  can  cause  blindness.  If  your  eyes  are accidentally exposed, seek medical advice immediately.

- (2) Do not turn on the laser oscillator while a panel is removed or a
2. door is open.

Operating  the  laser  with  a  door  open  or  panel  removed  may result  in  the  operator  being  directly  exposed  to  CO2  laser radiation.  Exposure  to  laser  light  can  cause  blindness  and/or severe burns. If your eyes are accidentally exposed to laser light, seek medical advice immediately.

Before  turning  on  the  power  during  maintenance  if  absolutely necessary, wear  protective glasses and  clothing to prevent accidents.

- (3) If  the  laser  oscillator  is  operated  with  a  panel  open,  ultraviolet radiation  is  emitted  from  the  high-frequency  discharge  section. Gazing  the  discharge  section  for  a  long  time  can  cause  visual disturbances such as impaired eyesight.

Always wear protective glasses during work. If you feel trouble with your eyes, seek medical advice immediately.

- (4) Surround  the  laser  machining  tool  with  a  fence  made  of  a material  which absorbs laser light well (such as acrylic). Place appropriate warning notices on the fence.

The  door  in  the  safety  fence  shall  be  fitted  with  an  interlock switch such that opening the door stops the laser.

Failure to provide such a fence exposes persons in the vicinity of the  machine  tool  to  the  danger  of  being  exposed  to  CO 2 laser radiation  and  the  associated  risk  of  blindness.  If  a  person  is accidentally exposed to laser light, seek medical advice immediately.

- (5) The  laser  beam  shall  be  no  higher  than  average  eye  height. Enclose the path of the laser beam with covers. Do not leave the end of the beam path open. Place laser- absorbing material at the end of the beam path to absorb the beam' s energy.

A CO2 laser beam is directional and has a high energy density. Exposure to laser light can cause blindness. Flammable material may burn or explode if exposed to the laser beam. If your eyes are  accidentally  exposed  to  laser  light,  seek  medical  advice immediately.

B-70254EN/01

- (6) A high voltage of 3 to 4 kV0-p is applied to some places in the laser oscillator cabinet. Therefore, do not turn the power to the oscillator on or operate the oscillator when an oscillator panel is open. Operating the laser oscillator with a panel open can cause a  touch  on  a  high-voltage  place,  resulting  in  electric  shock. Before  turning  on  the  power  during  maintenance  if  absolutely necessary, take measures against accidents.
- (7) Before daily inspection, the replacement of a maintenance  part or maintenance, open the main circuit breaker and turn the power supply off (double power-off).

To prevent the power from being inadvertently turned on, lock the  circuit  breaker  open,  and  affix  an  indication  of  work  in

- progress.

Failure  to  turn  off  the  power  during  inspection  or  replacement exposes the operator to the danger of electric shock.

Before  turning  on  the  power  during  maintenance  if  absolutely necessary, take measures against accidents.

- (8) The oscillator output mirror and focusing lens on the machining head both have a substrate made of ZnSe (zinc selenide), a toxic substance. Therefore, do not touch the mirror or lens with your

bare hands. Inhaling ZnSe dust may cause difficulty in breathing, completely stopping the breathing of the victim in the worst case. If you accidentally touch the mirror or lens with your bare hands, wash your hands well under running water.

If  you  accidentally  inhale  ZnSe  dust  or  debris,  seek  medical advice immediately.

- (9) Do  not  look  at  the  machining  point  without  eye  protection. Otherwise,  your  eyes  may  be  exposed  to  reflected  laser  light, resulting in blindness.

If your eyes are accidentally exposed to laser light, seek medical advice immediately.

- (10) Before  attempting  to  machine  any  material  for  the  first  time, consult with the manufacturer of the material.

Some  materials  generate  toxic  gases  when  cut  or  drilled  by  a

- laser beam.

Should  you  accidentally  inhale  any  toxic  gas,  seek  medical advice immediately.

- (11) If  the  laser  oscillator  must  be  moved,  entrust  the  work  to  the machine tool builder whenever possible. If performed  by inexperienced personnel, the oscillator may topple or be dropped, resulting in a potentially fatal accident.

When  the  machine  tool  builder  is  not  available  to  move  the oscillator, follow the procedure described on the hanging method label.    While moving the oscillator, stand well clear and never pass under the oscillator.

B-70254EN/01

- (12) Do not allow any dangerous or high-pressure gas to get into the oscillator housing. The  oscillator cabinet has a hermetic structure  (dustproof  and  dripproof), it  cannot  be  ventilated easily.

Flammable gases such as oxygen can cause a fire or explosion.

Toxic  gases  can  harm  operators  during  maintenance.  Organic gases can degrade machining performance. High-pressure gases can damage a panel or the cabinet, resulting in injury from flying matters.

If such a gas accidentally gets into the oscillator housing, remove a panel for ventilation. The installation room must be also well ventilated.

To purge the oscillator housing, use purified, low-pressure air or nitrogen.

B-70254EN/01

## 2.2 CAUTION

- (1) If there is a possibility of being exposed to CO2 laser radiation exceeding the  maximum  permissible  exposure  (MPE)  level  for skin, wear protective clothing. Otherwise, there is a danger of being burnt.
- (2) FANUC  LASER-MODEL  C1000 i A is fitted with a red semiconductor  laser  to  indicate  the  approximate  position  of invisible CO2 laser beam. Do not look directly at the semiconductor laser beam. Otherwise, your eyes may be injured.
- (3) The gas circulating system in the oscillator becomes very hot. Do  not  touch  the  gas  pipes,  turbo  blower,  heat  exchanger,  or exhaust pump, until they have cooled down sufficiently after the oscillator has been turned off. Otherwise, you may be burnt.
- (4) Do not pass your hand in the optical path of the laser machine or under the laser head when the shutter of the oscillator is open. When the shutter is open, a laser beam may be emitted from the oscillator accidentally. Before work in the optical path or under the laser head, confirm that the shutter is closed.
- (5) The workpiece becomes very hot during machining. Never touch the  workpiece  with  your  bare  hands.  Otherwise,  you  may  be burnt.
- (6) During machining, extremely hot chips are likely to be generated. Unless  sufficient  caution  is  exercised,  there  is  a  danger  of  the operator being burnt, or of a fire being started.
- (7) Some  materials  may  burn  or  explode  when  laser  machined. Before  attempting  to  machine  any  material  for  the  first  time, consult  with  the  manufacturer  of  the  material,  to  prevent  the danger of fire of or the possibility of operator injury.
- (8) The oscillator contains cooling fan units. Although the fan units are fitted with a finger guard, to prevent injury, keep your hands well away from the fans.
- (9) The  oscillator  is  controlled  according  to  the  CNC  internal parameter settings. If a numeric value different from a setting is entered and the oscillator is operated, the oscillator  may malfunction. In the worst case, the oscillator may be damaged.

B-70254EN/01

## 2.3 NOTE

- (1) During installation or maintenance necessitating the opening of an oscillator door or the removal of a panel, only persons who have  undergone  maintenance  training  should  operate  the  laser. In such a case, extreme caution must be exercised.
- (2) Warning labels are affixed to those parts of the oscillator where there  is  a  danger  of  exposure  to  laser  radiation.  Observe  the precautions given on the labels. (Section 2.4 shows the warning labels.)
- (3) Laser products shall conform to the regulations laid down in the laser  safety  standard,  including  that  stipulating  control  using  a key.
4. The oscillator start signal (RUN ON) shall be controlled with a key switch such that the oscillator cannot be turned on without a specific key. Control  using  a  key  ensures  that  other  than  the  authorized personnel  cannot  operate  the  laser  oscillator.  It  is  extremely dangerous  if  a  person  who  is  unfamiliar  with  the  equipment attempts to operate the laser oscillator.
- (4) The shutter shall be unlocked only while a beam is being output. Otherwise, keep the shutter locked to provide protection should the laser accidentally be turned on.
- (5) Do  not  discard  a  used  output  mirror  or  focusing  lens  together with  regular  waste.  If  the  output  mirror  or  focusing  lens  is replaced,  return  the  original  to  the  supplier  or  entrust  it  to  a specialized disposal company.
- (6) Do not  place  any  flammable  material  (such  as  paper,  cloth,  or wood) near the workpiece table.
- (7) Keep a fire extinguisher beside the unit.
- (8) The  FANUC  LASER-MODEL  C1000 i A  is  equipped  with  an alarm  lamp.  The  alarm  lamp  blinks  while  discharge  is in progress or whenever laser radiation is possible. While the alarm lamp is blinking, pay careful attention to laser radiation and high voltages.

B-70254EN/01

## 2.4 WARNING LABELS

The  oscillator  uses  high  voltages  and  laser  beam  radiation.  Such hazards  are  indicated  with  warning  labels  attached  to  the  positions shown in Fig. 2.4 (a) to (b).

Fig. 2.4 (a)    Warning label positions (C1000 i A : front view)

<!-- image -->

Fig. 2.4 (a)    Warning label positions (C1000 i A : rear view)

<!-- image -->

B-70254EN/01

## (1) Class indication label (JPN)

-INVISIBLE and/or VISIBLE LASER RADIATIoNAVOID EYE OR SKIN EXPOSURE TO DIRECT OR SCATTERED RADIATION.

一不可视/可视一光一 一散乱光危。见触下

|                              | INVISIBLE(不可初）                    | VISIBLE(可)   |
|------------------------------|-----------------------------------|--------------|
| LASER PRODUCT （品）            | CLASS4                            | CLASS 3A     |
| MAXIMUM OUTPUT （最大出力）        | 2000W                             | <5mW         |
| PULSE DURATION (八)           | 100μS~CW                          | CW           |
| EMITTED WAVELENGTH (液&) (媒体) | 10.6μm                            | 0.6~0.7αm    |
| LASERMEDIUM                  | CO/N/He=5/55/40%|SEM1C0M.or He-Ne |              |

A3T0-1168-0118

## (1) Class indication label (FDA)

|                    | INVISIBLE                             | VISIBLE   |
|--------------------|---------------------------------------|-----------|
| MAXIMUM OUTPUT     | 2000W                                 | < 5mW     |
| PULSE DURATION     | 100μS~Cw                              | CW        |
| EMITTED WAVELENGTH | 10.6μm                                | 0.6~0.7μm |
| LASER MEDIUM       | CO,/UL/Ho=5/55/40% |SEM1COM. or He-Me |           |

<!-- image -->

## (2) Warning label

<!-- image -->

B-70254EN/01

- (3) Aperture label

## AVOID EXPOSURE INVISIBLE AND/Or VISIBLE LASER RADIATION IS EMITTED FROM THIS APERTURE.

注意:一廿光出口 二不可机又可机而方の

一廿光加出可。

A370-1146-0106

- (4) Suspension method label
- (5) Access panel

<!-- image -->

WHEN OPEN. AVOID EYE OR SKIN EXPOSURE TO

DIRECT OR SCATTERED RADIATION.

危 一光出。一散乱光危 。见触下

A370-1146-0105

<!-- image -->

- (6) Label inside the access panel

## DANGER

VISI8LE and/or INVISIBLELASER RADIATION WHEN OPEN.AVOID EYE OR SKIN EXPOSURE TO DIRECT OR SCATTERED RADIATION.

B-70254EN/01

- (7) Discharge section label
- (8) Certification label

<!-- image -->

## -CertifiCatiOn LaBel-

- ·This laser product complies with 21( CFR R1040.10 and

A370-1146-0060

- (9) Equipment nameplate
- (10) Manufacturer' s address label
3. /G36/G1/G1/G37 Label  for  regulating  the  atmospheric  gases  in  the  oscillator housing

<!-- image -->

<!-- image -->

<!-- image -->

3

.

INTERNAL

STRUCTURE                                                                                                                B-70254EN/01

## 3 INTERNAL STRUCTURE

B-70254EN/01

## 3.1 OUTLINE

Fig. 3.1 show the internal structure of the laser oscillator.

The  C1000 i A  consists  of  a  laser  resonator,  discharge  drive  unit, forced gas circulating system, pressure controller, CNC interface, and a protective housing.

Fig. 3.1 C1000 i A internal structure

<!-- image -->

## (1) Laser resonator

The laser resonator consists of several discharge tubes, connected in series using folding mirrors, with a rear mirror and output mirror placed at the open ends of the discharge tubes, thus sealing  the  tubes.    The  resonator  is  fitted  with  a  gas  pipe connecting port through which laser gas is fed into the discharge tubes.

A discharge from the electrodes of the discharge tube energizes CO2  molecules,  which  emit  light.  This  light  is  amplified  by stimulated emission, repeated between the rear mirror and output mirror, a laser beam being emitted from the output mirror.

STRUCTURE                                                                                                                B-70254EN/01

- (2) Discharge drive unit

The  discharge  drive  unit  consists  of  a  laser  power  supply, matching box, and discharge tubes. High-frequency output of 2 MHz  that  is  controlled  by  the  CNC  discharges  the  laser  gas flows through discharge tubes to energize CO2 molecules.

- (3) Forced gas circulating system

A  gas circulating system is configured by connecting the resonator and turbo blower with a circulating pipe.    Laser gas is forced  through  the  discharge  tubes  at  a  speed  of  200  m/s  or higher.

A water-cooled heat exchanger, used to cool the hightemperature gas from the discharge tubes, is provided at the inlet side of the turbo blower.    At the outlet side of the turbo blower, another water-cooled heat exchanger dissipates the compression heat.

## (4) Pressure controller

The laser gas pressure within the forced gas circulating system is controlled  by  commands  issued  from  the  CNC,  thus  ensuring stable laser output.

- (5) CNC interface

Interface used to connect a FANUC  Series 16 i -L.  CNC commands that, control the operation of the laser oscillator, such as start/stop and laser output, are input via this interface.

- (6) Protective housing

An enclosure  that  houses  the  above  components.  The  housing, consisting of metal panels, completely encloses the laser oscillator,  thus  protecting  the  operator  from  exposure  to  laser radiation and from high voltages. All panels are screw-fixed and cannot be removed without an appropriate tool.

B-70254EN/01

## 3.2 COMPONENT DETAILS

This  section  describes  the  internal  structure  of  the  C1000 i A  more specifically.    Fig. 3.2 is an internal structural drawing.

Fig. 3.2    C1000 i A structural drawing

<!-- image -->

## (1) Resonator

The resonator consists of an output mirror, rear mirror, folding mirrors,  discharge  tubes,  power  sensor  unit,  etc.  It  converts electrical energy first to laser gas, then to optical energy (10.6µ m single-wavelength laser beam).

- (2) Output mirror

A  transmitting/reflecting  mirror  which  outputs  the  laser  beam after it has been amplified. The output mirror consists of a ZnSe (zinc selenide) substrate, coated with dielectric. ZnSe is tightly toxic.  Be  particularly  careful,  therefore,  when  handling  the output mirror.

<!-- image -->

STRUCTURE                                                                                                                B-70254EN/01

## (3) Rear mirror

A  reflecting  mirror  consisting  of  a  Ge  (germanium)  substrate, coated with dielectric.

Having a high reflectance  of  99.5%,  the  rear  mirror  is  used  to reflect  the  laser  beam  within  the  resonator  while  transmitting 0.5%  of  the  laser  light  so  that  the  beam  can  be  monitored externally.

## (4) Folding mirror

A mirror unit which reflects the laser beam at a 90-degree angle. The folding mirror consists of a block with a surface tilting to a 45-degree  angle  and  an  Si  (silicon) substrate,  coated  with multilayer dielectric film.

## (5) Discharge tube

A pair of Ag (silver) electrodes are metallized on the surface of a hollow  quartz  glass  pipe.  A  high-frequency  discharge  between these  electrodes  injects  electrical  energy  into  the  laser  gas. Each  electrode  is  coated with  ceramic,  preventing  it  from degrading and thus improving system reliability.

- (6) Trigger electrode

A  predischarge  placed  outside  the  laser  oscillation  area  can facilitate the start of the main discharge. With it, the laser output is completely zero when the beam is off.

## (7) Power sensor

An optical sensor which detects the intensity of the laser beam, transmitted through the rear mirror, thus enabling monitoring of the laser output level.

- (8) Gas circulating system

A gas circulating path including a turbo blower, heat exchangers, and circulating pipes, which circulates laser gas in the discharge tubes at high speed.

- (9) Turbo blower

During laser oscillation, the laser gas pressure is 1330 - 9310 Pa. The turbo blower circulates this rough-vacuum gas at high speed without contaminating the gas.

## (10) Heat exchanger (inlet)

Water-cooled heat exchanger used to cool the laser gas that has been  heated  by  discharge,  before  it  is  drawn  into  the  turbo blower.

## (11) Heat exchanger (outlet)

Water-cooled heat exchanger used to cool the laser gas that has been  heated  by  compression  in  the  turbo  blower,  before  being forced into the discharge tubes.

B-70254EN/01

## (12) Gas controller

The  gas  controller  always  monitors  the  gas  pressure  in  each discharge tube and supplies the fresh laser gas to the circulating system to keep the pressure constant. It also monitors the supply status  of  the  laser  gas,  purge  check  for  the  circulating  system, and  other  items  and  has  a  function  of  adjusting  the  amount  of flow of the gas to be exhausted.

## (13) Exhaust pump unit

This  unit  is  used  to  vacuum-exhaust  laser  gas  from  the  gas circulating  system  such  that  its  pressure  falls  to  that  used  for laser  oscillation.  Also,  within  this  unit,  a  small  amount  of circulating gas is constantly being exchanged, to prevent degradation of the circulating gas.

## (14) Hour meter

The hour meter indicates the total number of hours that the laser oscillator has operated (how many hours the exhaust pump has operated),  to  indicate  whether  maintenance  or  inspection  is necessary.

## (15) Shutter

The shutter has a rotary arm operated by a rotary solenoid and an Au (gold)-evaporated reflecting mirror attached to the arm.

It  can  be  opened  and  closed  by  CNC  commands.  It  also  has  a position sensor and a temperature sensor for safety and always monitors the open/close status and shutter temperature.

## (16) Beam absorber

While the laser oscillator is operating with the shutter closed, the laser beam is guided into the beam absorber. The beam absorber absorbs nearly 100% of laser beam and is water-cooled, allowing it  to  safely  absorb  the  beam  for  relatively  long  periods.  For safety, the beam absorber is equipped with a temperature sensor which allows the system to monitor the temperature of the beam absorber.

## (17) Distribution unit

This unit distributes cooling water, supplied from either a chiller unit  or  a  temperature-regulated  external  water  supply,  to  each unit in the laser oscillator.

For  safety,  the  water  distribution  unit  is  equipped  with  a  flow sensor which allows the system to monitor the flow rate of the cooling water.

STRUCTURE                                                                                                                B-70254EN/01

- (18) Laser power supply

A  power  supply  for  generating  a  discharge  in  each  discharge tube. The laser power supply receives the three-phase AC input at 200/220V and outputs 2-MHz high-frequency power

- controlled with stability by commands from the CNC.

The  RF  inverter  converts  DC  power  to  3  to  4  kVPO-P  highfrequency (2 MHz) power, then outputs it to the matching box.

- (19) Matching box

The matching box contains a matching circuit, consisting of coils and capacitors, which ensures that power is effectively input to the discharge tubes.

- (20) Intermediate PCB B

This PCB transmits signals output by the shutter section, such as those from the limit switch, absorber temperature sensor, power sensor, and condensation sensor, to the interface PCB.

- (21) Input unit

The  power  magnetics  cabinet  distributes  power,  supplied  from an  external  unit,  to  each  unit  in  the  laser  oscillator.  It  also protects each unit from overcurrents.

## (22) Input unit control PCB

- This PCB has functions of transmitting the contactor open/close signals according to CNC commands and of notifying the CNC of the open/close status of the circuit breaker in the input unit.
- (23) Interface PCB

Transfers signals to and from the CNC via the FANUC I/O Link (serial interface).

## (24) Stabilized power supply

- This unit converts the 200/220 VAC power source to DC power for the interface PCB and other units.
- (25) Condensation sensor

The  condensation  sensor  is  mounted  above  the  output  mirror holder.  If  condensation  occurs  on  this  sensor,  the  resistance changes, an alarm (abnormal water temperature) occurs, and the oscillator is stopped. It prevents faults in each unit  from occurring due to condensation.

## (26) High-frequency inverter

- This  inverter  drives  the  turbo  blower.  It  is  responsible  for acceleration/deceleration  control  during  start  and  stop  of  the blower.
- (27) Turbo PCB

This  PCB  monitors  overheating,  the  oil  level,  and  frequency reached signal of the turbo blower.

B-70254EN/01

## (28) Guide laser (diode laser)

A  diode  laser  is  overlaid  on  the  same  optical  axis  as  a  guide beam for checking the optical axis because the CO2 laser beam is invisible  to  the  unaided  eye.  The  guide  beam  is  emitted  in synchronization  with  the  mechanical  shutter  only  when  the shutter  is  closed.  The  guide  laser  can  be  used  for  roughly adjusting the optical path of an external optical system and for obtaining a guide for the machining point.

4

B-70254EN/01

## MAINTENANCE

In  FANUC  LASER  C1000 i A,  periodic  inspection  items  have  been reduced, and adjustments have been made easy. To keep the oscillator in a satisfactory operating condition over a long period, however, it is necessary to carry out periodic maintenance (including daily maintenance) described in this chapter. The oscillator is designed to maintain  the  same  performance  and  reliability  as  it  has  when  it  is installed, provided that maintenance is carried out as prescribed.

B-70254EN/01

## 4.1 DAILY INSPECTION

Table 4.1 lists daily inspection items.    Inspect the FANUC LASER C1000 i A  according  to  this  table.    When  parts  (including  oil)  have been used for a prescribed period, replace them quickly.

Table 4.1    Daily inspection items for FANUC LASER C series

|    | Item                  | Period   | Content and instruction                                                                                                                                                                                                                                                                                           |
|----|-----------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Residual laser gas    | Daily    | Check to see if the primary pressure is 1MPa or less as measured at the regulator on the laser gas cylinder. If the primary pressure is 1MPa or lower, replace the gas cylinder.                                                                                                                                  |
|  2 | Exhaust pump oil      | Weekly   | Make sure that the oil level is between L (lower limit) and H(higher limit). If the oil level is below L, supply oil. Be sure to replace the oil periodically, every 1500 hours of operation, whichever is earlier.                                                                                               |
|  3 | Exhaust pump oil leak | Weekly   | Make sure that no oil is leaking from the exhaust pump main body, drain valve and their periphery. If oil is leaking, immediately replace the exhaust filter, because it is likely to have been clogged. Be sure to replace the exhaust filter periodically, every 3000 hours of operation, whichever is earlier. |
|  4 | Turbo blower oil      | Weekly   | Make sure that the oil level is between L (lower limit) and H (higher limit). If the oil level is below L, supply oil. Be sure to replace the oil periodically, every 1000 hours of operation, whichever is earlier.                                                                                              |
|  5 | Turbo blower oil leak | Weekly   | Make sure that no oil is leaking from the turbo blower main body, oil inlet, cock, and their periphery. If oil leaks for any reason other than a cock being open, call FANUC.                                                                                                                                     |
|  6 | Laser output          | Weekly   | If the laser output decreases within the oscillator, warning message No. 4085 is issued. If this message appears, clean or replace the mirror in the oscillator quickly.                                                                                                                                          |
|  7 | Cooling water         | Daily    | Make sure that the chiller discharge output is 5 kgf/cm 2 or less. At the start of the oscillator, also make sure that the water temperature is 20 ° C or higher.                                                                                                                                                 |
|  7 | Cooling water         | Weekly   | Check the quality of cooling water in the chiller. Be sure to replace the cooling water every two months. Adding an anticorrosive to cooling water can decrease the replacement frequency.                                                                                                                        |

B-70254EN/01

## 4.2 PERIODIC MAINTENANCE

The  FANUC  LASER  C1000 i A  contains  consumables  that  must  be replaced periodically. Table 4.2(a) or (b) lists such consumables and the related periodic maintenance work.

Perform periodic maintenance as well as daily inspection described in Section 4.1 by using the listed periods as guidelines.

Note, however, that the replacement and maintenance intervals are not guaranteed values but standard values based on field records.

Table 4.2(a)    Periodic maintenance items and periods

|    | Item                                  | Period of maintenance (operation hour)                     |
|----|---------------------------------------|------------------------------------------------------------|
|  1 | Output mirror change                  | Every 3000 to 4000 hours, or when the quality has degraded |
|  2 | Rear mirror change                    | Every 3000 to 4000 hours, or when the quality has degraded |
|  3 | Folding mirror change                 | Every 3000 to 4000 hours, or when the quality has degraded |
|  4 | Exhaust pump oil change               | Every 1500, or when the exhaust power has degraded         |
|  5 | Exhaust pump filter change            | Every 3000, or when the exhaust power has degraded         |
|  6 | Exhaust pump overhaul                 | Every 10000, or when the exhaust power has degraded        |
|  7 | Turbo blower oil change               | Every 1000, or when oil properties have changed            |
|  8 | Turbo blower overhaul                 | Every 12000, or when the power has degraded                |
|  9 | Pressure controller gas filter change | Every 12000, or when a pressure failure occurs             |
| 10 | Discharge tube O-ring change          | Every 6000, or internal leakage occurs                     |
| 11 | Gas pipe O-ring replacement           | Every 6000, or internal leakage occurs                     |
| 12 | Cooling water                         | Every 1500, or when cooling water properties have changed  |
| 13 | Water tubing cleaning                 | Every 3000, or when the water pipe has clogged             |
| 14 | Alarm lamp replacement                | Every 3000, or when the lamp fails to light                |

Table 4.2(b)    Mirror cleaning periods

| Item                                     | Period of maintenance (operation hour)   |
|------------------------------------------|------------------------------------------|
| Cleaning of output and rear mirrors only | None                                     |
| Cleaning of all internal mirrors         | Every 3000 to 4000 hours                 |

B-70254EN/01

## 4.3 DETAILS OF MAINTENANCE

When  opening  the  panels  and  doors  during  maintenance,  keep  the power turned off. Before replacing oil, be sure to check that purging is completed.

## 4.3.1 Changing the Turbo Blower Oil

## (1) Check method

Check the amount of oil in the turbo blower while referring to the figure below. The oil level should be between graduations H and L.

This  check  should  be  made  when  the  oscillator  is  at  a  rest. When the turbo blower is running, it is impossible to check the amount of oil correctly.

Fig. 4.3.1    Turbo blower oil gauge

<!-- image -->

## (2) Replenishment method

- 1 Remove the hexagonal-head screw from the oil inlet with a 17 mm wrench.

Be careful not to lose the O-ring on the screw.

Before supplying turbo oil, stop the oscillator according to the correct procedure and turn off the power.

## CAUTION

If the oscillator is not stopped by the correct procedure, the pressure in the turbo blower becomes negative. Opening the oil inlet under such a condition lets a large amount of air get in the turbo blower. This flow of air causes oil mist to get into the oscillator housing, resulting in contamination of internal mirrors.

B-70254EN/01

- 2 Take out a bottle of oil from an oil kit (A04B-0800-K326). Remove the nozzle from the bottle, and take off the inner lid, then put the nozzle back on the bottle.

Put the supplied tube into the nozzle, insert the tube into the oil inlet, pour oil being careful to cause no foreign matters to get into oil.

Pour  oil  while  checking  the  oil  level  from  the  oil  level window until the oil level reaches the three-quarter position from L between L and H. Either superfluous or insufficient oil can be a cause of trouble.

- 3 Lightly wipe the area around the oil inlet, hexagonal-head screw  on  the  oil  inlet,  and  O-ring  with  a  clean  cloth  or paper, then check that there are no foreign matters. Foreign matters getting into oil may cause a turbo blower fault.  Check  that  the  O-ring  is  fit  to  the  hexagonal-head screw on the oil inlet, then tighten the screw (recommended torque: 7.85Nm)
- 4 If oil has spilled over, wipe it up. Otherwise, the peripheral equipment may be affected adversely.
- 5 If there is oil left over, put the inner lid back on the bottle, and keep the bottle in a dark, cool place.

## (3) Replacement method

- 1 Get a container for oil drain on hand, and put the tip of the drain tube into the container.
- 2 Turn the oil drain cock through 90 degrees, and the oil will start  draining.  Opening  the  oil  inlet  during  draining  can drain oil fast.
- 3 After all the oil has been drained, close the oil drain cock by setting it back in the initial place.
- 4 Supply oil by following the same procedure as for replenishment.

## CAUTION

After replacing the turbo blower oil, perform discharge aging.

B-70254EN/01

## 4.3.2 Changing the Exhaust Pump Oil

## (1) Check method

Watch  the  oil  gauge,  and  check  that  the  oil  level  is  between graduations L and H.    Also check whether the oil is dark.

If the oil level is below L, add oil to the turbo blower or replace the oil in it.    If the oil level is above H, drain until the oil level becomes below H.

<!-- image -->

The exhaust of the turbo blower contains oil mist. The exhaust pump will capture oil mist, and the amount of exhaust pump oil increases  with  time.  When  the  oil  has  increased  too  much,  the filter  gets  immersed  in  the  oil,  possibly  causing  white  mist  to come out from the pump, or oil to leak. Furthermore, the exhaust capacity may get lowered, or the pump may be damaged.

B-70254EN/01

## (2) Replacement method

- 1 Stop the oscillator, and turn off the power.
- 2 Remove  the  oil  inlet  plug.  There  is  an  O-ring  on  it.  Be careful not to damage it. A missing or damaged O-ring can lower the exhaust capacity of the pump.
- 3 Insert  the  drain  tube  into  a  drain  oil  vessel  then  open  the drain cock.
- 4 After the oil has been drained up, close the cock.
- 5 Supply  1.8  liters  of  new  oil  through  the  oil  inlet,  while watching the oil gauge.
- 6 Attach the oil inlet plug.

## 4.3.3 Replacing the Exhaust Pump Filter

When the operation time reaches 3000 hours or the exhaust capacity gets lowered, replace the filter. A clogged filter may cause a whitish smoke  of  oil  mist  to  come  out  of  the  pump  or  lower  the  exhaust capacity.

<!-- image -->

- 1 Stop the oscillator, and turn off the power.
- 2 Remove  the  black  screw  from  the  exhaust  pump  unit,  then remove the filter cover and O-ring.
- 3 Remove the spring and washer.
- 4 Pull out the filter element.
- 5 Check  the  mounting  orientation  of  a  new  filter  element,  then insert the filter. A filter mounted improperly may cause oil mist (whitish smoke) to come out of the exhaust pump gas outlet.

Therefore, check again that the filter is mounted properly.

Replacement work is now complete.

B-70254EN/01

## 4.4 MAINTENANCE PARTS

The following table lists maintenance parts.

Order a consumable from the machine tool builder or FANUC service center by the corresponding specification number listed below.

|    | Name                | Specification                                                         |
|----|---------------------|-----------------------------------------------------------------------|
|  1 | Turbo blower oil    | A04B-0800-K326                                                        |
|  2 | Exhaust pump oil    | SA-H (Manufactured by Matumura Sekiyu Co. Ltd. ) A98L-0040-0093/1.0L6 |
|  3 | Exhaust pump filter | A98L-0001-0911                                                        |

B-70254EN/01

## 4.5 COOLING WATER

## 4.5.1 Cooling Water Specification

The  quality  of  cooling  water  is  specified  in  the  table  below.  If  tap water is used, it should be treated in an ion exchanger.

## Refrigerator/air-conditioner cooling water quality standard

## (JRA-9001-1980)

| Standard item   | pH (25 ° C)           | pH (25 ° C)           | pH (25 ° C)           | 6.0 to 8.0         |
|-----------------|-----------------------|-----------------------|-----------------------|--------------------|
| Standard item   | Conductivity (25 ° C) | Conductivity (25 ° C) | Conductivity (25 ° C) | 200 µ s/cm or less |
| Standard item   | Chlorine ion Cl -     | Chlorine ion Cl -     | Chlorine ion Cl -     | 20ppm or less      |
| Standard item   | Sulfate ion SO 4 2-   | @ @                   | @ @                   | 50ppm or less      |
| Standard item   | Malkalinity CaCO 3    | Malkalinity CaCO 3    | @ @ @                 | 50ppm or less      |
| Standard item   | Total hardness CaCO 3 | Total hardness CaCO 3 | @ @ @                 | 50ppm or less      |
| Reference item  | Iron Fe               | @ @ @                 | @ @ @                 | 0.3ppm or less     |
| Reference item  | Sulfur ion S 2-       | @ @                   | @ @                   | Not to be detected |
|                 | Ammonia ion NH 4 +    | @                     | @ @                   | 0.2ppm or less     |
|                 | Ionic silica SiO 2    | Ionic silica SiO 2    | @ @                   | 30ppm or less      |

Add  the  following  anticorrosive  to  cooling  water  immediately  after installation to prevent problems due to corroding cooling water and to decrease the frequency of replacement of cooling water.

Consult the chiller manufacturer for use of the anticorrosive.

Product name:

CONTLIME K-6000

Manufacturer:

MITSUBISHI GAS CHEMICAL. ISC

Use:

Add the anticorrosive to cooling water in concentration of 1000 ppm (100 cc/100 liters). Monthly check the concentration of the anticorrosive using concentration check paper dedicated to anticorrosives  and  add  the  anticorrosive  to  cooling  water  until the concentration reaches about 1000 ppm.

Concentration check paper:

Purchase a concentration check set (50 sheets of check paper, a dropping pipette, etc.) together  with  CONTLIME  K-6000 (manufactured by Mitsubishi Gas Chemical ISC).

If the above anticorrosive is added to cooling water and the concentration is controlled, also be sure to replace the cooling water every year.

## [Reference]    Cooling water capacity of the oscillator

| Model     | Water capacity   |
|-----------|------------------|
| C1000 i A | About 5 liters   |

## 4.5.2 Anticorrosive

B-70254EN/01

## 4.5.3 Cleaning Agent

To remove foreign matters such as fur that have adhered to the inside of the cooling water circulating path, wash  the cooling  water circulating  path  using  the  following  detergent.  Consult  the  chiller manufacturer for use of the detergent.

Product name:

DESLIME

Manufacturer:

MITSUBISHI GAS CHEMICAL ISC

Add  the  detergent  of  10%  of  the  amount  of  cooling  water, circulate the water for an hour, then drain the water. After that, rinse the cooling water circulating path thoroughly. Do not touch a stock solution of DESLIME with your bare hands because the solution  is  a  strong  chemical.  If  a  stock  solution  accidentally contacts  your  skin,  wash  the  stock  solution  off  your  skin  well under running water.

If  waste  water  used  for  washing  is  left  standing,  the  main ingredient, hydrogen peroxide, is decomposed. Wait until hydrogen  peroxide  is  decomposed,  or  dilute  waste  water  with water  to  reduce  the  concentration,  then  flush  the  waste  water down the drain.

## 4.5.4 Antifreezing Solution

If the chiller is used in a cold district, it should be provided with an antifreezing function.    When it is extremely cold, the chiller should be kept running.

If  it  is  necessary  to  use  an  antifreezing  solution  for  lack  of  an alternative,  he  following  antifreezing  solution  should  be  used.    Its concentration should be 30% (usually) or 40% (in an extremely cold district).    Use of an antifreezing solution should be restricted within four months in winter. Do not use antifreezing solution together with an anticorrosive. The following antifreezing solution is already added with an anticorrosive.

Product name:

AURORA BRINE

Manufacturer:

TOKYO FINE CHEMICAL Co.

Use:

Refer to the description indicated on the product.

Use:

B-70254EN/01

## 4.5.5 Pure Water Supply Unit

It is recommended that a pure water supply unit (ion-exchange resin) be  installed  at  the  water  inlet  of  the  chiller.  The  pure  water  supply unit  can  prevent  problems  with  the  oscillator  from  occurring  due  to corrosion or a clogged pipe.    Replace the water periodically because the quality of the circulating cooling water is lowered.

Product name:

Pure Water Supply Cartridge

Manufacturer:

ORUGANO Co. Ltd.

Use:

Refer to the description indicated on the product.

B-70254EN/01

## 4.6 LASER GAS

## 4.6.1 Laser Gas Specification

Supply  the  laser  oscillator  with  a  mixture  of  gases  that  satisfy  the conditions listed below.

- (1) Composition ratio and accuracy
- (2) Water (H2O):    5 ppm or less
- (3) Hydrocarbon (CnHm):    1 ppm or less
4. (4)
5. Gas purity:    99.99% or higher

CO2 :

5 ± 0.25%

He :

40 ± 2.00%

N2 :

55 ± 2.75% (N2 balance)

Observe  the  following  cautions  for  piping  between  the  laser  gas cylinder and laser oscillator.

- (1) Use  nylon  tube  having  an  inside  diameter  of  8  mm  or  larger (Junlon AS1 manufactured by Junkousha, or equivalent). Do not use a rubber or urethane tube.
- (2) Use a swage-lock vacuum joint. Do not use a one-touch coupler, quick coupler, or hose-band joint.
- (3) Minimize the length of tubing.    It  should  be  kept  within  5  m. Never exceed 15 m. For a length of 15 m or greater, use stainless pipe.
- (4) If it is necessary to use metal pipe for lack of an alternative, use stainless  bright  annealed  pipe.  Minimize  the  number  of  joints used.  Connect  pipes,  if  necessary,  using  a  swage-lock  vacuum joint or by TIG welding. Do not use silver soldering or copper piping. Piping should be installed by a vacuum piping specialist. Do not extend metal piping over 30 m.
- (5) Always  keep  the  piping  materials  clean.  Do  not  allow  foreign matter to get in the pipe.
- (6) Use a pressure reducer that is free from gas leakage.
- (7) After installing the pipe, check it for gas leakage, using a liquid leak  checker  (Gyupoflex  :  A98L-0001-0856,  detecting  bubbles caused by leaking gas) or a clamp test1).

## Clamp test

Open the valve of the gas cylinder to pressurize the inside of the pipe,  then  close  the  valve.  Check  to  see  if  the  pressure  in  the pipe becomes low with time. Monitor the primary pressure of the gas reducer for over 8 hours. If the gas pressure becomes lower by  10%  within  8  hours,  gas  is  likely  to  be  leaking.  Take  an appropriate measure.

## 4.6.2 Gas Pipe

|   5 . TROUBLESHOOTING | B-70254EN/01    |
|-----------------------|-----------------|
|                     5 | TROUBLESHOOTING |

B-70254EN/01

## 5.1 TROUBLESHOOTING PROCEDURE

If  an  alarm  occurs,  the  alarm  number and message are displayed  on the CNC screen.

## CHECKING ON FAULTS

After identifying the following items, call the FANUC service center. In  some  cases,  a  symptom  is  not  actually  a  fault  in  the  oscillator, although it looks like a fault. So, check it with the following sections.

- (1) Symptoms
2. (a) State of operation

(machining in progress, oscillator being started, etc.)

- (b) Timing of a fault (alarm)
- (c) Alarm number
- (d) How often the fault occurs
- (e) Oscillator serial number
- (2) Other information
- (a) Software system and edition indicated on the CNC screen when power is turned on

check the current parameter settings with the corresponding values indicated on the unit, and report your finding to the

- (b) Parameter settings; FANUC service center.

## 5 . TROUBLESHOOTING B-70254EN/01

## 5.2 ALARM MESSAGE LIST

|   Alarm number | Contents             |
|----------------|----------------------|
|           4061 | A/D CONVERTER \ P    |
|           4062 | A/D CONVERTER \ Q    |
|           4063 | RF POWER SUPPLY      |
|           4065 | SHUTTER ACTION       |
|           4066 | DISCHARGING          |
|           4067 | LASER CABINET OH     |
|           4068 | BEAM REFLECTION      |
|           4069 | LASER IF PCB         |
|           4070 | CHILLER NOT READY    |
|           4071 | ASSIST GAS NOT READY |
|           4072 | CHILL FLOW           |
|           4073 | LASER GAS PRES.      |
|           4075 | CHILL TEMP.          |
|           4076 | LASER POWER DOWN     |
|           4077 | ABSORBER TEMP.       |
|           4078 | LASER TUBE PRES.     |
|           4079 | PUSH RESET KEY       |
|           4080 | LASER TUBE EXHAUST   |
|           4081 | GAS PRES. CONTROL    |
|           4082 | TUBE PRES.SENSOR     |
|           4085 | MIRROR CLEANING      |
|           4087 | SHUTTER OH           |
|           4088 | LASER VOLTAGE DOWN   |
|           4089 | ASSIST GAS NO SELECT |
|           4090 | LASER NOT GENERATE   |
|           4094 | VANE PUMP            |
|           4099 | GAS PRES.NOT REACH   |

B-70254EN/01

## 5.3 RESPONDING TO ALARM MESSAGES ON THE SCREEN

## ALM No.4061

## ALM No.4062

## ALM No.4063

## AD converter 1 is not normal.

|   No. | Cause of trouble          | Solution                                                                                                  |
|-------|---------------------------|-----------------------------------------------------------------------------------------------------------|
|     1 | Anomaly of AD converter 1 | It is necessary to replace AD converter 1 mounted on B8 on A16B-2100-0141. Call the FANUC service center. |
|     2 | Anomaly of IF PCB         | I It is necessary to replace the IF PCB (A16B- 2100-0141). Call the FANUC service center.                 |

## AD converter 2 is not normal.

|   No. | Cause of trouble          | Solution                                                                                                  |
|-------|---------------------------|-----------------------------------------------------------------------------------------------------------|
|     1 | Anomaly of AD converter 2 | It is necessary to replace AD converter 2 mounted on D7 on A16B-2100-0141. Call the FANUC service center. |
|     2 | Anomaly of IF PCB         | Replace the IF PCB (A16B-2100-0141).                                                                      |

## Anomaly of laser power supply unit

This  alarm  is  displayed  if  an  error  occurs  in  the  laser  power supply unit or the power  supply unit performs protective operation. Fully check the cause of the error because the power supply unit also performs protective operation if an error occurs in other than the power supply unit itself. This alarm will recur after replacement of the power supply alone without eliminating the root cause.

## (1) Preliminary inquiry

|    | Check item                     | Solution                                                                                                                                                                                                                                                                                             |
|----|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Checking parameters            | Confirm that all the parameters described in the attached parameter sheets are correctly set. In case there exists any error, correct it.                                                                                                                                                            |
|  2 | Checking the discharge tubes   | 1) Check whether the mounting bracket of a discharge tube are loose or missing. 2) Check whether the electrode has separated. 3) Check whether the inside and outside of a discharge tube is dirty. 4) Check the discharge tubes for a crack. 5) Check the O-ring of each discharge tube for damage. |
|  3 | Checking the trigger electrode | Check whether the trigger electrode is dirty.                                                                                                                                                                                                                                                        |
|  4 | Checking the matching box      | 1) Check whether the matching box fan stops. 2) Check whether any coil in the matching box becomes black.                                                                                                                                                                                            |

B-70254EN/01

|    | Check item                         | Solution                                                                        |
|----|------------------------------------|---------------------------------------------------------------------------------|
|  5 | Checking cooling water temperature | Confirm that the cooling water temperature is in the range of 20 ° C to 30 ° C. |
|  6 | Checking cable connectors          | Check the cables and connectors connected to the power supply for looseness.    |
|  7 | Insufficient discharge aging       | Perform aging operation.                                                        |

## (2). Confirming operation and investigating the cause of a fault

|    | Phenomenon                                                                                                                                                                                                                                                                                                    | Presumption cause                                                                                                 |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|  1 | An alarm is issued when the LED of a laser power supply unit is not turned on.                                                                                                                                                                                                                                | The IF PCB is faulty. Poor cable contact                                                                          |
|  2 | An alarm occurs before discharge begins. An instantaneous HVON alarm occurs.                                                                                                                                                                                                                                  | The laser power supply is defective.                                                                              |
|  3 | The RF current is small in comparison with other power supply units and the discharge tends to disappear.                                                                                                                                                                                                     | The laser power supply is maladjusted.                                                                            |
|  4 | The RF discharge current is large in comparison with other units. The alarm is DCV alarm.                                                                                                                                                                                                                     | The laser power supply is maladjusted.                                                                            |
|  5 | The RF voltage of all the units is high during discharge and the laser power is low. The discharge tends to disappear. When the purge is repeatedly performed, the RF voltage gradually decreases and the laser power recovers. This phenomenon often appears after the laser was not used for a long period. | The external laser gas pipe is abnormal. The gas composition is not normal due to leakage of a gas.               |
|  6 | The RF voltage of all the units is high during discharge and the laser power is low. The discharge is tends to disappear. Even though the purge is repeatedly performed, the situation does not recover.                                                                                                      | Internal leakage of oscillator Internal leakage of water of the oscillator                                        |
|  7 | The RF voltage of all the units is high during discharge but the laser power is normal. The discharge is tends to disappear. The output is high for the high output command, and it is lower than the standard for the low output command.                                                                    | The intra-tube pressure of the laser gas is high or the gas composition is not normal (excessive amount of N 2 ). |
|  8 | The RF voltage of all the units is low during discharge and the laser power is low. The discharge is widely spread. In the high laser power region, the power is low but in the low power region, it is higher than the normal value. The alarm is DCV alarm.                                                 | The intra-tube pressure of the laser gas is high or the gas composition is not normal (excessive amount of He).   |
|  9 | Although the RFV, RFI, and output are normal, an alarm may occur.                                                                                                                                                                                                                                             | Anomaly of the Laser power-supply unit itself (anomaly of alarm circuit).                                         |

B-70254EN/01

(3).Solution

## 5 . TROUBLESHOOTING

|    | Cause of trouble                                     | Solution                                                                                                                                                                                               |
|----|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | External laser gas pipe abnormal                     | Check the faulty sections, then improve external piping.                                                                                                                                               |
|  2 | Laser gas composition ratio abnormal                 | Replace the laser gas with one that satisfies the specification. If there is a leakage in external piping, the gas composition in the gas cylinder connected to the piping for a long time may change. |
|  3 | Discharge tube abnormal                              | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                          |
|  3 | IF PCB abnormal                                      | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                          |
|  4 | Laser power supply abnormal                          | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                          |
|  5 | Laser power supply maladjusted                       | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                          |
|  6 | Pressure sensor abnormal                             | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                          |
|  7 | Internal leakage, leakage of water, or faulty O-ring | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                          |

## Shutter anomaly

This alarm occurs when the shutter does not operate normally for the  shutter  open/close  commands.  The  table  below  lists  the causes of the fault and the corresponding countermeasures.

|   No. | Cause of trouble                  | Solution                                                                      |
|-------|-----------------------------------|-------------------------------------------------------------------------------|
|     1 | Shutter clamp not removed.        | Remove the shutter clamp.                                                     |
|     2 | Anomaly of position detector      | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     3 | Shutter cam loosened.             | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     4 | Shutter arm caught.               | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     5 | Relay PCB B abnormal              | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     6 | Anomaly of cables connecting PCB. | It is necessary to replace or adjust the part. Call the FANUC service center. |

## Discharge anomaly

After  HV  is  turned  on,  the  discharge  starts.  This  alarm  occurs when at least one discharge tube discharges hard and causes high voltage.

|   No. | Cause of trouble                 | Solution                                                                               |
|-------|----------------------------------|----------------------------------------------------------------------------------------|
|     1 | Anomaly of parameter setting     | Check whether the numeric values in the parameter list supplied with the unit are set. |
|     2 | Anomaly of laser gas composition | Use the laser gas with the specified composition and purity.                           |

## ALM No.4065

## ALM No.4066

ALM No.4067

ALM No.4068

B-70254EN/01

|   No. | Cause of trouble                                 | Solution                                                                      |
|-------|--------------------------------------------------|-------------------------------------------------------------------------------|
|     3 | Loose fixing parts of electrode                  | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     4 | Leakage in the vacuum system or leakage of water | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     5 | The gas flow control value is closed             | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     6 | Anomaly of matching box                          | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     7 | Crack or pinhole in discharge tube               | It is necessary to replace or adjust the part. Call the FANUC service center. |

## Overheating laser oscillator housing

The temperature of the input side of the electrode cooling fan is monitored  and  sends  alarm  when  it  exceeds  60 ° C.  When  the temperature  decreases,  the  alarm  state  is  solved  automatically. Before that it cannot be reset. (The C1000 i A does not have the sensor.)

|   No. | Cause of trouble                               | Solution                                                                             |
|-------|------------------------------------------------|--------------------------------------------------------------------------------------|
|     1 | Excessive environmental temperature            | Lower the ambient temperature by ventilation (5 to 30 )                              |
|     2 | Excessive cooling water temperature            | Set the temperature of the cooling water to within an appropriate range (20 to 30 ). |
|     3 | Anomaly of cooling fan motor                   | It is necessary to replace or adjust the part. Call the FANUC service center.        |
|     4 | Anomaly of temperature sensor                  | It is necessary to replace or adjust the part. Call the FANUC service center.        |
|     5 | Anomaly of oscillator IF PCB(A16B-2100-0141)   | It is necessary to replace or adjust the part. Call the FANUC service center.        |
|     6 | Anomaly of connecting cables between the PCBs. | It is necessary to replace or adjust the part. Call the FANUC service center.        |

## Too much incident laser beam back to the resonator..

This  alarm  is  issued,  if  a  workpiece  reflects  laser  beam  more than the rating to the laser oscillator.    This can happen when the laser beam is used to drill, cut, or weld materials (such as copper, brass, and aluminum) having a high reflectivity to the laser beam (10.6 µ m).

|    | Cause of trouble                                 | Solution                                                                                                                        |
|----|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
|  1 | Excessive returning beam back into the resonator | Lower the output specified in the command, or take an action to reduce the reflected laser beam.                                |
|  2 | Anomaly of parameter for alarm detection         | Check the settings of parameter Nos. 15265 and 15266 with the corresponding values in the parameter table attached to the unit. |
|  3 | Anomaly of parameter for output power table      | Check the settings of parameter Nos.15280 to 15308 with the corresponding values in the parameter table attached to the unit.   |

B-70254EN/01

## 5 . TROUBLESHOOTING

|    | Cause of trouble                                       | Solution                                                                                                                                                                                                           |
|----|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  4 | Anomaly of parameter for input calibration coefficient | Set the parameter PRM. No.15215 to be the values as shown in the attached table. After replacing the rear mirror or power sensor, it is necessary to change this parameter setting. Call the FANUC service center. |

## Anomaly of power supply unit voltage of IF PCB

This  alarm  appears  when  there  occurs  the  anomaly  in  the stabilized power unit voltage +5, ± 15, +24V of IF PCB for NC interface.

|   No. | Cause of trouble                               | Solution                                                                         |
|-------|------------------------------------------------|----------------------------------------------------------------------------------|
|     1 | Fuse blowing                                   | It is necessary to replace or adjust the part. Call the FANUC service center.    |
|     2 | Anomaly of stabilized power source unit        |                                                                                  |
|     3 | Anomaly of power unit of IF PCB                |                                                                                  |
|     4 | Laser oscillator main circuit breaker abnormal | Check whether the main circuit breaker is in the complete continuity (ON) state. |

## Anomaly of chiller unit

Setting the RUN ON switch to ON causes the CNC to output a chiller unit start signal to the machine, which will respond with a chiller  unit  ready  signal.  The  CNC  monitors  this  signal.  If  the chiller ready signal stops, the CNC issues this alarm. Check the operation of the chiller.

## Anomaly of assist gas

When starting machining, the CNC monitors for a ready signal from the assist gas supply unit in the machine.    If this signal is not sent normally, the CNC issues this alarm.

Check  the  operation  of  the  assist  gas  supply  unit.  Also  check whether there is the assist gas.

This alarm is issued also when in G32P α Q β , α is not 0 to 3, or β is not 1 to 7 during program execution.

## ALM No.4069

## ALM No.4070

## ALM No.4071

## 5 . TROUBLESHOOTING

## ALM No.4072

ALM No.4073

B-70254EN/01

## Shortage of cooling water

This alarm appears when the water shortage takes place.

|   No. | Cause of trouble                  | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 | Shortage of cooling water         | 1 The capacity of the chiller unit is insufficient, or the water flow rate is reduced due to a clogged pipe. Use a chiller unit having sufficient capacity, or clean the piping. 2 Check whether the cooling water is distributed normally throughout between the external optical system and the laser oscillator. Ensure that cooling water is supplied to the laser oscillator at the specified flow rate. This alarm is issued if cooling water is supplied at a flow rate even slightly below the specified value. |
|     2 | Anomaly of sensor cable           | It is necessary to replace or adjust the part.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     3 | Anomaly of water flow rate sensor | Call the FANUC service center.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Decrease of laser gas pressure

The pressure of  the laser  gas  supplied  to  the  laser  oscillator  is monitored.

This  alarm  is  issued,  if  this  pressure  becomes  lower  than  the permissible level.

|   No. | Cause of trouble                                    | Solution                                                                                                                                                                                                                                                                                                                                   |
|-------|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 | Tool low supply pressure of laser gas               | Adjust the secondary pressure at the regulator on the gas cylinder so that the pressure of laser gas supplied to the laser oscillator is 0.15MPa (rating) as measured at the entry of the oscillator. If the distance between the gas cylinder and the oscillator is larger than 5 m, it is necessary to set the pressure slightly higher. |
|     2 | No laser gas.                                       | Check whether the gas cylinder is empty or whether the connection valve is closed. If empty, replace the gas cylinder.                                                                                                                                                                                                                     |
|     3 | Leakage from the gas tube leading to the oscillator | Check that the gas pipe joint is secure. Also check whether the tube or pipe is broken. If so, replace it.                                                                                                                                                                                                                                 |
|     4 | Gas supply pressure sensor or cable abnormal        | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                              |

B-70254EN/01

## ALM No.4075

## ALM No.4076

## ALM No.4077

## Condensation

A condensation sensor is mounted near the output mirror holder in  the  oscillator.  This  alarm  occurs  when  the  sensor  detects condensation. After this alarm occurs, the alarm status cannot be reset until the condensation status is released. Do not blow hot air of 60 ° C or higher on the condensation sensor. Flowing dry air in the oscillator is effective.

|   No. | Cause of trouble                                | Solution                                                                      |
|-------|-------------------------------------------------|-------------------------------------------------------------------------------|
|     1 | Tool low cooling water temperature              | Set the water temperature near the room temperature (plus about 1 ° C).       |
|     2 | Connecting anomaly of condensation sensor cable | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     3 | Anomaly of condensation sensor                  | It is necessary to replace or adjust the part. Call the FANUC service center. |

## Laser gas pressure decrease

This alarm is issued, if the monitored laser output is much lower than the specified laser output, that is the monitored laser output is  lower  than  the  specified  output  by  a  value  specified  in parameter No. 15271.

|   No. | Cause of trouble                                            | Solution                                                                      |
|-------|-------------------------------------------------------------|-------------------------------------------------------------------------------|
|     1 | Lack of output from laser power sensor unit                 | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     2 | Connecting anomaly of the cable of laser power sensor unit. | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     3 | Anomaly of intermediate PCB B A16B-1600-0361                | It is necessary to replace or adjust the part. Call the FANUC service center. |

## Overheat of beam absorber

Laser  beam  is  introduced  into  the  beam  absorber,  when  the oscillation  takes  place  with  shutter  closed.  This  absorber  is water-cooled  and  sends  alarm  when  the  temperature  of  the absorber  exceeds  a  critical  one.  In  the  usual  operation,  the irradiation of the absorber takes place only during the calibration after the oscillator start.

|   No. | Cause of trouble                     | Solution                             |
|-------|--------------------------------------|--------------------------------------|
|     1 | Insufficient cooling water           | It is necessary to replace the part. |
|     2 | Temperature sensor wired incorrectly | Call the FANUC service center.       |
|     3 | Temperature sensor abnormal          |                                      |
|     4 | Absorber abnormal                    |                                      |

## ALM No.4078

## ALM No.4079

## ALM No.4080

B-70254EN/01

## Gas pressure anomaly in discharge tube

The  gas  pressure  is  monitored  after  the  discharge  start  ready condition  (LRDY)  is  established.  This  alarm  is  issued,  if  the monitored gas pressure deviates by ± 100 (1330Pa) from the set gas pressure.

|   No. | Cause of trouble                                     | Solution                                                                                                                                                                                                                                                                                                                                          |
|-------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 | Anomaly of parameter setting of gas pressure control | Check whether the values of PRM NO. 15000/bit1,15244,15245,15246 are set as indicated in the attached data sheets. If a different value is set, set the value specified in the data sheets.                                                                                                                                                       |
|     2 | Abnormal supply laser gas pressure setting           | Adjust the secondary pressure at the regulator on the gas cylinder so that the pressure of laser gas supplied to the laser oscillator is 0.1 to 0.2 MPa (rating) as measured at the entry of the oscillator. If the distance between the gas cylinder and the oscillator is larger than 5 m, it is necessary to set the pressure slightly higher. |
|     3 | Leakage in circulating system                        | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                                     |
|     4 | Stopped turbo blower                                 | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                                     |
|     5 | Anomaly of pressure sensor                           | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                                     |
|     6 | The gas flow control valve is closed.                | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                                     |
|     7 | Anomaly of gas control unit                          | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                                     |

## Press the RESET key

The emergency stop button was pressed.

If the emergency stop button is pressed after the discharge start ready condition (LRDY)  is  set up, the shutter is closed, discharge stops, and the LRDY condition is resumed, then this alarm  is  displayed.  To  reset  the  alarm,  remove  the  cause  of trouble,  release  the  emergency  stop  button,  and  press  the  reset key on the operator' s panel.

## Leakage of gas tube/anomaly of exhaust pump

When the RUN ON switch is turned on, the exhaust pump starts evacuating the gas in the circulating  system to place the oscillator in the low-pressure state. This alarm occurs when the pressure does not reach the exhaust completion pressure specified  for  parameter  No.  15240  until  the  specified  time (default: 10 minutes) has elapsed after the start of exhaust.

|   No. | Cause of trouble                                 | Solution                                                                                                                                                     |
|-------|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 | Incorrect gas pressure control parameter setting | Check if the value of PRM No. 15240 is set as indicated in the attached data sheets. If a different value is set, set the value specified in the data sheets |

B-70254EN/01

## 5 . TROUBLESHOOTING

|   No. | Cause of trouble                          | Solution                                                                      |
|-------|-------------------------------------------|-------------------------------------------------------------------------------|
|     2 | Anomaly of IF PCB A16B-2100-0141          | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     3 | Gas leakage from piping                   | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     4 | Anomaly of gas connection of exhaust pump | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     5 | Anomaly of exhaust pump                   | It is necessary to replace or adjust the part. Call the FANUC service center. |

## Anomaly of gas pressure control

When the RUN ON switch is turned on, the vacuum pump starts evacuation. After the pressure is lowered to the specified value, the laser gas is introduced into the pipe, and gas pressure control starts.

Whether  the  pressure  is  within ± 20  (266  Pa)  of  the  pressure specified  for  parameter  No.15241  is  checked,  45  seconds  after the  start  of  gas  pressure  control.  This  alarm  occurs  when  the pressure does not fall within this range. When no error occurs, the turbo blower rotates and the discharge start ready condition (LRDY) is established.

|   No. | Cause of trouble                                     | Solution                                                                                                                                                                                                                                                                                                                                          |
|-------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 | Anomaly of parameter setting of gas pressure control | Check whether the values of PRM Nos. 15000#1, 15244, 15245, 15246 are set as indicated in the attached data sheets. If a different value is set, set the value specified in the data sheets.                                                                                                                                                      |
|     2 | Anomaly of supply laser gas pressure                 | Adjust the secondary pressure at the regulator on the gas cylinder so that the pressure of laser gas supplied to the laser oscillator is 0.1 to 0.2 MPa (rating) as measured at the entry of the oscillator. If the distance between the gas cylinder and the oscillator is larger than 5 m, it is necessary to set the pressure slightly higher. |
|     3 | Gas leakage from piping                              | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                                     |
|     4 | Anomaly of IF PCB A16B-2100-0141                     | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                                     |
|     5 | Anomaly of pressure sensor                           | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                                     |
|     6 | Anomaly of pressure control valve                    | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                                                                     |

## ALM No.4081

## 5 . TROUBLESHOOTING

## ALM No.4082

## ALM No.4083

## ALM No.4085

B-70254EN/01

## Anomaly of pressure sensor

This alarm appears when the signal of the pressure sensor used vanishes.

|   No. | Cause of trouble                                                            | Solution                                                                      |
|-------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|     1 | Open or poor contact in connection cable between pressure sensor and IF PCB | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     2 | Anomaly of IF PCB                                                           | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     3 | Anomaly of pressure sensor                                                  | It is necessary to replace or adjust the part. Call the FANUC service center. |

## Shutter failure to open

This  alarm  occurs  when  the  shutter  does  not  reach  the  correct position at a certain time (pre-flow time of assist gas) after the shutter open command.

|   No. | Cause of trouble                                                      | Solution                                                                      |
|-------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------|
|     1 | The pre-flow time of assist gas is too short for the shutter to open. | Adjust the pre-flow time on setting screen. It should be longer than 0.6 sec. |
|     2 | When beam output was specified, other alarm was issued.               | Check the cause of occurred alarm, then take appropriate action.              |
|     3 | Movable part caught                                                   | It is necessary to replace or clean the part. Call the FANUC service center.  |

## Decrease of laser output power

This alarm appears when the laser output power decreases and takes an abnormally higher calibration coefficient.

|   No. | Cause of trouble                                            | Solution                                                                                                                               |
|-------|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|     1 | An optical part in the laser resonator is out of position.  | It is necessary to align the laser resonator or to clean or replace an optical part. Call the FANUC service center.                    |
|     2 | An optical part in the laser resonator is dirty.            | It is necessary to align the laser resonator or to clean or replace an optical part. Call the FANUC service center.                    |
|     3 | The supplied laser gas is not the one specified.            | Replace the laser gas with the specified one, that is CO 2 :N2:He = 5:55:40% (volume ratio) with a composition ratio accuracy of ± 5%. |
|     4 | Cooling water temperature out of specified range            | Check whether the temperature of cooling water falls within the range of 20 to 30 ° C.                                                 |
|     5 | Laser oscillator ambient temperature out of specified range | Check whether the ambient temperature falls within the range of 5 to 30 ° C.                                                           |

B-70254EN/01

## ALM No.4087

## ALM No.4088

ALM No.4089

## Shutter temperature abnormal

This alarm is issued when the temperature of the shutter mirror exceeds a preset maximum. The table below lists the causes of faults and the corresponding countermeasures.

|   No. | Cause of trouble                                                    | Solution                                                                                                                                                  |
|-------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 | Contamination of shutter mirror                                     | Clean the shutter mirror. If this alarm recurs after the shutter mirror is cleaned, it is necessary to replace the mirror. Call the FANUC service center. |
|     2 | Anomaly of temperature sensor                                       | It is necessary to replace the part. Call the FANUC service center.                                                                                       |
|     3 | Temperature sensor cable broken                                     | It is necessary to replace the part. Call the FANUC service center.                                                                                       |
|     4 | Relay PCB B (A16B- 1600-0361) or IF PCB (A16B-2100-0141) is faulty. | It is necessary to replace the part. Call the FANUC service center.                                                                                       |
|     5 | Anomaly of PCB connection cables                                    | It is necessary to replace the part. Call the FANUC service center.                                                                                       |

## Discharge tube voltage drop

This alarm is issued, if the voltage applied to the discharge tube drops largely.

More specific, the discharge tube voltage for reference discharge is  set  up  automatically  to  parameter  No.  15270  each  time  the RUN button is pressed.

This  alarm  is  issued,  if  the  automatically  set  discharge  tube voltage  is  lower  than  the  discharge  voltage  specified  at  the previous  RUN  time, by at least the  amount specified in parameter No. 15272.

|   No. | Cause of trouble                                                | Solution                                                                                                                               |
|-------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|     1 | The laser gas composition is not as specified.                  | Replace the laser gas with the specified one, that is CO 2 :N2:He = 5:55:40% (volume ratio) with a composition ratio accuracy of ± 5%. |
|     2 | Anomaly of discharge tube voltage detection system              | It is necessary to replace the part. Call the FANUC service center.                                                                    |
|     3 | Reduced blowing capacity of turbo blower or anomaly of inverter | It is necessary to replace the part. Call the FANUC service center.                                                                    |

## Assist gas not output

This alarm is issued, if an attempt is made to radiate a laser beam, when no assist gas is selected, or an assist gas condition is not set up.

## 5 . TROUBLESHOOTING

## ALM No.4090

## ALM No.4094

## ALM No.4099

## ALM No.4100

B-70254EN/01

## Laser beam not generated

This alarm is issued, if an attempt is made to radiate a laser beam, when the laser  oscillator  is  not  in  the  LSTR  state  (discharging state).

## Vacuum pump operation abnormal

This  alarm  occurs  when  the  thermal  switch  of  the  magnetic contactor for the exhaust pump is tripped.

|   No. | Cause of trouble                | Solution                                                                          |
|-------|---------------------------------|-----------------------------------------------------------------------------------|
|     1 | Clogged exhaust pump filter     | Replace the exhaust pump filter.                                                  |
|     2 | Clogged exhaust pump air outlet | Clean the outlet and remove the foreign matters with which the outlet is clogged. |
|     3 | Anomaly of thermal switch       | It is necessary to replace the part. Call the FANUC service center.               |
|     4 | Anomaly of IF PCB               | It is necessary to replace the part. Call the FANUC service center.               |
|     5 | Signal cable broken             | It is necessary to replace the part. Call the FANUC service center.               |

## Gas pressure not reached

This alarm is issued, if the discharge tube gas pressure does not reach [specified discharge tube gas pressure during oscillation tolerance] after HV is set to ON.

|   No. | Cause of trouble                 | Solution                                                                                                                                                                                     |
|-------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 | Invalid parameter setting        | Check whether the values of PRM Nos. 15001/bit3, 15247, and 15248 are set as indicated in the attached data sheets. If a different value is set, set the value specified in the data sheets. |
|     2 | Gas leakage from internal piping | It is necessary to locate the leakage and replace the related part.                                                                                                                          |
|     3 | Pressure sensor abnormal         | Call the FANUC service center.                                                                                                                                                               |

## Inverter abnormal

If the inverter used to power the turbo blower is abnormal, this alarm is issued.

When this alarm is issued, check that the alarm LED on the LED indicator section of the inverter is lit. At this time, do not turn off the power to the inverter because the alarm will be reset if the power is turned off.

For an explanation of faults and corresponding countermeasures, see the Maintenance Manual (B-70255EN)

|   No. | Cause of trouble          | Solution                                                                                                    |
|-------|---------------------------|-------------------------------------------------------------------------------------------------------------|
|     1 | Excessive intake pressure | Check whether the values of PRM Nos. 15240, 15241, and 15242 are set according to the attached data sheets. |

B-70254EN/01

## 5 . TROUBLESHOOTING

|   No. | Cause of trouble               | Solution                                                                      |
|-------|--------------------------------|-------------------------------------------------------------------------------|
|     2 | Turbo blower rotor locked      | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     3 | Failed bearing in turbo blower | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     4 | Invalid inverter setting       | It is necessary to replace or adjust the part. Call the FANUC service center. |

## Inverter frequency reached signal abnormal

This alarm is issued, if a frequency reached signal is not received within 120 seconds after the turbo blower is started.

|   No. | Cause of trouble          | Solution                                                                      |
|-------|---------------------------|-------------------------------------------------------------------------------|
|     1 | Cable connection abnormal | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     2 | Faulty turbo blower       | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     3 | Inverter abnormal         | It is necessary to replace or adjust the part. Call the FANUC service center. |
|     4 | Invalid inverter setting  | It is necessary to replace or adjust the part. Call the FANUC service center. |

## Turbo blower temperature abnormal

This  alarm  is  issued,  if  the  temperature  of  the  turbo  blower motor winding becomes higher than the permissible level.

|   No. | Cause of trouble                               | Solution                                                                                                                                                                                                                                                                                          |
|-------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 | Cooling water temperature high                 | Reduce the temperature of the cooling water.                                                                                                                                                                                                                                                      |
|     2 | Insufficient cooling water                     | The amount of cooling water supplied to the turbo blower may be insufficient. Check whether the cooling water tube between the water branch unit and blower is twisted or clogged. If the tube is twisted or clogged, replace the tube. If a tube in the turbo blower is clogged, clean the tube. |
|     3 | Anomaly of temperature sensor                  | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                     |
|     4 | Anomaly of temperature sensor cable connection | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                     |
|     5 | Anomaly of turbo blower                        | It is necessary to replace or adjust the part. Call the FANUC service center.                                                                                                                                                                                                                     |

## Low turbo blower oil

This alarm is issued if the signal from the turbo blower oil sensor indicates that the oil level has fallen below the setting.

|   No. | Cause of trouble                       | Solution                                                                                                                                                                      |
|-------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 | The oil level is lower than specified. | Replenish the turbo blower with oil until the oil level on the oil gauge is between H and L. Replace the oil every 1000 hours of operation.                                   |
|     2 | Insufficient turbo blower cooling      | When the temperature of the turbo blower motor section is high, check whether the cooling water path is clogged. If the cooling water path is clogged, wash the turbo blower. |

## ALM No.4101

## ALM No.4105

## ALM No.4106

## 5 . TROUBLESHOOTING

## ALM No.4107

## ALM No.4132

B-70254EN/01

|   No. | Cause of trouble       | Solution                                       |
|-------|------------------------|------------------------------------------------|
|     3 | Invalid sensor setting | It is necessary to replace or adjust the part. |
|     4 | Sensor abnormal        | Call the FANUC service center.                 |

## External reflecting mirror not installed

This alarm is issued, if the beam reflecting unit is not attached with  a  mirror  or  mirror  holder.  (The  C1000 i A  has  no  beam folding unit.)

|   No. | Cause of trouble   | Solution                                       |
|-------|--------------------|------------------------------------------------|
|     1 | Mirror not mounted | Mount a mirror.                                |
|     2 | Sensor abnormal    | It is necessary to replace or adjust the part. |
|     3 | Cable abnormal     | Call the FANUC service center.                 |

## Parameter changed (warning)

Press the RESET key to release this alarm.

## APPENDIX

B-70254EN/01

<!-- image -->

A

## EXTERNAL VIEW OF LASER OSCILLATOR

Fig. A    EXTERNAL VIEW OF LASER OSCILLATOR

<!-- image -->

<!-- image -->

B-70254EN/01

## B SPECIFICATIONS

| Item                                 | Item                                         | Contents                                                                                                      |
|--------------------------------------|----------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Type                                 | Type                                         | FANUC LASER MODEL-C1000 i A                                                                                   |
| Method                               | Method                                       | High-speed axial carbon dioxide gas laser by high-frequency discharge excitation                              |
| Structure                            | Structure                                    | Combination resonator/power supply type (separate exhaust pump)                                               |
| Rated laser output                   | Rated laser output                           | 1,000W                                                                                                        |
| Maximum laser output                 | Maximum laser output                         | 1,000W (continuously variable output range of 100W or greater)                                                |
| Pulse peak value                     | Pulse peak value                             | 1,000W                                                                                                        |
| Output stability                     | Output stability                             | ± 1% (for 8-hour rated output under output feedback control)                                                  |
| Laser wavelength                     | Laser wavelength                             | 10.6 µ m                                                                                                      |
| Beam mode                            | Beam mode                                    | Low-order mode                                                                                                |
| Beam diameter(at oscillator outlet)  | Beam diameter(at oscillator outlet)          | Approximately φ 20 mm or less                                                                                 |
| Polarization                         | Polarization                                 | 45 ° polarization                                                                                             |
| Angle of beam divergence(full angle) | Angle of beam divergence(full angle)         | 2 mrad or less                                                                                                |
| Pulse output command frequency       | Pulse output command frequency               | 5 to 2,000 Hz                                                                                                 |
| Pulse output command duty factor     | Pulse output command duty factor             | 0 to 100%                                                                                                     |
| Laser gas                            | Composition                                  | Mixture of CO 2 :He:N 2 = 5:40:55% (volume ratio with N 2 balance) with a composition ratio accuracy of ± 5%. |
| Laser gas                            | Gas pressure                                 | 0.175 ± 0.025 MPa (0.15 to 0.20 MPa) measured on a gauge                                                      |
| Laser gas                            | Consumption                                  | About 10 liters/h                                                                                             |
| Cooling water                        | Amount                                       | 40 liters/min or more                                                                                         |
| Cooling water                        | Temperature / Temperature stability          | 20 ° C to 30 ° C/ ± 1 ° C (for laser output stability of ± 1%)                                                |
| Cooling water                        | Circulating water pressure                   | 0.5MPa or less on a gauge                                                                                     |
| Cooling water                        | Recommended cooling capacity of chiller unit | 11 kW or more                                                                                                 |
| Power requirements                   | Power requirements                           | 200VAC +10%, -15% 50/60 Hz ± 1Hz or 220VAC +10%, -15% 60 Hz ± 1Hz                                             |
| Required input power                 | Required input power                         | 18 kVA                                                                                                        |
| Maximum current                      | Maximum current                              | 60 A                                                                                                          |
| Hour meter                           | Hour meter                                   | Total operation hours of the exhaust pump                                                                     |
| Door interlock                       | Door interlock                               | No                                                                                                            |
| Warning lamp                         | Warning lamp                                 | Blinks while discharge is in progress.                                                                        |
| Weight                               | Weight                                       | Main oscillator unit: About 350 kg Exhaust pump unit: About 30 kg                                             |

B-70254EN/01

<!-- image -->

## C PARAMTER LIST

This appendix describes the parameters for the Series 16 i -L. Many parameters depend on the laser oscillator model and unit. Check  the  parameter  list  in  the  data  sheet  supplied  with  each  unit, then set parameters.

LIST                                                                                                                                B-70254EN/01

## C.1 PARAMETERS FOR ENABLING/DISABLING VARIOUS FUNCTIONS

<!-- image -->

Data type:

Bit

LPC

Power control function

0: Invalid (standard)

1: Valid

LGC

Two stage gain selection of intra-tube pressure control

- 0: Invalid

- 1: Valid (standard)

(When this bit is 1, PRM No. 15245 becomes valid.)

AGA Assist gas preparation check with beam on

- 0: Valid (standard)

- 1: Invalid (for maintenance)

BMO

Beam on only with beam off

- 0: Invalid (standard)

- 1: Valid (for manual only and maintenance)

- CLB

Power compensation

- 0: Disabled

- 1: Enabled (standard)

FLT Filter in power control

- 0: Invalid

- 1: Valid (standard)

<!-- image -->

Data type:

Bit

EXA

Selection of assist gas

0: 3 types (standard)

1: 7 types

G0B

When G00 is specified, a beam

- 0: Outputs (standard).

- 1: Does not output.

- PES

Piercing time during machine lock or dry run

- 0: Enabled (standard)

- 1: Disabled

NGC

- 0: Presets an integral gas pressure control value.

- 1: Does not preset an integral gas pressure control value.

- PC8 The power compensation function

- 0: Specifies a fixed value for the power.

- 1: Increases the power in eight levels.

B-70254EN/01

## LHC

- 0: Does not control the oscillator with external signals (standard).
- 1: Controls the oscillator with external signals. In  the  automatic  operation  mode,  external  signals  are  used  to turn on and off the shutter and beam output.

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15002 |      | PSH  |      |      |      |      | ADC  | BMA  |

Data type:

Bit

BMA

- 0: Disables  beam  output  with  the  shutter  closed  in  the  automatic operation mode (standard).

- 1: Enables  beam  output  with  the  shutter  closed  in  the  automatic operation mode (for maintenance).

## ADC

- 0: Uses the select signal to determine AD converter 2 data.

- 1: the DI signal to determine AD converter 2 data. (standard)

PSH

- 0: Uses all discharge tubes.

- 1: Uses half of the discharge tubes.

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15003 |      |      |      |      |      | GVW  | HPT  | TIV  |

Data type:

Bit

TIV

- 0: Inverts the sign (+/-) of the amount of tracing displacement.

- 1: Does  not invert the sign (+/-) of the amount  of tracing displacement.

## HPT

- 0: Rewrites parameter settings for extending or shortening piercing.

- 1: Does not rewrite parameter settings for extending or shortening piercing.

## GVW

- 0: Disables evacuation when RUN is turned off.

- 1: Enables evacuation when RUN is turned off.

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15004 | CWY  | ECH  |      | EDG  |      | SPB  | STC  | AGC  |

Data type:

Bit

AGC

- 0: Uses  the  "G32  P\_;"  command  (when  Q,  T,  and  R  are  not specified) as the flow pattern command.

- 1: Uses  the  "G32  P\_;"  command  (when  Q,  T,  and  R  are  not specified) as the gas pressure control direct command.

STC

- 0: Controls the shutter with a G code.

- 1: Controls the shutter with an external signal.

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

SPB

EDG

ECH

CWY

- 0: Outputs a beam in skip operation.
- 1: Outputs no beam in skip operation.
- 0: Turns the  beam  off  when  switching  the  assist  gas  during  edge machining.
- 1: Does not turn the beam off when switching the assist gas during edge machining.
- 0: Does not clear the active E number upon reset.

1:

Clears the active E number upon reset.

- 0: A CO2 laser oscillator is used.
- 1: A CW-YAG laser oscillator is used.

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15005 | DLY  | ITR  |      | GNS  | BPV  | TTD  |      | INB  |

Data type:

Bit

INB

- 0: Stops beam output upon completion of pulse distribution.

1: Stops beam output upon completion of in-position check.

TTD

0:

Each laser power supply drives only one discharge tube.

1:

Each laser power supply drives two discharge tubes.

BPV

- 0: Opens the bypass valve during power calibration.

1: Closes the bypass valve during power calibration.

GNS

- 0: Stops  the  assist  gas  output  during  assist  gas  switching  by  the assist gas direct command. (standard)

- 1: Does not stop assist gas output during assist gas switching by the assist gas direct command.

ITR

- 0: Disables the tracing control interlock signal (G227#6 *TRIL).

1:

Enables the tracing control interlock signal (G227#6 *TRIL).

DLY

- 0: Disables the beam output condition delay function.

- 1: Enables the beam output condition delay function.

|       | #7   | #6   | #5   | #4   | #3   | #1   | #0   |
|-------|------|------|------|------|------|------|------|
| 15006 |      |      | PCN  | PCL  |      | TRM  | NCC  |

Data type:

Bit

NCC

0:

Displays the processing condition setting screen.

- 1: Does not display the processing condition setting screen.

B-70254EN/01

## TRM

PIN

PCL

## PCN

## ECK

## XSC

## STO

- 0: Enables the zero-point, start-point and end-point soft keys for the trace setting screen.
- 1: Disables  the  zero-point,  start-point  and  end-point  soft  keys  for the trace setting screen.
- 0: Specifies a G13 address P using metric input.
- 1: Specifies a G13 address P using inch input.
- 0: On-screen pressure display of assist gas in kg/cm 2 .
- 1: On-screen pressure display of assist gas in MPa.
- 0: Rewrites the power compensation factor with 1024 when power compensation is not performed.
- 1: Does not rewrite the power compensation factor and retains the previous value when power compensation is not performed.

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15007 |      |      | STO  | XSC  | ECK  | ESE  |      |      |

## Data type: Bit ESE

- 0: After completion of distribution, executes piercing during edge machining.
- 1: After  completion  of  distribution,  checks  the  smoothing  errors, then executes piercing during edge machining.
- 0: Determines the angle on the actual processing path during edge machining.
- 1: Determines  the  angle  on  the  path  in  the  machining  program during edge machining.
- 0: Does not operate the edge machining function in the exact stop mode.
- 1: Operates the edge machining function in the exact stop mode.
- 0: Does not execute the after-flow and pre-flow when the assist gas command is issued with the same type and same flow pattern.
- 1: Executes the after-flow and pre-flow when  the assist gas command is issued with the same type and same flow pattern.

LIST                                                                                                                                B-70254EN/01

<!-- image -->

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15008 | RMP  | EGE  | DCW  |      | SOC  | TAL  | GPC  | MST  |

## Data type: MST

GPC

TAL

SOC

DCW

EGE

RMP

Bit

- 0: When a reference displacement amount is specified with a plus sign  (+)  in  the  trace  command,  the  nozzle  approaches  the workpiece. When a reference displacement amount is specified with a minus  sign (-), the nozzle  moves  away  from  the workpiece.
- 1: When a reference displacement amount is specified with a plus sign (+) in the trace command, the nozzle moves away from the workpiece. When a reference displacement amount is specified with a minus sign (-), the nozzle approaches the workpiece.
- 0: Exercises tracing control according to the reference displacement amount.
- 1: Exercises tracing control according to the gap amount (distance between the nozzle and workpiece).
- 0: Invalidates the "out-of-tracing-range alarm"  when  the trace check mode signal (G225#2 TRCKM) is set to "1."
- 1: Invalidates both of the "out-of-tracing-range alarm" and "excess tracing  displacement  alarm"  when  the  trace  check  mode  signal (G225#2 TRCKM) is set to "1."
- 0: Uses the reference displacement amount for piercing as that for tracing control not during  processing  when  the  processing condition setting function is used.
- 1: Uses the reference displacement amount for piercing as that for tracing control only during piercing when the processing condition setting function is used.
- 0: Does  not  display  the  DCV,  DCI,  and  DCW  values  on  the diagnostic display.
- 1: Displays  the  DCV,  DCI,  and  DCW  values  on  the  diagnostic display.
- 0: Disables the automatic aging function.
- 1: Enables the automatic aging function.
- 0: The  step  function  uses  only  the  up/down  step  distances  to measure the travel distance.
- 1: The step function uses the up/down step distances and feedrate setting to measure the travel distance.

B-70254EN/01

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15009 | TEM  | BCG  | BEM  | AFZ  | BS2  | BS1  | AS2  | AS1  |

Data type:

Bit

AS1,AS2,BS1,BS2

Parameters for the laser gas mixing function.

This function stores and monitors the operating status of the mixer.

These parameters need not be set manually because they are automatically set.

AS2,AS1 Indicates the status of tank A.

|   AS2 |   AS1 | Status                                        |
|-------|-------|-----------------------------------------------|
|     0 |     0 | Filling gases in tank A                       |
|     0 |     1 | Mixing gases in tank A                        |
|     1 |     0 | Supplying gases in tank A                     |
|     1 |     1 | Setup for filling gases in tank A in progress |

|   BS2 |   BS1 | Status                                        |
|-------|-------|-----------------------------------------------|
|     0 |     0 | Filling gases in tank B                       |
|     0 |     1 | Mixing gases in tank B                        |
|     1 |     0 | Supplying gases in tank B                     |
|     1 |     1 | Setup for filling gases in tank B in progress |

- 1: Does  not  include  the  Z-axis  in  calculation  for  actual  cutting feedrate display.
- 0: Includes  the  Z-axis  in  calculation  for  actual  cutting  feedrate display.
- 1: The supply pressure of the three-gas cylinder is normal.
- 0: The supply pressure of the three-gas cylinder is low.
- 1: The three-gas cylinder is not replaced.
- 0: The three-gas cylinder is replaced.
- 1: The tank supply pressure is normal.
- 0: The tank supply pressure is low.

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15010 | OVE  |      | TRG  |      |      |      |      |      |

Data type:

Bit

TRG

- 0: Disables the trigger pulse command control function.

- 1: Enables the trigger pulse command control function.

OVE

- 0: Does not allow edge machining and feedrate clamp based on arc radius to be used together.

- 1: Allows edge machining and feedrate clamp based on arc radius to be used together.

## AFZ

## BEM

## BCG

TEM

LIST                                                                                                                                B-70254EN/01

<!-- image -->

## Data type: EDS

LVE

Bit

- 0: Uses the conventional conditions as the cutting conditions during execution of edge machining or start-up processing for a return.
- 1: Uses the piercing operating conditions in edge machining for the laser  power,  assist  gas  type,  and  assist  gas  pressure  as  cutting conditions during  execution of  edge  machining  or  start-up processing for a return.
- 0: Performs  assist  gas  switching  according  to  the  conventional specifications at the start of edge machining and at the start of cutting for the return distance after that.
- 1: Ignores the time setting when the gas type and pressure do not change  for  assist  gas  switching  at  the  start  of  edge  machining and at the start of cutting for the return distance after that.
- CSC When  the  following  four  values,  S,  P,  Q,  and  F,  are  concurrently specified  in  the  first  G01,  G02,  or  G03  block  following  G24  in  the start-up processing mode,
- 0: Executes  conventional  start-up  processing  without  using  the specified S, P, Q, and F values.
- 1: Cancels  operation  of  start-up  processing  and  performs  cutting using the specified S, P, Q, and F values.
- 0: The  external  piping  exhaust  valve  operates  only  once  after power-on.
- 1: The external piping exhaust valve always operates when RUN is turned on.

OPV

B-70254EN/01

## C.2 PARAMETERS FOR DISCHARGE TUBE SELECTION

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15025 | PS8  | PS7  | PS6  | PS5  | PS4  | PS3  | PS2  | PS1  |
| 15026 | PS16 | PS15 | PS14 | PS13 | PS12 | PS11 | PS10 | PS9  |

Data type: PS1 to PS16

Bit

Discharge tube selection when half of the discharge tubes are used Set the bit for each discharge tube to be used to 1, and set the other bits to 0.

## NOTE

Parameter No. 15026 is provided for future addition of discharge tubes. In the current specifications, this parameter is not used. Set all bits to 0.

<!-- image -->

|    #7 | #6   | #5   | #4   | #3   | #2   | #1   | #0   |     |
|-------|------|------|------|------|------|------|------|-----|
| 15027 | PS8  | PS7  | PS6  | PS5  | PS4  | PS3  | PS2  | PS1 |
| 15028 | PS16 | PS15 | PS14 | PS13 | PS12 | PS11 | PS10 | PS9 |

Data type: PS1 to PS16

Bit

Discharge tube selection when all discharge tubes are used Set the bit for each discharge tube to be used to 1, and set the other bits to 0.

## NOTE

Parameter No. 15028 is provided for future addition of discharge tubes. In the current specifications, this parameter is not used. Set all bits to 0.

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

## C.3 PARAMETERS FOR CONTOURING CONDITIONS

15040

Data type:

Word

Unit of data:

W

Range of data:

0 to 7000

15041

Data type:

Word

Unit of data:

Hz

Range of data:

5 to 2000

15042

Data type:

Word

Unit of data:

%%

Range of data:

0 to 100

## Power output setting

## Pulse frequency setting

## Pulse duty ratio setting

B-70254EN/01

## C.4 PARAMETERS FOR EDGE MACHINING CONDITIONS

15050

## Edge detection angle

Data type:

Word

Unit of data:

deg

Range of data:

0 to 180

A  corner  is  assumed  to  be  present  when  the  angle  formed  by  two blocks is smaller than the specified angle.

15051

## Peak piercing power value

Data type:

Word

Unit of data:

W

Range of data:

0 to 7000

Set a peak power value for piercing to be performed at the top of a corner.

15052

## Piercing pulse frequency

Data type:

Word

Unit of data:

Hz

Range of data:

5 to 2000

Set  a  pulse  frequency  for  piercing  to  be  performed  at  the  top  of  a corner.

15053

## Piercing pulse duty ratio

Data type:

Word

Unit of data:

%

Range of data:

0 to 100

Set  a  pulse  duty  ratio  for  piercing  to  be  performed  at  the  top  of  a corner.

15054

## Piercing time

Data type:

Two-word

Unit of data:

msec

Range of data:

0 to 99999999

Set a piercing time used for piercing to be performed at the top of a corner.

15055

## Piercing assist gas pressure

Data type:

Word

Unit of data:

0.01Mpa or 0.1 kg/cm 2

Range of data:

0 to 255

Set an assist gas pressure for piercing to be performed at the top of a corner.

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

15056

## Type of piercing assist gas

Data type:

Word

Unit of data:

Range of data:

0 to 7

Set a type of assist gas to be used for piercing.

15057

Data type:

Two-word

Unit of data:

## Return distance

| Setting range   |   IS-A |   IS-B |   IS-C | Unit   |
|-----------------|--------|--------|--------|--------|
| Metric input    |  0.01  | 0.001  | 0.0001 | mm     |
| Inch input      |  0.001 | 0.0001 | 1e-05  | inch   |

Range of data:

0 to 65000

Set a return distance from the top of a corner to the next block.

15058

## Return feedrate

Data type:

Word

Unit of data:

mm/min

Range of data:

0 to 9999

Set a return feedrate to be used for movement from the top of a corner to the next block.

15059

## Peak return power value

Data type:

Word

Unit of data:

W

Range of data:

0 to 7000

Set a peak return power value to be used for movement from the top of a corner to the next block.

15060

## Return frequency

Data type:

Word

Unit of data:

Hz

Range of data:

5 to 2000

Set  a  return  frequency  to  be  used  for  movement  from  the  top  of  a corner to the next block.

15061

## Return duty ratio

Data type:

Word

Unit of data:

%

Range of data:

0 to 100

Set a return duty ratio to be applied to movement from the top of a corner to the next block.

B-70254EN/01

## C.5 PARAMETERS FOR PIERCING CONDITIONS

15080

Data type:

Word

Unit of data:

W

Range of data:

0 to 7000

Set the piercing power.

15081

## Initial piercing frequency

Data type:

Word

Unit of data:

Hz

Range of data:

5 to 2000

Set the initial piercing frequency.

15082

## Incremental piercing frequency

Data type:

Word

Unit of data:

Hz

Range of data:

0 to 2000

Set the incremental piercing frequency.

15083

## Initial piercing duty ratio

Data type:

Byte

Unit of data:

%

Range of data:

0 to 100

Set the initial piercing duty ratio.

15084

## Incremental piercing duty ratio

Data type:

Byte

Unit of data:

%

Range of data:

0 to 100

Set the incremental piercing duty ratio.

15085

## piercing step time

Data type:

Word

Unit of data:

msec

Range of data:

0 to 32767

Set the piercing step time.

## Piercing power

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

15086

## Number of piercing steps

Data type:

Word

Unit of data:

Range of data:

0 to 32767

Set the number of piercing steps

15087

## Piercing end time

Data type:

Two-word

Unit of data:

msec

Range of data:

0 to 99999999

Set the piercing end time

B-70254EN/01

## C.6 PARAMETERS FOR POWER CONTROL

|       | #7   | #6   | #5   | #4   | #3   | #2   | #1   | #0   |
|-------|------|------|------|------|------|------|------|------|
| 15089 | LP8  | LP7  | LP6  | LP5  | LP4  | LPZ  | LPY  | LPX  |

Data type: LP*

Bit

- 0: Does  not  use  the  *-axis  for  speed  calculation  for  the  power control function.
- 1: Uses  the  *-axis  for  speed  calculation  for  the  power  control function.

If  no  bit  is  specified,  the  power  control  function  operates,  assuming the first axis (LPX) and second axis (LPY) to be specified.

Ordinarily,  specify  each  axis  to  be  used  for  interpolation.  Do  not specify  a  synchronously  controlled  axis  for  simple  synchronous control or PMC axis.

## 15090

Data type:

Word

Unit of data:

W

Range of data:

0 to 7000

15091

Data type:

Word

Unit of data:

Hz

Range of data:

5 to 2000

15092

## Minimum output power

## Minimum pulse frequency

## Minimum pulse duty ratio

Data type:

Word

Unit of data:

%

Range of data:

0 to 100

Set the minimum pulse duty ratio.

## 15093

## Power control constant

Data type:

Word

Unit of data:

%

Range of data:

0 to 100

Set the power control constant.

15094

## Power control filter time constant

Data type:

Word

Unit of data:

msec

Range of data:

0 to 32767

Set the power control filter time constant.

LIST                                                                                                                                B-70254EN/01

15095

## Allowable variation in power control speed

Data type:

Byte

Unit of data:

mm/min (specified increment for B8F1-08 or earlier) or %

Range of data:

0 to 255

Standard setting:

4

Set the amount by which the power control speed is allowed to vary. This parameter is valid when parameter No. 15450 is set to 0. To set a value of 256 or greater, use parameter No. 15450. Set this parameter according to the setting of bit 6 of parameter No.

15096 (SDB) as follows.

<!-- image -->

Data type:

Bit

PCP

- 0: Does not control the output according to the feedrate in power control.
- 1: Controls the output according to the feedrate in power control.
- 0: Does  not  control  the  frequency  according  to  the  feedrate  in power control.
- 1: Controls  the  frequency  according  to  the  feedrate  in  power control.
- 0: Does  not  control  the  duty  ratio  according  to  the  feedrate  in power control.
- 1: Controls  the  duty  ratio  according  to  the  feedrate  in  power control.
- 0: Cancels the power control mode in the edge machining or startup processing mode.
- 1: Stops power control only during return distance movement in the edge machining or start-up processing mode.

In the edge machining or start-up processing mode, the E number for specifying  conditions  for  edge  machining  or  start-up  processing  is selected.

15097

## Parameter for calculating the displacement of the output (output at a speed of F = 0)

Data type:

Word

Unit of data:

v

Range of data:

0 to 7000

## PCF

## PCD

## EGM

B-70254EN/01

15098

## C . PARAMTER LIST

Parameter for calculating the displacement of the frequency (frequency at a speed of F = 0)

Data type:

Word

Unit of data:

Hz

Range of data:

5 to 2000

15099

Parameter for calculating the displacement of the duty ratio (duty ratio at a speed of F = 0)

Data type:

Word

Unit of data:

Range of data:

0 to 100

LIST                                                                                                                                B-70254EN/01

## C.7 PARAMETERS FOR ASSIST GAS PRESSURE AND TIME SETTING

15100

Data type:

Unit of data:

Range of data:

15101

Data type:

Unit of data:

Range of data:

15102

15103

15104

Data type:

Unit of data:

Range of data:

15108

15109

15110

Word

10msec

0 to 32767

Set the assist gas pre-flow time.

After-flow time 1

After-flow time 2

After-flow time 3

Data type:

Word

Unit of data:

10msec

Range of data:

0 to 32767

Set the assist gas after-flow time.

## Selection of assist gas

Word

0 to 7

Select a type of assist gas.

## Selection of flow pattern

Word

1 to 3

Select a assist gas flow pattern.

Pre-flow time 1

Pre-flow time 2

Pre-flow time 3

B-70254EN/01

15114

15115

15116

Pre-flow pressure 1

## Pre-flow pressure 2

## Pre-flow pressure 3

Data type:

Word

Unit of data:

0.01Mpa or 0.1 kg/cm 2

Range of data:

0 to 255

Set the assist gas pre-flow pressure.

15120

## Processing flow pressure 1

15121

## Processing flow pressure 2

15122

## Processing flow pressure 3

Data type:

Word

Unit of data:

0.01Mpa or 0.1 kg/cm 2

Range of data:

0 to 255

Set the assist gas processing flow pressure.

15126

15127

15128

## After flow pressure 1

## After flow pressure 2

## After flow pressure 3

Data type:

Word

Unit of data:

0.01Mpa or 0.1 kg/cm 2

Range of data:

0 to 255

Set the assist gas after-flow pressure.

15132

## Maximum assist gas pressure

Data type:

Word

Unit of data:

0.01Mpa or 0.1 kg/cm 2

Range of data:

0 to 255

Set an assist gas pressure    (kg/cm 2 (Mpa)) at which 10V is output in analog output.

15135

## Assist gas pressure set time

Data type:

Word

Unit of data:

10msec

Range of data:

0 to 32767

Set a desired assist gas pressure set time.

## C . PARAMTER LIST

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

15136

## Assist gas pressure

Data type:

Word

Unit of data:

0.01Mpa or 0.1 kg/cm 2

Range of data:

0 to 255

Set a desired assist gas pressure.

15137

## Assist gas pressure set time for piercing

Data type:

Word

Unit of data:

10msec

Range of data:

0 to 32767

Set a desired assist gas pressure set time for piercing.

15138

## Assist gas pressure for piercing

Data type:

Word

Unit of data:

0.01Mpa or 0.1 kg/cm 2

Range of data:

0 to 255

Set a desired assist gas pressure for piercing.

15139

## Assist gas stop time

Data type:

Word

Unit of data:

10msec

Range of data:

0 to 32767

Set the wait time when the assist gas stops.

B-70254EN/01

## C.8 PARAMETERS FOR LASER MAINTENANCE TIMING INDICATION FUNCTIONS

15150

## Laser RUN ON time

Data type:

Two-word

Unit of data:

0.1hour

Range of data:

0 to 99999999

A cumulative RUN ON time is automatically set.

15151

Data type:

Two-word

Unit of data:

0.1hour

Range of data:

0 to 99999999

A cumulative vacuum pump operation time is automatically set.

15152

## Shutter alarm mask time

Data type:

Word

Unit of data:

msec

Range of data:

0 to 32767

Set a time from when shutter operation is directed until shutter alarm monitoring starts.

<!-- image -->

Data type:

Bit

LCK

- 0: Disables the leakage check function.

- 1: Enables the leakage check function.

15154

## Leakage judgment time

Data type:

Word

Unit of data:

sec

Range of data:

3 to 65535

Set the time during which the valve is closed and the internal pressure of a discharge tube is kept for leakage check. The internal pressure of a discharge tube is measured four times within the specified time. If a value of 0 to 2 is set, the leakage check function does not operate.

## Vacuum pump operation time

LIST                                                                                                                                B-70254EN/01

<!-- image -->

## Data type: MNT

Bit

0: Does not display the laser maintenance screen.

- 1: Displays the laser maintenance screen.

When the  value  indicating  that  the  laser  maintenance  screen  is  not displayed is specified, the compensation factor is also stored and the cumulative  operating  time  is  also  set.  You  can  display  the  laser maintenance screen to check the data when required.

0: Disables data input on the laser maintenance screen.

- 1: Enables data input on the laser maintenance screen.

Data input on the laser maintenance screen is disabled to prevent the end user from entering data such as the operating time unintentionally. (The data can only be referenced.)

Setting this parameter to 1 enables data input.

MDS

B-70254EN/01

## C.9 PARAMETERS FOR THE OSCILLATOR

15200

## Power used for power compensation factor determination when half of the

## discharge tubes are used

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

Set a power to find the power compensation factor when half of the discharge tubes are used.

15201

## Power used for power compensation factor determination when all discharge tubes are used

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

Set a power to find the power compensation factor when all discharge tubes are used.

15203

Data type:

Word

Unit of data:

Range of data:

0 to 32767

If  the  power compensation factor exceeds this value, the low output alarm signal (F220#6 MWRN) is output to notify the user of the time to clean or replace the mirror.

15204

## Power calibration coefficient

Data type:

Word

Unit of data:

Range of data:

0 to 32767

This is to calibrate command power for real power. This parameter is automatically  set  at  power  compensation  after  the  oscillator  start signal (G222#6 RUN) is turned on.

15205

## Power compensation time

Data type:

Word

Unit of data:

sec

Range of data:

0 to 32767

Set a power compensation time.

## Power calibration limit

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

15206

## Time constant for the power sensor input filter

Data type:

Word

Unit of data:

msec

Range of data:

8 to 32767

This time constant is used when the laser power monitor value input from the power sensor is multiplied by the primary delay filter.

15207

## Maximum specifiable power

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

If  the  power  setting  after  power  compensation  or  power  feedback addition exceeds this value, the power output is clamped to this value.

15208

## Laser power feedback gain

Data type:

Word

Unit of data:

Range of data:

0 to 32767

Set the laser power feedback gain.

15209

## Power feedback clamp

Data type:

Word

Unit of data:

Range of data:

0 to 32767

This  clamp  value  is  used  to  prevent  the  excess  power  setting  from being made during power feedback.

15210

## Maximum command power

Data type:

Word

Unit of data:

W

Range of data:

0 to 7000

This is power clamp when power command is greater than this value.

15211

## Minimum command power

Data type:

Word

Unit of data:

W

Range of data:

0 to 7000

This is power clamp when power command is smaller than this value.

B-70254EN/01

15212

## Maximum specifiable power when the duty ratio is not clamped

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

If  PRM  No.  15213  does  not  clamp  the  duty  ratio  to  50%,  and  a specified  power  after  power  compensation  and  power  feedback processing exceeds the setting in this parameter, the power is clamped to the setting.

If a value of 0 is set, the setting of parameter No. 15207 is set.

15213

## Duty ratio clamp criterion

Data type:

Word

Unit of data:

W

Range of data:

0 to 7000

When a specified power multiplied by an override value exceeds the value set in this parameter, the duty ratio is clamped to 50%    (fixed value),  and  the  peak  value  is  clamped  to  the  value  set  in  PRM  No. 15210.0, the setting of parameter No. 15210 is set.

15214

## Maximum setting for the CW-YAG laser frequency

Data type:

Word

Unit of data:

Hz

Range of data:

0 to 32767

For a CW-YAG laser oscillator, the frequency setting is clamped to this value.

15215

## Power input calibration coefficient

Data type:

Word

Unit of data:

W

Range of data:

102 (0.1 × 2 10 ) to 10240 (10 × 2 10 )

(If 0 is specified, 1024 (10 × 2 10 ) is assumed.)

Set the power input compensation factor.

15216

## Power display filter time constant

Data type:

Word

Unit of data:

msec

Range of data:

0 to 32767

This  is  the  filter  time  constant  with  which  fluctuation  in  power display is suppressed.

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

15217

## Beam stop delay time

Data type:

Word

Unit of data:

msec

Range of data:

0 to 32767

Set the time between the in-position check and stop of the beam.

15218

## Maximum setting for the CW-YAG duty clamp output

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

If  the  specified  laser  output,  Pc,  for  a  CW-YAG  laser  exceeds  this setting, the duty limit is clamped to 100(%) .15218 × PRM .

Pc

If a value of 0 is set, 500 W is assumed.

15219

Data type:

Byte

Unit of data:

8msec

Range of data:

0 to 8

## Beam output condition delay time

B-70254EN/01

## C.10 PARAMETERS FOR DISCHARGE

15220

## Maximum bias command at discharge start

Data type:

Word

Unit of data:

mV

Range of data:

0 to 32767

Set the maximum bias setting at the start of discharge.

15221

## Voltage for conforming discharge

Data type:

Word

Unit of data:

V

Range of data:

0 to 32767

Set the discharge starting voltage.

15222

## Discharge waiting time

Data type:

Word

Unit of data:

10msec

Range of data:

0 to 32767

Specifies  the  waiting  time  until  the  discharge  is  checked  after  the maximum bias setting is specified at the start of discharge.

15223

Data type:

Word

Unit of data:

mV

Range of data:

0 to 32767

Specify the bias setting.

15224

## Modulation voltage

Data type:

Word

Unit of data:

mV

Range of data:

0 to 3000

Set  the  voltage  to  which  the  normal  bias  value  is  lowered  during modulation by the base modulation function.

15225

## Modulation time

Data type:

Word

Unit of data:

10msec

Range of data:

0 to 32767

Set the time during which the bias setting is lowered.

## Bias command

LIST                                                                                                                                B-70254EN/01

## C.11 PARAMETERS FOR GAS CONTROL (1)

15240

## Negative pressure in exhaust completion

Data type:

Word

Unit of data:

(1=13Pa)

Range  This  pressure  is  used  for  evacuating  the  discharge  tubes  in laser start-up sequence.

15241

## Intra-tube pressure in discharge start

Data type:

Word

Unit of data:

(1=13Pa)

Range of data:

0 to 32767

Internal gas pressure of the discharge tubes at the start of discharge

15242

## Tube pressure for oscillation    (50Hz)

Data type:

Word

Unit of data:

(1=13Pa)

Range of data:

0 to 32767

Internal  gas  pressure  of  the  discharge  tubes  during  laser  oscillation. (at 50 Hz)

15243

## Tube pressure for oscillation    (60Hz)

Data type:

Word

Unit of data:

(1=13Pa)

Range of data:

0 to 32767

Internal  gas  pressure  of  the  discharge  tubes  during  laser  oscillation. (at 60 Hz)

15244

## Gas pressure control gain

Data type:

Word

Unit of data:

Range of data:

0 to 32767

This is the gain to feedback control the intra-tube laser gas pressure.

15245

## Intratube pressure control gain 2

Data type:

Word

Unit of data:

Range of data:

0 to 32767

Set the gas pressure control gain during base discharge.

When bit 1 of parameter No.15000 is 1, this parameter is valid.

B-70254EN/01

15246

## Pressure control integration gain

Data type:

Word

Unit of data:

Range of data:

0 to 32767

This is feedback integration gain for gas pressure control.

15247

## Pressure control integral element preset value

Data type:

Word

Unit of data:

Range of data:

-32768 to 32767

Integral element preset value for gas pressure control

15248

## Allowable gas pressure insufficiency

Data type:

Word

Unit of data:

(1=13Pa)

Range of data:

0 to 32767

Allowable  value  used  to  determine  to  issue  no  alarm  if  the  gas pressure does not reach the setting

15249

## Gas pressure rising time

Data type:

Word

Unit of data:

sec

Range of data:

0 to 60

Set the gas pressure rising time in sequence 27.

15255

## RUN ON evacuation time

Data type:

Word

Unit of data:

sec

Range of data:

0 to 32767

Set the evacuation time at the RUN start.

15256

## RUN OFF evacuation time

Data type:

Word

Unit of data:

sec

Range of data:

600 to 32767

When bit 2 of parameter No. 15003 (GVW) is set 1 and the oscillator start  signal  (G222#6  RUN)  is  set  to  "0,"  evacuation  is  performed according to this time setting.

## C . PARAMTER LIST

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

15257

## Number of abnormal vibrations detected

Data type:

Word

Unit of data:

Range of data:

0 to 32767

If  the  number  of  abnormal  vibrations  detected  exceeds  the  value specified in this parameter, an alarm is issued.

15258

Time constant of the filter used for laser gas pressure variation suppression

Data type:

Word

Unit of data:

msec

Range of data:

17to  32767  (If  a  value  less  than  16  is  specified,  the  filter  does  not function.)

15259

## Exhaust time when RUN is ON

Data type:

Word

Unit of data:

sec

Range of data:

0 to 32767

Set a desired evacuation time when RUN is ON.

15260

## Period when the exhaust value of the external pipe is open

Data type:

Byte

Unit of data:

sec

Range of data:

0 to 60 (When a time beyond 60 sec is specified, the time is clamped to 60 sec.)

Set the time the exhaust valve of the external pipe is open.

B-70254EN/01

## C.12 PARAMETERS FOR HIGHLY REFLECTIVE MATERIAL ALARMS

15265

## Maximum allowable power increase

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

If the difference between the specified power and actual output power is greater than this value, beam reflection error alarm 4068 is issued.

15266

## Maximum allowable power

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

If  the  actual  output  exceeds  this  value,  beam  reflection  error  alarm 4068 is issued.

LIST                                                                                                                                B-70254EN/01

## C.13 PARAMETERS FOR LASER POWER/VOLTAGE DROP

15270

## Discharge tube voltage in normal operation

Data type:

Word

Unit of data:

V

Range of data:

0 to 32767

Set the discharge tube voltage during normal base discharge.

This  parameter  is  automatically  rewritten  after  the  discharge  start signal (G222#7 HVON) is turned on.

15271

## Power decrease limit

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

If  the  difference  between  the  specified  output  and  actual  output  is greater than this setting, low output alarm 4076 is issued.

15272

## Discharge tube voltage decrease limit

Data type:

Word

Unit of data:

V

Range of data:

0 to 32767

If the difference between the discharge tube voltage during use of the laser  and  that  at  the  start-up  of  the  laser  is  greater  than  this  setting, low voltage alarm 4088 is issued.

15276

## Laser gas replacement time

Data type:

Word

Unit of data:

sec

Range of data:

0 to 32767

Time  during  which  a  new  laser  gas  is  filled  in  the  internal  piping system after RUN is turned on

B-70254EN/01

## C.14 PARAMETERS FOR POWER TABLE SETTING

15280

15281

Table interval when half of the discharge tubes are used

Table interval when all discharge tubes are used

Data type:

Word

Unit of data:

Range of data:

0 to 32767

Standard setting:

Refer to the parameter data sheet delivered with the machine. Set the increment in watts used for the setting in the output command.

<!-- image -->

|   15290 | Power command 0 when half of the discharge tubes are used   |
|---------|-------------------------------------------------------------|
|   15291 | Power command 1 when half of the discharge tubes are used   |
|   15292 | Power command 2 when half of the discharge tubes are used   |
|   15293 | Power command 3 when half of the discharge tubes are used   |
|   15294 | Power command 4 when half of the discharge tubes are used   |
|   15295 | Power command 5 when half of the discharge tubes are used   |
|   15296 | Power command 6 when half of the discharge tubes are used   |
|   15297 | Power command 7 when half of the discharge tubes are used   |
|   15298 | Power command 8 when half of the discharge tubes are used   |

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

Standard setting:

Refer to the parameter data sheet delivered with the machine.

Sequentially  set  the  output  setting  starting  from  0  for  each  table interval when half of the discharge tubes are used.

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

<!-- image -->

|   15300 | Power command 0 when all discharge tubes are used   |
|---------|-----------------------------------------------------|
|   15301 | Power command 1 when all discharge tubes are used   |
|   15302 | Power command 2 when all discharge tubes are used   |
|   15303 | Power command 3 when all discharge tubes are used   |
|   15304 | Power command 4 when all discharge tubes are used   |
|   15305 | Power command 5 when all discharge tubes are used   |
|   15306 | Power command 6 when all discharge tubes are used   |
|   15307 | Power command 7 when all discharge tubes are used   |
|   15308 | Power command 8 when all discharge tubes are used   |

Data type:

Word

Unit of data:

W

Range of data:

0 to 32767

Standard setting:

Refer to the parameter data sheet delivered with the machine. Sequentially  set  the  output  setting  starting  from  0  for  each  table

interval when all discharge tubes are used.

B-70254EN/01

## C.15 AUTOMATIC AGING FUNCTION

15320

Data type:

Unit of data:

Range of data:

15321

Data type:

Unit of data:

Range of data:

15322

Data type:

Unit of data:

Range of data:

15323

Data type:

Unit of data:

Range of data:

15324

Data type:

Unit of data:

Range of data:

## Command power for power compensation coefficient calculation

Word

v

0 to 7000

## Oscillation frequency command for power compensation coefficient

Word

Hz

5 to 2000

## Pulse duty cycle command for power compensation coefficient

Word

%

0 to 100

## Command time for power compensation coefficient calculation

Word sec

0 to 32767

## Gas pressure setting for normal compensation (50Hz)

Word

(1=13Pa)

0 to 32767

15325

## Gas pressure setting for normal compensation (50Hz)

Data type:

Word

Unit of data:

(1=13Pa)

Range of data:

0 to 32767

15326

## Power command when aging is performed with the automatic aging

Data type:

Unit of data:

Range of data:

Word

v

0 to 7000

15327

Data type:

Word

Unit of data:

Hz

Range of data:

5 to 2000

## Oscillation frequency command for aging

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

15328

Data type:

Unit of data:

Range of data:

15329

Data type:

Unit of data:

Range of data:

15330

Data type:

Unit of data:

Range of data:

15331

Data type:

Unit of data:

Range of data:

15332

Data type:

Unit of data:

Range of data:

15333

Data type:

Unit of data:

Range of data:

15334

Data type:

Unit of data:

Range of data:

15335

Word

%

0 to 100

Word sec

0 to 32767

Word

(1=13Pa)

0 to 32767

Word

(1=13Pa)

0 to 32767

## Oscillation frequency command value for power compensation

Word

Hz

5 to 2000

## Pulse duty cycle command during power compensation

Word

%

0 to 100

Word

0 to 32767 (Automatically set by the CNC)

## Time data 1 when the HV is turned off after LSTR

Data type:

Two-word

Unit of data:

Year

Range of data:

0 to 99999999 (Automatically set by the CNC)

## Pulse duty cycle command for aging

## Power command time for aging

## Gas pressure setting (50 Hz) for aging

## Gas pressure setting (60 Hz) for aging

## Number of aging operations

B-70254EN/01

15336

## C . PARAMTER LIST

## Time data 2 when the HV is turned off after LSTR

Data type:

Two-word

Unit of data:

Month

Range of data:

1 to 12 (0 to 99999999) (Automatically set by the CNC)

15337

## Time data 3 when the HV is turned off after LSTR

Data type:

Two-word

Unit of data:

Day

Range of data:

1 to 31 (0 to 99999999) (Automatically set by the CNC)

15338

## Time data 4 when the HV is turned off after LSTR

Data type:

Two-word

Unit of data:

Hour

Range of data:

0 to 24 (0 to 99999999) (Automatically set by the CNC)

15339

## Stop time for the oscillator requiring aging operation

Data type:

Word

Unit of data:

hour

Range of data:

0 to 32767 (range of valid settings:    30 to 120)

If the setting is less than 30, internal processing assumes the value to be 60.

LIST                                                                                                                                B-70254EN/01

## C.16 POWER CONTROL (2)

15450

Data type:

Word

Unit of data:

mm/min

Range of data:

0 to 32767

Standard setting:

4

Set the amount by which the power control speed is allowed to vary. When  this  parameter  is  set  to  0,  parameter  No.  15095  is  valid. Parameter No. 15095 and this parameter differ in the range of valid settings.

For details of setting, see the explanation of parameter No. 15095.

## Allowable variation in power control speed

B-70254EN/01

## C.17 LASER GAS MIXER FUNCTION

15710

## Wait time for checking the remaining amount in the gas cylinder

Data type:

Word

Unit of data:

sec

Range of data:

0 to 32767

Standard setting:

Wait time when the remaining amount in the gas cylinder is checked

15711

Data type:

Word

Unit of data:

min

Range of data:

0 to 32767

Standard setting:

60

Time required until gas mixture is complete and the mixed gas can be supplied after gases are filled in the tank.

15712

## Gas mixer evacuation time

Data type:

Word

Unit of data:

min

Range of data:

0 to 32767

Standard setting:

30

Set  the  time  required  for  evacuating  the  mixer.    This  value  is  also used for the time required for evaluation for leakage check.

15713

Data type:

Word

Unit of data:

msec

Range of data:

0 to 32767

Standard setting:

Time required for exhausting the Helium gas from piping before the next gas is filled after the helium gas is filled

15714

Data type:

Word

Unit of data:

msec

Range of data:

0 to 32767

Standard setting:

Time required for exhausting the nitrogen gas or carbon dioxide gas from the piping before the next gas is filled after that gas is filled

## Nitrogen and CO2 exhaust time

## Helium exhaust time

## Gas mixture wait time

## C . PARAMTER

LIST                                                                                                                                B-70254EN/01

15715

Data type:

Word

Unit of data:

(1=13Pa)

Range of data:

0 to 32767

Standard setting:

This value is used for determining the degree of vacuum of the laser gas pressure in the gas mixer.

If the laser gas pressure does not reach this value, an alarm is issued.

## Evacuation wait time

15716

Data type:

Word

Unit of data:

min

Range of data:

0 to 32767

Standard setting:

Wait time for evacuation. If the setting is 0, a value of 30 is input.

## Vacuum criteria gas pressure

B-70254EN/01

## C.18 PARAMETERS FOR GAS PRESSURE CONTROL (2)

<!-- image -->

Data type: TPC

Bit

The  control  function  of  driving  the  turbo  blower  with  a  constant power

0: Invalid

1: Valid

15801

Maximum internal pressure when the control function of driving the turbo blower with a constant power is enabled

Data type:

Word

Unit of data:

(1=13Pa)

Range of data:

1 to 32767

Maximum setting for the internal laser pressure. If the internal laser pressure setting  calculated  from  the  laser  power  setting  exceeds  the setting of this parameter, the internal laser pressure is clamped to this value.

15802

Laser power setting used as the maximum internal pressure when the control function of driving the turbo blower at a constant power is enabled

Data type:

Word

Unit of data:

W

Range of data:

1 to 32767

Laser power setting used when the setting of parameter No. 15801 is used as the internal laser pressure setting. The proportional constant for  the  internal  laser  gas  pressure  setting  and  laser  power  setting  is determined using this parameter and parameter No. 15801.

15803

Compensation factor for the internal pressure setting when the control function of driving the turbo blower at a constant power is enabled

Data type:

Word

Unit of data:

1/1024

Range of data:

0 to 32767

Compensation  factor  by  which  the  internal  laser  pressure  setting  is multiplied. When the parameter setting is 1024, compensation factor 1.0 is used for multiplication.

15804

Maximum exhaust valve open time for internal pressure control during oscillation

Data type:

Word

Unit of data:

msec

Range of data:

0 to 3000

Set the maximum open time for exhaust valve PCV.

B-70254EN/01

<!-- image -->

## D GLOSSARY

| Name                          | Meaning                                                                                                                                                                                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <A>                           |                                                                                                                                                                                                                                                           |
| Access panel                  | That protective component of a housing or enclosure which, when removed or shifted, can cause exposure to laser radiation.                                                                                                                                |
| AEL Accessible emission level | Maximum accessible emission level set up for each class of laser products                                                                                                                                                                                 |
| Alignment                     | Optical axis adjustment                                                                                                                                                                                                                                   |
| Aperture                      | Iris, or stop                                                                                                                                                                                                                                             |
| <B>                           |                                                                                                                                                                                                                                                           |
| Beam                          | Aggregate of unidirectional, diverging, or conversing rays                                                                                                                                                                                                |
| Beam diameter                 | Distance between two symmetrical points in a cross section of a beam where the power per unit area is 1/e as high as the maximum power per unit area                                                                                                      |
| Beam divergence               | Angle through which a beam spreads                                                                                                                                                                                                                        |
| Burn pattern                  | Laser beam mode pattern generated on a plate such as an acrylic plate for confirmation purposes                                                                                                                                                           |
| <C>                           |                                                                                                                                                                                                                                                           |
| Circular Polarization         | Polarization in which a plane of polarization rotates about the axis along which the light progresses and does not have directivity; an electric or magnetic field based on circular polarization has a constant intensity.                               |
| CO 2 laser                    | Laser that uses a carbon dioxide gas as a laser medium                                                                                                                                                                                                    |
| CW Continuous wave            | Continuously radiated laser output                                                                                                                                                                                                                        |
| <D>                           |                                                                                                                                                                                                                                                           |
| Discharge excitation          | Realization of inverted population by means of discharge                                                                                                                                                                                                  |
| <E>                           |                                                                                                                                                                                                                                                           |
| Enhanced pulse                | Greatly amplified peak output of a pulse                                                                                                                                                                                                                  |
| Excitation                    | Transition of atoms or molecules to a higher energy level by supplying them with external energy                                                                                                                                                          |
| Exposure time                 | Duration through which laser radiation is emitted                                                                                                                                                                                                         |
| <F>                           |                                                                                                                                                                                                                                                           |
| Fast axial flow laser         | Laser in which gas flows rapidly in the same direction as the laser beam                                                                                                                                                                                  |
| Feedback                      | Corrective action in which a quantity to be controlled is compared with a target value generated by feeding part of an output signal to the input through a specially created closed loop so that the quantity to be controlled matches the target value. |
| <L>                           |                                                                                                                                                                                                                                                           |
| Laser                         | Device for generating light by stimulated emission                                                                                                                                                                                                        |
| Laser controlled area         | Area in which activities are controlled or monitored for protection from hazards resulting from laser radiation                                                                                                                                           |
| Laser mirror                  | Reflecting mirror used in a laser resonator                                                                                                                                                                                                               |
| Laser safety officer          | Person having sufficient knowledge about evaluation and management of hazards of lasers and in charge of safety management of lasers                                                                                                                      |
| Laser safety standard         | Standard to protect human bodies from hazards resulting from laser beams in view of use of lasers and about laser products for sale                                                                                                                       |
| Linear Polarization           | Polarization in which a plain of polarization is at a constant angle with the axis along which the light progresses                                                                                                                                       |
| <M>                           |                                                                                                                                                                                                                                                           |
| Maintenance                   | Action taken by a user to preserve normal operation of a product, such as adjustment or other measures specified in documents created by the manufacturer for users                                                                                       |

B-70254EN/01

Name

Maximum output

Mode

MPE Maximum permissible exposure

&lt;O&gt;

Operation

Optical resonator

## &lt;P&gt;

| Parameter          | Variable that is assigned a given value for a specific purpose and indicates that purpose                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Phase              | Amount representing a positional relationship between two adjacent highest or lowest points on a wave                                                            |
| Power density      | Energy per unit area                                                                                                                                             |
| Protective housing | Laser product housing or its part designed to protect humans from exposure to a laser beam exceeding an accessible emission level or strong collateral radiation |
| Pulse duration     | Time interval between the points at which an instantaneous value on the leading and trailing edges is half the peak pulse amplitude                              |
| Pulse duty         | Ratio (%) of a duration in which a pulsating laser output is on, to its entire cycle                                                                             |
| Pulse frequency    | Repetition frequency at which pulsating laser beams are radiated from an oscillator                                                                              |
| Pulse laser        | Laser that outputs energy in the form of a single pulse or a pulse train                                                                                         |
| Pulse output       | Laser output radiated in the form of a pulse train                                                                                                               |

## &lt;R&gt;

Radian

Radiant energy

&lt;S&gt;

Safety interlock

Semiconductor laser

Sequence

Stimulated emission

## &lt;T&gt;

Meaning

Maximum radiation power or maximum radiation energy per pulse that a laser product outputs in all directions where there is a hazard of exposure in view of operational

capacity in every area at any point of time after the production of the laser product

State of a resonant system in which an electromagnetic field has a specific distribution

Maximum laser radiation level that can be radiated onto human bodies without harmful influence to them in an ordinary environment

Laser product's action covering all intended functions, not including maintenance or service.

Device in which stimulated emission of light is used for a laser and which consists of a pair of reflecting mirrors facing each other

Measurement unit of angle; 1 radian equals 360

°

/2

π

Energy emitted, transmitted, or received (measured in joules, or J)

Device combined with the protective housing of a laser product to stop its operation automatically when part of the housing is removed

Laser that uses a semiconductor as an exciting medium

A succession of steps carried out in a prescribed order

Emission of an electromagnetic wave from a material in proportion to the strength of the incident electromagnetic field

| Target    | Jig used to radiate and position a laser beam       |
|-----------|-----------------------------------------------------|
| Threshold | Physical quantity necessary to generate laser beams |

## D . GLOSSARY

B-70254EN/01                                                                                                                                                             INDEX

## INDEX

| '                                                                                                                                                                                                                                                                                                                                                                                                                                 | /G10/G13/G9/G14/G11/G38/G8/G23/G1/G22/G18 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G18                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                   | /G10/G39/G40/G41/G42/G38/G43/G43/G38/G44/G41/G45/G46 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G18     |
| /G10/G13/G10/G5/G9/G14/G9/G4/G17/G17/G10/G28/G4/G14/G13/G6/G17/G16/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G33                                                                                                                                                                                                                                                    | /G10/G39/G40/G41/G47/G43/G46/G46/G48/G41/G39/G49/G14/G17/G38/G50/G51/G40/G41/G38/G39/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G22             |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G27/G1 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G31                                                                                                                                                                                                                   | /G10/G19/G19/G13/G6/G15/G10/G20/G13/G4/G14/G9/G2/G21/G4/G13/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22                                                 |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G27/G18 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G31                                                                                                                                                                                                                  | /G10/G12/G16/G2/G9/G10/G16/G6/G15/G14/G10/G28/G6/G11/G28/G14/G24/G12/G11/G15/G16/G6/G2/G11 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G31/G1                                                                            |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G27/G22 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G31                                                                                                                                                                                                                  |                                                                                                                                                                                                                                   |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G27/G25 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G1                                                                                                                                                                                                                   | b                                                                                                                                                                                                                                 |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G27/G27 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G1                                                                                                                                                                                                                   | /G15/G10/G12/G16/G6/G2/G11/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G1/G30                  |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G27/G29 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G18                                                                                                                                                                                                                  | /G15/G52/G53/G39/G49/G41/G39/G49/G14/G40/G52/G46/G14/G4/G54/G52/G53/G51/G44/G40/G14/G19/G51/G55/G56/G14/G2/G41/G50 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G18/G31                                       |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G27/G33 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G18                                                                                                                                                                                                                  | /G15/G52/G53/G39/G49/G41/G39/G49/G14/G40/G52/G46/G14/G16/G51/G43/G57/G38/G14/G20/G50/G38/G58/G46/G43/G14/G2/G41/G50 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G18/G29                                |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G27/G31 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G22                                                                                                                                                                                                                  | /G15/G50/G46/G53/G39/G41/G39/G49/G14/G10/G49/G46/G39/G40 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G22             |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G29/G30 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G22                                                                                                                                                                                                                  | /G15/G2/G9/G19/G2/G11/G4/G11/G16/G14/G21/G4/G16/G10/G6/G13/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G1/G31                                                        |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G29/G1 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G22                                                                                                                                                                                                                   | /G15/G2/G2/G13/G6/G11/G28/G14/G7/G10/G16/G4/G5 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G18                                         |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G29/G18 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G23                                                                                                                                                                                                                  | /G15/G38/G38/G50/G41/G39/G49/G14/G7/G53/G40/G46/G43/G14/G17/G56/G46/G42/G41/G47/G41/G42/G53/G40/G41/G38/G39 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G18                      |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G29/G22 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G23 /G10/G13/G9/G14/G11/G38/G8/G23/G30/G29/G25 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G25 | c                                                                                                                                                                                                                                 |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G29/G27 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G25                                                                                                                                                                                                                  | /G21/G10/G6/G13/G26/G14/G6/G11/G17/G19/G4/G15/G16/G6/G2/G11/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G18/G25                                         |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G29/G29 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G25                                                                                                                                                                                                                  | /G21/G4/G16/G10/G6/G13/G17/G14/G2/G24/G14/G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G18/G29                                                                   |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G29/G33 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G27                                                                                                                                                                                                                  | d                                                                                                                                                                                                                                 |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G29/G31 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G27                                                                                                                                                                                                                  | /G4/G34/G16/G4/G5/G11/G10/G13/G14/G3/G6/G4/G7/G14/G2/G24/G14/G13/G10/G17/G4/G5/G14/G2/G17/G15/G6/G13/G13/G10/G16/G2/G5                                                                                                            |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G33/G30 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G27                                                                                                                                                                                                                  | /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G25 |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G33/G1 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G29                                                                                                                                                                                                                   | e                                                                                                                                                                                                                                 |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G33/G18 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G33 /G10/G13/G9/G14/G11/G38/G8/G23/G30/G33/G22 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G33 | /G24/G2/G5/G14/G17/G10/G24/G4/G14/G2/G19/G4/G5/G10/G16/G6/G2/G11 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25                                                   |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G33/G25 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G33                                                                                                                                                                                                                  | f                                                                                                                                                                                                                                 |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G33/G29 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G31                                                                                                                                                                                                                  | /G28/G53/G44/G14/G19/G41/G56/G46/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8           |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G33/G33 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G31                                                                                                                                                                                                                  | /G22/G25                                                                                                                                                                                                                          |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G33/G31 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23/G31 /G10/G13/G9/G14/G11/G38/G8/G23/G30/G31/G30 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G30 | /G28/G13/G2/G17/G17/G10/G5/G26 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G31/G33 h                   |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G31/G23 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G30                                                                                                                                                                                                                  | /G6/G11/G16/G4/G5/G11/G10/G13/G14/G17/G16/G5/G12/G15/G16/G12/G5/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G1/G27                                                          |
| /G10/G13/G9/G14/G11/G38/G8/G23/G30/G31/G31 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G30                                                                                                                                                                                                                  | k                                                                                                                                                                                                                                 |
| /G10/G13/G9/G14/G11/G38/G8/G23/G1/G30/G30 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G30                                                                                                                                                                                                                   | /G13/G10/G17/G4/G5/G14/G28/G10/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                             |
| /G10/G13/G9/G14/G11/G38/G8/G23/G1/G30/G1 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G1                                                                                                                                                                                                                     | /G22/G25                                                                                                                                                                                                                          |
| /G10/G13/G9/G14/G11/G38/G8/G23/G1/G30/G25 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G1                                                                                                                                                                                                                    | /G13/G10/G17/G4/G5/G14/G28/G10/G17/G14/G9/G6/G34/G4/G5/G14/G24/G12/G11/G15/G16/G6/G2/G11 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G31/G25                                                                       |
| /G10/G13/G9/G14/G11/G38/G8/G23/G1/G30/G27 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                                                                                                                                                                                                                            | /G13/G53/G44/G46/G43/G14/G28/G53/G44/G14/G17/G56/G46/G42/G41/G47/G41/G42/G53/G40/G41/G38/G39 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                         |
| /G25/G1                                                                                                                                                                                                                                                                                                                                                                                                                           | /G22/G25                                                                                                                                                                                                                          |

/G10/G13/G9/G14/G11/G38/G8/G23/G1/G30/G29

/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8

/G25/G18

INDEX                                                                                                                                                            B-70254EN/01

| l                                                                                                                                                                                                                                                                                                    | /G19/G2/G7/G4/G5/G35/G3/G2/G13/G16/G10/G28/G4/G14/G21/G5/G2/G19 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G33/G33                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G18/G23                                                                                                         | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G19/G6/G4/G5/G15/G6/G11/G28/G14/G15/G2/G11/G21/G6/G16/G6/G2/G11/G17                                                                                                         |
| /G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4/G14/G19/G10/G5/G16/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G1                                                                                                                          | /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27/G31 |
| /G9/G10/G11/G12/G10/G13/G14/G15/G2/G11/G16/G4/G11/G16/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G18                                                                                                                    | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G19/G2/G7/G4/G5/G14/G15/G2/G11/G16/G5/G2/G13 /G8/G8/G8/G8/G8/G8 /G29/G1 /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G19/G2/G7/G4/G5/G14/G16/G10/G20/G13/G4        |
| m                                                                                                                                                                                                                                                                                                    | /G17/G4/G16/G16/G6/G11/G28 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G33/G31                         |
| /G11/G2/G16/G4/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G1/G1                                                                             | /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G16/G32/G4/G14/G2/G17/G15/G6/G13/G13/G10/G16/G2/G5 /G8/G8/G8/G8/G8/G8 /G29/G31                                                                                              |
| o                                                                                                                                                                                                                                                                                                    | /G19/G10/G5/G10/G9/G16/G4/G5/G14/G13/G6/G17/G16 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G29                                  |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G10/G17/G17/G6/G17/G16/G14/G28/G10/G17/G14/G19/G5/G4/G17/G17/G12/G5/G4                                                                                                                                                                         | /G19/G2/G7/G4/G5/G14/G15/G2/G11/G16/G5/G2/G13/G14/G36/G18/G37 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G31/G23                                               |
| /G10/G11/G21/G14/G16/G6/G9/G4/G14/G17/G4/G16/G16/G6/G11/G28 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G29/G23                                                                                                                          | /G19/G51/G43/G46/G14/G7/G53/G40/G46/G43/G14/G17/G51/G56/G56/G50/G59/G14/G12/G39/G41/G40/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G23                         |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G15/G2/G11/G16/G2/G12/G5/G6/G11/G28 /G15/G2/G11/G21/G6/G16/G6/G2/G11/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27/G27                | q                                                                                                                                                                                                                                 |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G21/G6/G17/G15/G32/G10/G5/G28/G4/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G33/G22                                                                                                                                                   | /G5/G4/G13/G10/G16/G4/G21/G14/G9/G10/G11/G12/G10/G13/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G23                                               |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G21/G6/G17/G15/G32/G10/G5/G28/G4/G14/G16/G12/G20/G4                                                                                                                                                                                            | /G5/G46/G56/G50/G53/G42/G41/G39/G49/G14/G40/G52/G46/G14/G4/G54/G52/G53/G51/G44/G40/G14/G19/G51/G55/G56/G14/G24/G41/G50/G40/G46/G43 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G30                                      |
| /G17/G4/G13/G4/G15/G16/G6/G2/G11 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27/G25                                                                                                        | /G5/G4/G17/G19/G2/G11/G21/G6/G11/G28/G14/G16/G2/G14/G10/G13/G10/G5/G9/G14/G9/G4/G17/G17/G10/G28/G4/G17/G14/G2/G11                                                                                                                 |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G4/G21/G28/G4/G14/G9/G10/G15/G32/G6/G11/G6/G11/G28 /G15/G2/G11/G21/G6/G16/G6/G2/G11/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27/G29 | /G16/G32/G4/G14/G17/G15/G5/G4/G4/G11 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G31 r                                     |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G4/G11/G10/G20/G13/G6/G11/G28/G35/G21/G6/G17/G10/G20/G13/G6/G11/G28 /G3/G10/G5/G6/G2/G12/G17/G14/G24/G12/G11/G15/G16/G6/G2/G11/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G33         | /G17/G10/G24/G4/G16/G26/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G27         |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G28/G10/G17/G14/G15/G2/G11/G16/G5/G2/G13/G14/G36/G1/G37/G8/G8/G8/G8/G8/G8/G8 /G33/G23                                                                                                                                                          | /G17/G19/G4/G15/G6/G24/G6/G15/G10/G16/G6/G2/G11/G17 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G25/G27                                    |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G28/G10/G17/G14/G19/G5/G4/G17/G17/G12/G5/G4 /G15/G2/G11/G16/G5/G2/G13/G14/G36/G18/G37 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G31/G29   | s                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      | /G16/G5/G2/G12/G20/G13/G4/G17/G32/G2/G2/G16/G6/G11/G28/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G27                                                    |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G32/G6/G28/G32/G13/G26/G14/G5/G4/G24/G13/G4/G15/G16/G6/G3/G4                                                                                                                                                                                   | /G16/G5/G2/G12/G20/G13/G4/G17/G32/G2/G2/G16/G6/G11/G28/G14/G19/G5/G2/G15/G4/G21/G12/G5/G4 /G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G22/G29                                                                                              |
| /G9/G10/G16/G4/G5/G6/G10/G13/G14/G10/G13/G10/G5/G9/G17/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G33/G29 /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G13/G10/G17/G4/G5/G14/G9/G10/G6/G11/G16/G4/G11/G10/G11/G15/G4         | v                                                                                                                                                                                                                                 |
| /G16/G6/G9/G6/G11/G28/G14/G6/G11/G21/G6/G15/G10/G16/G6/G2/G11/G14/G24/G12/G11/G15/G16/G6/G2/G11/G17/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G29/G29                                                                                                                                                              | /G7/G10/G5/G11/G6/G11/G28/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8                        |
| /G19/G10/G5/G10/G9/G4/G16/G4/G5/G17/G14/G24/G2/G5/G14/G13/G10/G17/G4/G5                                                                                                                                                                                                                              | /G29 /G7/G10/G5/G11/G6/G11/G28/G14/G13/G10/G20/G4/G13/G17/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8/G8 /G1/G18                                      |

## Revision Record FANUC LASER-MODEL C1000 i A OPERATOR'S MANUAL (B-70254EN)

<!-- image -->

|            | Contents   |
|------------|------------|
|            | Date       |
|            | Edition    |
|            | Contents   |
| Oct., 2000 | Date       |
| 01         | Edition    |

<!-- image -->

Printed at GE Fanuc Automation S.A. , Luxembourg

October 2000