# Data Requirements

Overall, this model aims to chart the path of training and employement of physician and non-physician anesthetists in Uganda from ~1990 to 2045. In additon, we would like to estimate the costs and effects of various interventions aimed at increasing the number of practicing anesthetists.  In order to do so, we need various pieces of data to inform the model. These can be broadly divided into training, distribution, and intervention-specific.

Here I have included a description of best-available data. Key unknown parameters are shown with a "?".

## Training

### Overview

According to Bulamba et al <cite data-cite="bulamba2018"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/bulamba2018.md">(bulamba2018)</a></cite>: 

> Prior to 1970, most anaesthesia in Uganda was provided either by the surgeons (mainly foreign expatriates) or medical assistants trained on the job to provide ether or chloroform using apparatus like the Schimmelbusch mask. Mulago paramedical school had been established in the 1960s to provide technical training to a range of medical assistants who otherwise had no formal medical background but were expected to work with expatriates in the provision of medical care. Formal training of anaesthesia providers started in 1971 when the Ministry of Health initiated a three-year training program for Anaesthetic Assistants. The pre-entry qualification in this program was an Ordinary Level (O-level) certificate and the course was followed by a mandatory year of internship at Mulago national referral hospital, Kampala. The award was a national Diploma in Anaesthesia. This program had a pioneer intake of 8 students but was terminated in 1982, after only 12 years of training.

He also notes the following significant events (other events added as data permit).

| Time period |                                                Event                                                |     Source    |
|-------------|-----------------------------------------------------------------------------------------------------|---------------|
| Before 1890 | All anesthesia traditional medicine                                                                 | bulamba2018   |
| 1890        | First documented anesthetic delivered                                                               | bulamba2018   |
| 1924        | Makarere Medical School founded                                                                     | bulamba2018   |
| 1960's      | Mulago Paramedical School founded, training medical assistants                                      | bulamba2018   |
| 1962        | Mulago Hospital founded                                                                             | bulamba2018   |
| 1970        | MakCHS Department of Anaesthesia founded                                                            | bulamba2018   |
| 1971        | Anes. assistant program begins (post O-lvl, 3y training, 8 students per year)                       | bulamba2018   |
| 1970's      | Mulago Dept Anes formed by Dr. Kityo, no training                                                   | bulamba2018   |
| 1980        | J. Wilson Carswell writes that there are no practing physician anesthetists                         | carswell1980  |
| 1983        | One-year post-MBChB Diploma in Anes (not MMed) started at Mulago, 2 annually                        | bulamba2018   |
| 1985        | Commonwealth: AO req previous RN/CO. AO training reduced to 18 months with six months of internship | bulamba2018   |
| 1985        | MMed anesthesia founded at MakCHS (req diploma and MBChB, 2/y)                                      | bulamba2018   |
| 1987        | Entry requirement for Mmed changed to just intern, not diploma year                                 | bulamba2018   |
| 1988        | Graduation of the first Ugandan trained physician anaesthetists                                     | bulamba2018   |
| 1990's      | Lacor, Gulu AO programs founded "within last 30 years"                                              | bulamba2018   |
| 1995        | Mbarara Regional referral hospital opens                                                            | bulamba2018   |
| 2000        | MMed program at MUST began, enrolling 2-3 student per year (avg 2.66 per year)                      | bulamba2018   |
| 2001        | 188 students trained as Anesthesia Assistants (1y for CO/RN), unable to practice w/o Higher Dipl    | bulamba2018   |
| 2003        | New Vision article claims 12 practicing (5 expat) MDs, 144 AA's trained, 21 MDs trained, 144 AA's   | newvision2003 |
| 2006        | Uganda Anesthesia Fellowship program founded with support from AAGBI + GPAS                         | bulamba2018   |
| 2016        | Kabale and Mbale AO training programs were started                                                  | bulamba2018   |
| 2017        | Bachelor of Science in Anaesthesia (BScA) has been started at Busitema                              | bulamba2018   |

Sources: <cite data-cite="bulamba2018"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/bulamba2018.md">(bulamba2018)</a></cite>, <cite data-cite="newvision2003"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/newvision2003.md">(newvision2003)</a></cite>, <cite data-cite="carswell1980"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/carswell1980.md">(carswell1980)</a></cite>

