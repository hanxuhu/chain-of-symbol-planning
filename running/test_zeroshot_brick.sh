
PYTHON_SCRIPT="zeroshot_davinci_brick.py"
NUMS=("3" )
SETTING=( "shuffle_both")

for setting in "${SETTING[@]}"
do
  for num in "${NUMS[@]}"
  do
    python $PYTHON_SCRIPT --prompt_type "cot" --num $num --setting $setting
  done
done


echo "All done!"
