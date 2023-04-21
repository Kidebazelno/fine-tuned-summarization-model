# ${1}: path to the input file
# ${2}: path to the output file


python3 run_summarization.py \
--model_name_or_path ./new_out \
--test_file ${1} \
--do_predict\
--text_column "maintext" \
--summary_column "title" \
--source_prefix "summarize" \
--predict_with_generate \
--output_dir ${2}

