from toolbox.ML_NLP_cleanup import clean

def test_clean():
    assert clean('this is superb if this can work!22') == 'superb work'
