# Sir-Alfred

![Alt text](assets/Untitled.png)


Automated Account checker for Android apps, using Python and ADB shell. 

This software is not intended for illegal purposes.

Reads from file and uses shell sendevents to access device, including ``` dumpsys ``` to obtain changes in activity.

Current version only supports 5.5 inches device, due to 'keyevents.tap' function.

Your Phone needs ``` Developer Options > Android Debugging ``` enabled in order to be connected. Some future functions may need root.

--------------------------------------------------

#### Requires Android Debug Bridge running, i.e. :

``` sudo apt-get install android-tools-adb ```

#### Requires pure-python-adb, i.e.:

``` pip3 install -U pure-python-adb ```

#### Run ADB server before starting, i.e.:

``` adb devices ```

#### Connect your phone, and check an existing text file containing account combos, i.e. :

``` cd ~/accounts ```

``` cat accounts ```

``` example@mail.com:password ```

--------------------------------------------------

#### To do:

- *Fix 429 response on some apps with tricks*
- *Fix similar 'Too many requests' responses on some apps with proxies/tricks*
- *Add more clients*
- *Add option to restart/quit after list exhaustion*
- *Add option to select user directories for read/write*
- *Add relative paths (i.e. ``` from pathlib import Path ``` )*
- *Add option to select type of combo file so that correct ``` .split() ``` method can be used (i.e. *user:pass* or *user:pass | TEST ACCOUNT BY* etc..)*