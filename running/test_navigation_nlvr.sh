#!/bin/bash
PYTHON_SCRIPT="test_navigation_nlvr.py"
NUMS=("3" )
SETTING=( "navigation") #"nlvr"
# 
for setting in "${SETTING[@]}"
do
  for num in "${NUMS[@]}"
  do
    python $PYTHON_SCRIPT --prompt_type "cot" --setting $setting --num $num --model_name "text-davinci-003" --key ${api_key}
  done
done

#
echo "All done!"
