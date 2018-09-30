import constants


class Matching:
    def execute(self, text_list, agent_list):
        for key, text in text_list.items():
            text_list[key]['point'] = self.calc_point(text, agent_list)

        return text_list

    def calc_point(self, text, agent_list):
        point_list = {}
        for agent_url, agent in agent_list.items():
            point_sum = 0
            point_sum += self.calc_news_point(text['news_rank'], agent_url)

            for content, point in constants.points_dic.items():
                if text[content] != agent[content]:
                    continue
                point_sum += point

            point_list[agent['name']] = point_sum

        return point_list

    @staticmethod
    def calc_news_point(news_rank, agent_url):
        for url in news_rank:
            rank = news_rank.index(url) + 1
            if agent_url == url:
                try:
                    return constants.points_news_dic[rank]
                except:
                    return 0

        return 0
