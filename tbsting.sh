#!/bin/sh

ABS_PATH=$(cd $(dirname $0) && pwd)
export  PATH=$PATH:$ABS_PATH

PYTHON=`which python2`

if [ ! -f $PYTHON ];then
    PYTHON="$ABS_PATH/tools/python2.7/bin/python2.7"
fi

# init tools

# run
$PYTHON $ABS_PATH/lib/tbsting.py $@
