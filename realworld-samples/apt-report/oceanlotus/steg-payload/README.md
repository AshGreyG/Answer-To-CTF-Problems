# OceanLotus Steganography Malware Analysis

## 1 Introduction

This directory is to imitate **OceanLotus Steganography Malware** in Linux,
related resources are listed below:

+ Chinese Blog: [海莲花APT组织最新“隐写术”系列活动总结](https://www.secrss.com/articles/9675)
+ Github APT report collections: [APT_REPORT repo](https://github.com/blackorbird/APT_REPORT/tree/master/Oceanlotus)
+ Original Blackberry Cylance report: [original report](https://www.blackberry.com/content/dam/bbcomv4/blackberry-com/en/company/research-and-intelligence/OceanLotus-Steganography-Malware-Analysis-White-Paper.pdf)

## 2 Imitate in Linux

### 2.1 Analysis of Original Malware in Windows

One of OceanLotus malware loader attempts to imitate McAfee's McVsoCfg DLL and
expects to be side-loaded by the legitimate "On Demand Scanner" executable.
It arrives together with an encrypted payload stored in a separate.png image
file. The payload is encoded inside this image with the use of a technique 
called **steganography**, which **utilizes the least significant bits of each
pixel's color code to store hidden information**.

The encoded payload is additionally encrypted with AES128 and further obfuscated
with XOR. The XOR key is not hardcoded but instead is read from the first byte
of the `C:\Windows\system.ini` file.

The size of the payload is encoded within the **first four pixels** of the image.
After obtaining this size, the malware will allocate an appropriate memory
buffer and proceed to decode the remaining payload byte by byte.

<!-- TODO: Should learn more about AES128, and later the file will refer to
---- my notes.
---->
