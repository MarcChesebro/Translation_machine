export VOCAB_SOURCE=data/toy_copy/train/vocab.sources.txt
export VOCAB_TARGET=data/toy_copy/train/vocab.targets.txt
export TRAIN_SOURCES=data/toy_copy/train/sources.txt
export TRAIN_TARGETS=data/toy_copy/train/targets.txt
export DEV_SOURCES=data/toy_copy/dev/sources.txt
export DEV_TARGETS=data/toy_copy/dev/targets.txt

export DEV_TARGETS_REF=data/toy_copy//dev/targets.txt
export TRAIN_STEPS=1000

export MODEL_DIR=./out
mkdir -p $MODEL_DIR

python -m bin.train \
  --config_paths="
      seq2seq/example_configs/nmt_small.yml,
      seq2seq/example_configs/train_seq2seq.yml,
      seq2seq/example_configs/text_metrics_bpe.yml" \
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