## AOs

### AO historical training estimates

|     Year    | AOs graduated (annually, nationwide) |     Source    |
|-------------|--------------------------------------|---------------|
| Before 2000 | ?                                    |               |
| 2000        | 16                                   | ahwo2009      |
| 2001        | 11                                   | ahwo2009      |
| 2002        | 13                                   | ahwo2009      |
| 2003        | 20                                   | ahwo2009      |
| 2004        | ?                                    |               |
| 2005        | ?                                    |               |
| 2006        | ?                                    |               |
| 2007        | ?                                    |               |
| 2008        | ?                                    |               |
| 2009        | ?                                    |               |
| 2010        | 33                                   | hrhaudit2015b |
| 2011        | 23                                   | hrhaudit2015b |
| 2012        | 18                                   | hrhaudit2015b |
| 2013        | 26                                   | hrhaudit2015b |
| 2014        | 15                                   | hrhaudit2015b |
| 2015        | 26                                   | hrhaudit2015b |
| 2016        | ?                                    |               |
| 2017        | ?                                    |               |
| 2018        | ?                                    |               |

Sources: <cite data-cite="ahwo2009"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/ahwo2009.md">(ahwo2009)</a></cite>, <cite data-cite="hrhaudit2015b"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/hrhaudit2015b.md">(hrhaudit2015b)</a></cite>

## AO current training estimates

List of programs source: <cite data-cite="mohscholar2017"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/mohscholar2017.md">(mohscholar2017)</a></cite>

|                        Program                        | Expected Output |     Source    |
|-------------------------------------------------------|-----------------|---------------|
| UAHIMS-Mulago                                         | ?               |               |
| Mbale School of Clinical Officers                     | ?               |               |
| Fort Portal School of Clinical Officers               | ?               |               |
| Lacor School of Anesthesia                            | 25              | lacoranes2018 |
| Gulu School of Clinical Officers                      | ?               |               |
| Ishaka Adventists Anaesthetic Officer Training School | ?               |               |
| Kitovu Catholic Anaesthetic Officer Training School   | ?               |               |
|=======================================================|=================|===============|
| Total                                                 | ?               |               |

Sources: <cite data-cite="lacoranes2018"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/lacoranes2018.md">(lacoranes2018)</a></cite>, <cite data-cite="bulamba2018"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/bulamba2018.md">(bulamba2018)</a></cite>


# Physician anethetists


### Physician anethetists historical training estimates

| Year | Physician anesthetists graduated (annually, nationwide) |           Source/Comments            |
|------|---------------------------------------------------------|--------------------------------------|
| 1988 | 2                                                       | bulamba2018                          |
| 1989 | ?                                                       |                                      |
| 1990 | ?                                                       |                                      |
| 1991 | ?                                                       |                                      |
| 1992 | ?                                                       |                                      |
| 1993 | ?                                                       |                                      |
| 1994 | ?                                                       |                                      |
| 1995 | ?                                                       |                                      |
| 1996 | ?                                                       |                                      |
| 1997 | ?                                                       |                                      |
| 1998 | ?                                                       |                                      |
| 1999 | ?                                                       |                                      |
| 2000 | ?                                                       | MMed program at MUST began           |
| 2001 | ?                                                       |                                      |
| 2002 | ?                                                       |                                      |
| 2003 | ?                                                       |                                      |
| 2004 | ?                                                       |                                      |
| 2005 | ?                                                       |                                      |
| 2006 | ?                                                       | 2 in training total, hewittsmith2018 |
| 2007 | ?                                                       |                                      |
| 2008 | ?                                                       |                                      |
| 2009 | ?                                                       |                                      |
| 2010 | ?                                                       |                                      |
| 2011 | ?                                                       |                                      |
| 2012 | ?                                                       |                                      |
| 2013 | ?                                                       |                                      |
| 2014 | 3                                                       |                                      |
| 2015 | 3                                                       | hewittsmith2018                      |
| 2016 | 3                                                       | hewittsmith2018                      |
| 2017 | 13                                                      | hewittsmith2018                      |

Sources: <cite data-cite="hewittsmith2018"><a href="https://github.com/alexgoodell/uganda-model/blob/master/refs/cite-md/hewittsmith2018.md">(hewittsmith2018)</a></cite>










