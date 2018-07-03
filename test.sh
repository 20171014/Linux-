#!/bin/bash
for((i=3;i<=26;i++));  
    do
    echo "####################第${i}列####################"   
    average=`awk -F' ' -v i="$i" '{sum+=$i} END {print sum/NR}' train.txt` 
    echo "平均值 = $average"
    max=`awk -F' ' -v p="$i" 'BEGIN {max=0} {if ($p+0>max+0) max=$p fi} END {print max}' train.txt`
    echo "最大值 = $max"
    min=`awk -F' ' -v p="$i" 'BEGIN {min=9999} {if ($p+0<min+0) min=$p fi} END {print min}' train.txt`
    echo "最小值 = $min"
    #寻找异常值
    mid=${average%.*}
    up=$[$mid+500]
    down=$[$mid-500]
    awk -F' ' -v p="$i" '{if ($p+0>"'"$up"'"+0 || $p+0<"'"$down"'"+0) print "异常值 行",NR,"值 ",$p fi}' train.txt
    done 
python draw.py
