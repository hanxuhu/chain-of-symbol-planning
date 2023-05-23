
PYTHON_SCRIPT="test_brick.py"
NUMS=("1" "2" "3" )
SETTING=( "shuffle_both")
# 
for setting in "${SETTING[@]}"
do
  for num in "${NUMS[@]}"
  do
    python $PYTHON_SCRIPT --prompt_type "cos" --num $num --setting $setting --model_name "chatgpt" 
  done
done


echo "All done!"