# Major data sources

Bulamba gives the following figures for currently practicing anesthetists. However, the totals in his Table 2 do not match the data given. Using the data given and re-calculating the totals, we have:


|    Region    | Nature of institution | Ugandan physician | Foreign physician | Total | Total by region |
|--------------|-----------------------|-------------------|-------------------|-------|-----------------|
| Northern     | PNFP hospital         |                 2 |                 1 |     3 |                 |
|              | Public University     |                 1 |                   |     1 |               4 |
| Eastern      | PNFP hospital         |                 1 |                   |     1 |                 |
|              | Public hospital       |                 1 |                 1 |     2 |               3 |
| Southwestern | Public university     |                 5 |                   |     5 |                 |
|              | Public hospital       |                 2 |                   |     2 |               7 |
| Central      | Several and mixed     |                61 |                 1 |    62 |              62 |
|==============|=======================|===================|===================|=======|=================|
| Total        |                       |                73 |                 3 |    76 |              76 |




## Data flow within model 

The following diagram describes the flow of data currently used in the model as of Apr 5, 2018 3:15 PM. 

![data structure](misc/data-flow.svg)

[Edit this diagram](https://mermaidjs.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbmRzW2Rpc3RyaWN0c10gLS0-IGZjXG5iZ1tCdWRnZXQgb2ZmaWNlIGRpc3RyaWN0IGRhdGEsIG90aW1zXzIwMThdIC0tPiBkc1xudW1bVU1EUEMgcmVnaXN0cnksIHVtZHBjMjAxOF0gLS0-IG1kW2FkZl0gXG5tZCAtLT4gIG1kYWRmW21kYV9kZl1cbm5wYSAtLT4gbnBhZGZbbnBhX2RmXVxuZm1bRmFjaWxpdHkgbWFzdGVyIGxpc3QsIG1vaGRoaTIwMTddIC0tPiBmY1tmYWNpbGl0aWVzXVxuZmMgLS0gam9pbiBieSBmYWNpbGl0eSAtLT4gbWRcbmRzIC0tIGpvaW4gdG8gZGlzdHJpY3QgLS0-IG5wYVthZGZdXG5hZFtBSFBDIHJlZ2lzdHJ5LCBhaHBjMjAxOF0gLS0-IG5wYVthZGZdXG5tZGFkZlttZGFfZGZdIC0tPiBmaW5hbFthZGZdXG5ucGFkZltucGFfZGZdIC0tPiBmaW5hbFxuZmluYWwgLS0-IHZmaW5hbFthZGZdXG52ZmluYWwgLS0-IHZhcnNcbnZhcnNbTWlzYyB2YXJzXSAtLT4gbW9kZWxbUnVuIG1vZGVsXVxuaHJoaXNbSFJJUywgaHJoaXMyMDE3XSAgLS0-IHZhY1tWYWNhbmNpZXMgZGYsIHVzZWQgYnkgdmFyIG5iXVxuZHMgLS0gam9pbiB0byBkaXN0cmljdCAtLT4gdmFjXG5zdWJncmFwaCBTb3VyY2VzXG4gICAgYWRcbiAgICBmbVxuICAgIHVtXG4gICAgYmdcbiAgICBocmhpc1xuZW5kXG5zdWJncmFwaCBGYWNpbGl0aWVzIG5vdGVib29rXG4gICAgZHNcbiAgICBmY1xuICAgdmFjXG5lbmRcbnN1YmdyYXBoIFBoeXNpY2lhbiBuYlxuICAgIG1kXG5lbmRcbnN1YmdyYXBoIE5QQSBuYlxuICAgIG5wYVxuZW5kXG5zdWJncmFwaCBXb3JrZm9yY2UgbmJcbiAgICBucGFkZlxuICAgIG1kYWRmXG4gICAgZmluYWxcbmVuZFxuc3ViZ3JhcGggVmFyaWFibGVzIG5iLCBwcm9jZXNzaW5nXG4gIHZmaW5hbFxuICB2YXJzXG5lbmRcbnN1YmdyYXBoIE1vZGVsIG5iXG4gIG1vZGVsXG5lbmQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ)

