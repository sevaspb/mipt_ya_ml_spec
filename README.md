# Установка
```
1. brew update && brew install pyenv
2. PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.6.0
3. pip install ipython
4. pip install jupyter
5. pip install matplotlib
6. pip install scipy
6. pip install pandas
```

# Запуск

```
1. pyenv local 3.6.0
2. jupyter notebook
```

## Запуск `.py` файлов из `jupyter`

```
%run /path/to/script.py
```

## Загрузка фала `.py` в `jupyter`

```
%load /path/to/script.py
```
