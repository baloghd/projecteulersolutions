#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from eulerutil.prime import *

bound = 2_000_000
s = 2

#for i in range(3, bound + 1, 2):
    #if is_prime(i):
        #s += i

print(s)
Pollards_rho(100_000)
