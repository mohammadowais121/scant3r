<h1 align="center">
  <br>
  <br>
  ScanT3r
  <br>
</h1>


<img src=.src/1.gif>
***

**Why would you use Scant3r?**

Scant3r Scans all URLs with multiple HTTP Methods also,it Tries to look for bugs with basic exploits from Headers and URL Parameters By chaining waybackurls or gau with Scant3r you will have more time to look into functions and get Easy bugs on the way
and scant3r will help you  write your own python script faster , you don't need to configure http/threads/errors/options/etc... , just by writing `main` function in your script (also you can import scant3r function for write a awesome script), you can run it in your terminal or access your script from api 😃

### All Modules

| Module         | Description                                                  |
| :------------- | :-------------                                               |
| **lorsrf**     | Bruteforcing on Hidden parameters to find SSRF vulnerability |
| **ssrf**       | simple ssrf scanner                                          |
| **paths**      | checking for custom paths                                       |
| **xss**        | inject xss payload in parameter value                        |
| **sqli**       | simple sqli scanner                                          |
| **rce**        | simple RCE scanner
| **finder**     | text Matcher in request/response                                                              |
| **xss_param** | inject xss payload in parameter name
| **ssti** | simple server side template injection scanner |
| **injheaders** | inject blind xss and custom payloads in custom headers (headers.yaml&payload.yaml)
| **reflect** | find reflected parameters 
| **secrets** | find interesting variables content (API Keys , Debug Mode , etc ..) |

### OPTIONS:
Options:
  -h | show help menu and exit
  -H | add custom header (ex:-H='Cookies: test=1')
  -s | number of seconds to hold between each HTTP(S) requests.
  -a | Start Scant3r API
  -y | Methods Allowed on your target
  -m | run scant3r module (ex: -m=example)
  -n | Silent Mode
  -l | add targets list
  -g | Generate Famouse Parameters if your url dosen't have parameters
  -p | Forward all requests to proxy
  -b | add your xsshunter host (or any xss host)
  -d | debugging mode (show requests/responses)
  -x | add your host (burpcall,etc..)
  -R | use random user agent
  -w | Number of workers (default: 50)
  -t | set connection timeout (default: 10)


### Linux ![Linux](http://icons.iconarchive.com/icons/dakirby309/simply-styled/32/OS-Linux-icon.png)

```bash
$ git clone https://github.com/knassar702/scant3r
$ cd scant3r
$ pip3 install -r requirements.txt
$ ./scant3r.py -h
```

### Links:
* [Usage](https://github.com/knassar702/scant3r/wiki/Usage)
* [Modules Usage](https://github.com/knassar702/scant3r/wiki/Modules-Usage)
* [Writing your own scant3r module](https://github.com/knassar702/scant3r/wiki/writing-your-own-scant3r-module)
* [Edite Scant3r Command line options](https://github.com/knassar702/scant3r/wiki/edite-scant3r-command-options)
* [Edite Scant3r Logo](https://github.com/knassar702/scant3r/wiki/Edite-ScanT3r-Logo)

### TIPS
* [how to find hidden SSRF Parameters by using scant3r](https://github.com/knassar702/scant3r/wiki/how-to-find-hidden-SSRF-Parameters-by-using-scant3r)
* [Find Reflected Parameters with scant3r](https://github.com/knassar702/scant3r/wiki/find-reflected-parameters-with-scant3r)
* [How to Find sensitive files by using ScanT3r](https://github.com/knassar702/scant3r/wiki/How-to-Find-sensitive-files-by-using-ScanT3r)
* [Find Blind XSS With ScanT3r](https://github.com/knassar702/scant3r/wiki/Find-Blind-XSS-with-scant3r)

### ScanT3r API
* [Usage](https://github.com/knassar702/scant3r/wiki/ScanT3r-API)
* [Write ScanT3r API Script](https://github.com/knassar702/scant3r/wiki/write-module-for-api)


## TODO-Features
* add web spider
* DOM XSS Scanner
* send/analyzing requests from .yaml file

### Media 

### Version: 0.7
* All
[![asciicast](https://asciinema.org/a/403247.svg)](https://asciinema.org/a/403247)

* XSS Scanner
[![asciicast](https://asciinema.org/a/ROYOYuR7u7Ebjc81gf9iqisfw.svg)](https://asciinema.org/a/ROYOYuR7u7Ebjc81gf9iqisfw)

* injheaders
[![asciicast](https://asciinema.org/a/400245.svg)](https://asciinema.org/a/400245)*** 

#### Version: [0.6](https://github.com/knassar702/scant3r/releases/tag/0.6)

![](.src/all.gif)

**Nokia** https://www.nokia.com/responsible-disclosure/
![](.src/nokia.gif)

**IBM** https://hackerone.com/ibm

![](.src/ibm.png)
