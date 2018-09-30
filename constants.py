sheet_dic = {
    'form': {
        'range': 'C:I',
        'map': {
            0: 'url',
            1: 'gender',
            2: 'age',
            3: 'latest_industry',
            4: 'latest_job_category',
            5: 'salary',
            6: 'interest',
        },
        'output_range': 'K'
    },
    'agent': {
        'range': 'A:H',
        'map': {
            0: 'name',
            1: 'url',
            2: 'gender',
            3: 'age',
            4: 'latest_industry',
            5: 'latest_job_category',
            6: 'salary',
            7: 'interest',
        },
    },
}

points_dic = {
    'gender': 1,
    'age': 1,
    'latest_industry': 1,
    'latest_job_category': 1,
    'salary': 1,
    'interest': 0.06,
}

points_news_dic = {
    1: 1,
    2: 0.5,
    3: 0.25,
}
