## Description
In this project, I fine-tuned the google MT5 transformer model to predict the possible news topic given the news' context.

## Environment
```shell
bash download.sh
```

## Testing
```shell
bash run.sh
```

## Training
```shell
python3 run_summarization.py \
--model_name_or_path google/mt5 \
--train_file path_to_train\
--validation_file path_to valid \
--do_train\
--do_eval\
--text_column "maintext" \
--summary_column "title" \
--source_prefix "summarize" \
--output_dir path_to_output

```



