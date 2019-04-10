export VOCAB_SOURCE=english_vocab.txt
export VOCAB_TARGET=german_vocab.txt
export TRAIN_SOURCES=english_train.txt
export TRAIN_TARGETS=german_train.txt
export DEV_SOURCES=english_dev.txt
export DEV_TARGETS=german_dev.txt

export DEV_TARGETS_REF=german_dev.txt
export TRAIN_STEPS=300000

export MODEL_DIR=./out
mkdir -p $MODEL_DIR

python -m bin.train \
  --config_paths="
      configs/nmt_small.yml,
      configs/train_seq2seq.yml,
      configs/text_metrics_bpe.yml" \
  --model_params "
      vocab_source: $VOCAB_SOURCE
      vocab_target: $VOCAB_TARGET" \
  --input_pipeline_train "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - $TRAIN_SOURCES
      target_files:
        - $TRAIN_TARGETS" \
  --input_pipeline_dev "
    class: ParallelTextInputPipeline
    params:
       source_files:
        - $DEV_SOURCES
       target_files:
        - $DEV_TARGETS" \
  --batch_size 32 \
  --train_steps $TRAIN_STEPS \
  --output_dir $MODEL_DIR
