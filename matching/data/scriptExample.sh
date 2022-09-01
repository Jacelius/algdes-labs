#!/bin/sh
for FILE in *-in.txt

do
	echo $FILE
	base=${FILE%-in.txt}
    java -cp '..'GS $FILE > $base.fast.out.txt # replace with your command!
    diff $base.fast.out.txt $base-out.txt
done
