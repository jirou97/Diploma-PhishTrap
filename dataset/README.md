<p align="center">
<img src="https://github.com/souliotispanagiotis/PhishTrap/blob/main/PhishTrap/static/logo6.png" alt="logo">
</p>

# *Dataset.*
This dataset was created combining 3 datasets.
- [Legitimate Dataset](https://github.com/ebubekirbbr/phishing_url_detection/tree/master/dataset), from which we used the "cc1.txt", "cc2.txt" and "cc3.txt" files.
- [Phishing Dataset](https://github.com/mitchellkrogza/Phishing.Database), from the "phishing-links-ACTIVE.txt" file on 24-03-2021. 
- [Phishing Dataset 2](http://phishtank.org/phish_search.php?valid=y&active=y&Search=Search), from where we took the first 110 results on 25-03-2021.

Then, we only kept the active URLs. The active URLs are the ones with response code found in this [list](https://github.com/mitchellkrogza/Phishing.Database#define-an-active-status) for ACTIVE HTTP Codes
 and POTENTIALLY ACTIVE HTTP Codes.
 
Then we extracted features from these URLs, checked for duplicated rows and deleted them.

The final dataset is in this folder.
