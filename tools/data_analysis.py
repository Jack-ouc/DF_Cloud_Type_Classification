#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   data_analysis.py
@Desciption     :   None
@Modify Time      @Author    @Version 
------------      -------    --------  
2019/10/6 23:56   Daic       1.0        
'''
'''
===============================size：
threathod: 1.3:
too high = 2323
too wide = 1705

threathod: 1.2:
too high = 2328
too wide = 1717
'''
'''
================================k1 cate distribute
            train     val    arg_times
big mid 1
cate: 0      29        9        20
cate: 1    1458      438        1
cate: 2      11        5        40
cate: 3      68       22        10
cate: 4      73       35        10
cate: 5       4        0        0
cate: 6     115       33        10
cate: 7     238       80        6

big high 2
cate: 8       7        3        20
cate: 9    1057      377        10        
cate:10      93       27        10
cate:11       6        2        10
cate:12      51       13        16
cate:13      15        7        30
cate:14     155       46        6

big low 0
cate:15      33        7        10
cate:16     120       37        8
cate:17     747      264        1
cate:18     500      160        2
cate:19     625      215        2
cate:20     179       65        4
cate:21      68       18        10
cate:22      21        3        10
cate:23      42       12        10
cate:24    1230      382        10
cate:25      20        4        10
cate:26     408      126        2
cate:27     337      110        3
cate:28       1        0        0
'''

'''
============================label_countting:
single label : 10211
mutilabel    : 454
{'1': 38,
 '10': 1434,
 '10;18': 95,
 '10;18;18': 5,
 '10;18;20': 9,
 '10;19': 3,
 '10;20': 42,
 '10;25': 8,
 '10;27': 17,
 '11': 120,
 '11;18': 18,
 '11;20': 10,
 '12': 8,
 '13': 64,
 '14': 22,
 '15': 201,
 '15;18': 5,
 '15;20': 5,
 '16': 40,
 '17': 157,
 '18': 1011,
 '18;20': 5,
 '18;25': 8,
 '18;27': 3,
 '19': 660,
 '2': 1896,
 '20': 840,
 '20;27': 7,
 '21': 244,
 '22': 86,
 '23': 24,
 '24': 54,
 '25': 1612,
 '26': 24,
 '27': 534,
 '28': 447,
 '2;10': 54,
 '2;11': 8,
 '2;15': 3,
 '2;18': 20,
 '2;19': 3,
 '2;20': 11,
 '2;25': 6,
 '2;7': 3,
 '3': 16,
 '4': 90,
 '4;10': 3,
 '4;18': 7,
 '5': 108,
 '6': 4,
 '7': 148,
 '7;18': 15,
 '7;23': 9,
 '8': 318,
 '8;17': 21,
 '8;18': 6,
 '9': 10}
'''