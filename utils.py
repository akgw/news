class Utils:
    @staticmethod
    def formatted_spreadsheet_value(values, sheet_map):
        values.pop(0)
        ret_value = []

        for column_index, value in enumerate(values):
            if len(value) != len(sheet_map):
                print(str(value) + 'is not enough value')
                continue

            v = {}
            for index, key in sheet_map.items():
                v[key] = value[index]

            v['column_index'] = column_index + 2  # popしているため2から開始
            ret_value.append(v)

        return ret_value
