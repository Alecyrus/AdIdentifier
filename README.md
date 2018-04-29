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

ad = AdIdentifier()

adtexts1 = ["58同城",
     "托福考试",
     "奢侈品",
     "58贷",
     "宜人贷",
     "人人贷",
     "平安普惠，信任信用贷款。有车或有房最高可信用贷款30万，0.5小时到账申请简便:0抵押0担保，创新刷脸申请，随借随还!",
      "借了吗，一款纯手机贷款申请app，有身份证就能贷，轻松可达10万元；具有申请快、额度高、分期还款等优点；超快速现金放款，快至1小时到账；",
     "手机app贷款-玖富万卡，注册领5千-15万信用额度",
      "凭身份证，2小时下现金8000元！ 【产品特色】 1、闪电借款：极速小额借款，线上全自动化信审，快至2小时到账。 2、额度灵活：小额轻松借，大额高至5万！ 3、门槛超低：无抵押无担保，有身份证就能借。 4、操作便捷：借款进度实时查询，到期分期还款提醒，借还方便。 5、自主提额：额度跟随信用状况变更，实时提额，快至30分钟出结果。",
      "速贷之家--专业贷款平台，30秒极速申请，无需填写表格，随贷随到!!"]
 for text in adtexts1:
     resu = ad.is_finance(text)
    print text,"------->>", resu
    
 adtexts2 = ["https://ss3.bsaidu.com/-rVXeDTa2gU2pMbgoY3K/it/u=3778907493,3669893773&fm=202&mola=new&crop=v1",
             "http://pagead2.googlesyndication.com/pagead/show_ads.js",
             "http://www.googletagservices.com/tag/js/gpt_mobile.js"]
for text in adtexts2:
    resu = ad.is_ad(text)
    print(text, "------>>", resu)
```
### Output
```
Building prefix dict from the default dictionary ...
Loading model from cache /var/folders/cr/z2n_pkzd26jgfyx0366pcsj80000gn/T/jieba.cache
Loading model cost 0.511 seconds.
Prefix dict has been built succesfully.
***.*
optimization finished, #iter = 11
Objective value = -201.335591
nSV = 1990
58同城 ------->> False
托福考试 ------->> False
奢侈品 ------->> False
58贷 ------->> True
宜人贷 ------->> True
人人贷 ------->> True
平安普惠，信任信用贷款。有车或有房最高可信用贷款30万，0.5小时到账申请简便:0抵押0担保，创新刷脸申请，随借随还! ------->> True
借了吗，一款纯手机贷款申请app，有身份证就能贷，轻松可达10万元；具有申请快、额度高、分期还款等优点；超快速现金放款，快至1小时到账； ------->> True
手机app贷款-玖富万卡，注册领5千-15万信用额度 ------->> True
凭身份证，2小时下现金8000元！ 【产品特色】 1、闪电借款：极速小额借款，线上全自动化信审，快至2小时到账。 2、额度灵活：小额轻松借，大额高至5万！ 3、门槛超低：无抵押无担保，有身份证就能借。 4、操作便捷：借款进度实时查询，到期分期还款提醒，借还方便。 5、自主提额：额度跟随信用状况变更，实时提额，快至30分钟出结果。 ------->> True
速贷之家--专业贷款平台，30秒极速申请，无需填写表格，随贷随到!! ------->> True
('https://ss3.bsaidu.com/-rVXeDTa2gU2pMbgoY3K/it/u=3778907493,3669893773&fm=202&mola=new&crop=v1', '------>>', False)
('http://pagead2.googlesyndication.com/pagead/show_ads.js', '------>>', False)
('http://www.googletagservices.com/tag/js/gpt_mobile.js', '------>>', False)
```
