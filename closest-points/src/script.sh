#!/bin/bash

function print() {
  for FILE in ../data/*-tsp.txt
  do
    if [[ $FILE =~ (.*)\-(.*) ]]
    then
      echo -n "${BASH_REMATCH[1]}.tsp: "
      java Closest.java < $FILE
    else
      echo "Could not figure out format"
    fi  
  done
}
javac ./Closest.java
print > output.txt
diff output.txt ../data/closest-pair-out.txt > diffOutput.txt