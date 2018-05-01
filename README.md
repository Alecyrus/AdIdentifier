# AdIdentifier
[![PyPI version](https://img.shields.io/pypi/pyversions/adidentifier.svg)](https://pypi.python.org/pypi/adidentifier)
[![PyPI](https://img.shields.io/pypi/v/adidentifier.svg)](https://pypi.python.org/pypi/adidentifier)

## Installation
Prerequisites:
* The re2 library from Google
> \# git clone https://github.com/google/re2.git & cd re2 & make & make install

* The Python development headers 
> \# apt-get install python-dev

* Cython 0.20+ (pip install cython)
> $ pip install cython

After the prerequisites are installed, install as follows (pip3 for python3):
> $ pip install https://github.com/andreasvc/pyre2/archive/master.zip

or
>$ git clone git://github.com/andreasvc/pyre2.git

>$ cd pyre2

>$ make install

then
>$ pip install adidentifier

## Usage

### Example Code
```
from adidentifier import AdIdentifier
if __name__ == "__main__":

    ad = AdIdentifier()
    adtexts1 = [
         "速贷之家-借钱不担心_2小时到账","https://www.aiqianzhan.com/html/register3_bd4.html?utm_source=bd4-pc-ss&utm_medium=bd4SEM&utm_campaign=D1-%BE%BA%C6%B7%B4%CA-YD&utm_content=%BE%BA%C6%B7%B4%CA-%C3%FB%B4%CA&utm_term=p2p%CD%F8%B4%FB"]
    for text in adtexts1:
        resu = ad.is_finance(text)
        print text,"------->>", resu
    
    adtexts2 = ["https://ss3.baidu.com/-rVXeDTa2gU2pMbgoY3K/it/u=3778907493,3669893773&fm=202&mola=new&crop=v1",
                "https://ss2.bdstatic.com/8_V1bjqh_Q23odCf/pacific/upload_25289207_1521622472509.png?x=0&y=0&h=150&w=242&vh=92.98&vw=150.00&oh=150.00&ow=242.00",
                "http://pagead2.googlesyndication.com/pagead/show_ads.js",
                "http://www.googletagservices.com/tag/js/gpt_mobile.js"]
    for text in adtexts2:
        resu = ad.is_ad(text)
        print(text, "------>>", resu)
```
### Output
```
速贷之家-借钱不担心_2小时到账 ------->> True
https://www.aiqianzhan.com/html/register3_bd4.html?utm_source=bd4-pc-ss&utm_medium=bd4SEM&utm_campaign=D1-%BE%BA%C6%B7%B4%CA-YD&utm_content=%BE%BA%C6%B7%B4%CA-%C3%FB%B4%CA&utm_term=p2p%CD%F8%B4%FB ------->> True
('https://ss3.baidu.com/-rVXeDTa2gU2pMbgoY3K/it/u=3778907493,3669893773&fm=202&mola=new&crop=v1', '------>>', True)
('https://ss2.bdstatic.com/8_V1bjqh_Q23odCf/pacific/upload_25289207_1521622472509.png?x=0&y=0&h=150&w=242&vh=92.98&vw=150.00&oh=150.00&ow=242.00', '------>>', True)
('http://pagead2.googlesyndication.com/pagead/show_ads.js', '------>>', True)
('http://www.googletagservices.com/tag/js/gpt_mobile.js', '------>>', False)
```
