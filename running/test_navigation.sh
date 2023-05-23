PYTHON_SCRIPT="test_navigation_nlvr.py"
NUMS=("3" ) #"1" "2"
SETTING=( "navigation") #"nlvr"
# 
for setting in "${SETTING[@]}"
do
  for num in "${NUMS[@]}"
  do
    python $PYTHON_SCRIPT --prompt_type "cot" --setting $setting --num $num --model_name "text-davinci-003"  #--key "xxx"
  done
done

#
echo "All done!"
