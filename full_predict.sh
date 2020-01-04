#!/usr/bin/env bash

#!/usr/bin/env bash

export INPUT_FILE=input.json
export OUTPUT_DIR=dev

mkdir work_dir/${OUTPUT_DIR}

python3.7 paragraph_selection/select_paras.py \
    --input_path=${INPUT_FILE} \
    --output_path=work_dir/${OUTPUT_DIR}/selected_paras.json \
    --ckpt_path=work_dir/para_select_model.bin \
    --split=${OUTPUT_DIR}#error

python3.7 bert_ner/predict.py \
    --ckpt_path=work_dir/bert_ner.pt \
    --input_path=work_dir/${OUTPUT_DIR}/selected_paras.json \
    --output_path=work_dir/${OUTPUT_DIR}/entities.json #error

python3.7 bert_ner/predict.py \
    --use_query \
    --ckpt_path=work_dir/bert_ner.pt \
    --input_path=${INPUT_FILE} \
    --output_path=work_dir/${OUTPUT_DIR}/query_entities.json

python3.7 DFGN/text_to_tok_pack.py \
    --full_data=${INPUT_FILE} \
    --entity_path=work_dir/${OUTPUT_DIR}/entities.json \
    --para_path=work_dir/${OUTPUT_DIR}/selected_paras.json \
    --example_output=work_dir/${OUTPUT_DIR}/examples.pkl.gz \
    --feature_output=work_dir/${OUTPUT_DIR}/features.pkl.gz \

python3.7 predict.py
