# pandas-heal-data

## About
Related to this Stack Overflow question:
https://stackoverflow.com/questions/72494379/repairing-data-in-a-pandas-dataframe-when-duplicate-data-exists?noredirect=1#comment128080907_72494379

This problem is really more of an inference problem but it should be simple enough to solve algorithmically.


## Pattern 1

### Problem
During data intake, it is normal for some data to be missing.  It is also common to have data duplicated across data sources.  In such scenarios it is often reasonable to assume that the programmmer/scripter/data scientist knows (or can infer from context) something about the sorce of data in each column of a dataframe and whether or not data in one column can be used to fill in a missing value in another column.  This code is an attempt to do just that, algorithmically, if both representative and dependent columns are known.

For example, suppose the following data...

**Data Source 1.1
| Row | ID | HostName | IP | SERIAL |
|---- |--- |--------- |--- |------- |
| 0 | c2f | pa-dal-32f | 172.22.60.131 | 4fc-1482 |
| 1 | 94b | pa-dtx-199 | 172.22.61.27 | 4fc-5228 |
| _2_ | _ac7_ | _pa-lax-274_ | _172.22.62.58_ |  |
| 3 | 134 | pa-dul-a21 | 172.22.63.221 | 4fc-c811 |

**Data Source 1.2
| Row | ID | HostName | PURCHASE_DATE | SERIAL |
|---- |--- |--------- |--- |------- |
| 0 | 22 | pa-dal-32f | 2021-04-17 | 4fc-1482 |
| 1 | 23 | pa-dtx-199 | 2021-04-17 | 4fc-5228 |
| 2 | 24 | pa-dul-a21 | 2022-02-10 | 4fc-c811 |
| _3_ | _25_ | _pa-lax-274_ | _2019-06-21_ | _4fc-0982_ |

From this data we can infer that the missing serial number in row 2 of Data Source 1.1 can be "healed" (populated) by the serial number of the device with the same hostname in Data Source 1.2, row 3.

In this case, the dependent column is the hostname because if the hostname of a record matches between two sets of data we know (in this environment) that we are looking at data about the same device in both tables.

### Desired Outcome

From the two data sources above, the resulting dataset should look something like this...

**Result 1
| Row | ID | HostName | IP | SERIAL | PURCHASE_DATE | DS2_ID |
|---- |--- |--------- |--- |------- |-------------- |------- |
| 0 | c2f | pa-dal-32f | 172.22.60.131 | 4fc-1482 | 2021-04-17 | 22 | 
| 1 | 94b | pa-dtx-199 | 172.22.61.27 | 4fc-5228 | 2021-04-17 | 23 |
| _2_ | _ac7_ | _pa-lax-274_ | _172.22.62.58_ | _4fc-0982_ | _2019-06-21_ | _25_ |
| 3 | 134 | pa-dul-a21 | 172.22.63.221 | 4fc-c811 | 2022-02-10 | 24 |

### Solution

One option is to iterate through each dataframe, but since we don't know which of the SERIAL columns might be missing data, this can be tedious, and if not coded well, rather slow.  Performance of such a solution might be problematic on large datasets.  It is reasonable to assume that such a situation occurs often enough that it has likely already been solved, either within Pandas or using another library.

## Pattern 2

### Problem
Another common problem is the presence of data that is inconsistent.  There is a special case of such occurances:  We want all the values.  An example follows...

**Data Source 2.1
| Row | ID | HostName | IP | SERIAL |
|---- |--- |--------- |--- |------- |
| 0 | c2f | pa-dal-32f | 172.22.60.131 | 4fc-1482 |
| 1 | 94b | pa-dtx-199 | 172.22.61.27 | 4fc-5228 |
| 2 | ac7 | pa-lax-274 | 172.22.62.58 | 4fc-0982 |
| 3 | 134 | pa-dul-a21 | 172.22.63.221 | 4fc-c811 |

**Data Source 2.2
| Row | ID | HostName | PURCHASE_DATE | SERIAL |
|---- |--- |--------- |--- |------- |
| 0 | 22 | pa-dal-32f | 2021-04-17 | 4fc-1482 |
| 1 | 23 | pa-dtx-199 | 2021-04-17 | 4fc-5228 |
| 2 | 24 | pa-dul-a21 | 2022-02-10 | 4fc-c811 |
| 3 | 25 | pa-lax-274 | 2019-06-21 | 4fc-0982 |
