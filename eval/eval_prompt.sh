#!/bin/bash
PYTHON_SCRIPT="eval_prompt.py"
NUMS=("1" "2" "3")
SETTING=("shuffle_both")

for setting in "${SETTING[@]}"
do
  for num in "${NUMS[@]}"
  do
    python $PYTHON_SCRIPT --prompt_type "cos" --num $num --setting $setting
  done
done

echo "All done!"
