# スプレットシートの定義
sheet_dic = {
    'form': {
        'range': 'C:G',
        'map': {
            0: 'gender',
            1: 'salary',
            2: 'latest_job_category',
            3: 'interest',
            4: 'url',
        },
        'output_range': 'H',
        'tfidf_words_range': 'I'
    },
    'agent': {
        'range': 'A:F',
        'map': {
            0: 'name',
            1: 'url',
            2: 'gender',
            3: 'salary',
            4: 'latest_job_category',
            5: 'interest',
        },
    },
}

# 各項目ごとの配点
points_dic = {
    'gender': 1,
    'salary': 1,
    'latest_job_category': 1,
    'interest': 0.06,
}

# ニュースデータの順位配点
points_news_dic = {
    1: 1,
    2: 0.5,
    3: 0.25,
}
