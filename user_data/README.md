# Useful commands

```sh
source .venv/bin/activate
freqtrade download-data

# install and start ui
freqtrade install-ui
freqtrade trade
```

## Useful information

- Future pair names are different than spot.

## Print site

[print site](https://timvink.github.io/mkdocs-print-site-plugin/print_page.html)

```sh
# install
pip3 install mkdocs-print-site-plugin
# add print-site to plugins in mkdocs.yml
  - print-site:
      add_to_navigation: false
      print_page_title: ''
      add_print_site_banner: false
      # Table of contents
      add_table_of_contents: true
      toc_title: 'Table of Contents'
      toc_depth: 6
      # Content-related
      add_full_urls: false
      enumerate_headings: true
      enumerate_figures: true
      add_cover_page: true
      cover_page_template: ''
      path_to_pdf: ''
      include_css: true
      enabled: true
# run
mkdocs serve
# go to http://127.0.0.1:8000/en/print_page/
# save as pdf
# update your GPT
```

## [Freqtrade GPT](https://chatgpt.com/g/g-JfyoeJta0-freqtrade-advisor)

## Run backtesting

```sh
freqtrade backtesting --config user_data/config.json --strategy TrendFollowingStrategy
```

## Misc commands

```sh
freqtrade download-data --exchange binance --timeframe 1m --pairs "DOGE/USDT:USDT" "XRP/USDT:USDT" "BTC/USDT:USDT" "ETH/USDT:USDT" --timerange 20240101-20250101
```

## Start juptyer notebook

```sh
docker compose -f docker/docker-compose-jupyter.yml up
```

## FreqAI

```sh

# train modal
freqtrade backtesting --config user_data/configs/config_freqai.json --freqaimodel XGBoostRegressor --strategy FreqaiExampleStrategy --timerange 20240601-20240701

# plot data
freqtrade plot-dataframe  --config user_data/configs/config_freqai.json --freqaimodel XGBoostRegressor --strategy FreqaiExampleStrategy --timerange 20240615-20240701

# view modal in tensor dashboard
tensorboard --logdir user_data/models/unique-1

# list models
freqtrade list-freqaimodels

# RL 
freqtrade backtesting --freqaimodel ReinforcementLearner --strategy freqai_rl_test_strat  --config user_data/configs/config_freqai_rl.json --timerange 20240601-20240701 --logfile --cache none --export signals

freqtrade backtesting --freqaimodel ReinforcementLearner_multiproc --strategy freqai_rl_test_strat  --config user_data/configs/config_freqai_rl.json --timerange 20240601-20240701

freqtrade backtesting-analysis --freqaimodel ReinforcementLearner --strategy freqai_rl_test_strat  --config user_data/configs/config_freqai_rl.json --timerange 20240601-2024070 --analysis-groups 0 1 2 3 4 5

rm -rf user_data/models/* 
rm -rf user_data/backtest_results/*
rm -rf user_data/plotting/*
rm -rf user_data/analysis/*
```

## Tools

```sh
# UML diagram
brew install graphviz
pip install pylint
cd freqtrade
pyreverse -o pdf -p Freqtrade .
```