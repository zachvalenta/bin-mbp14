#!/usr/bin/env bash

bill=$(ps -A | grep -m1 cmus | awk '{print $1}')
kill -KILL $bill
