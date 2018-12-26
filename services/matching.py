import constants
from services.agents import AgentsService
from services.job_seekers import JobSeekersService


class Matching:

    # メインのマッチングロジック
    def execute(self):
        agents_service = AgentsService()
        agent_list = agents_service.get()

        job_seekers_service = JobSeekersService(agent_list)
        job_seekers = job_seekers_service.get()

        for key, text in job_seekers.items():
            job_seekers[key]['point'] = self.calc_point(text, agent_list)

        job_seekers_service.update(job_seekers)
        job_seekers_service.update_tfidf_words(job_seekers)

    # 配点
    def calc_point(self, text, agent_list):
        point_list = {}
        for agent_url, agent in agent_list.items():
            point_sum = 0
            if 'news_rank' in text:
                point_sum += self.calc_news_point(text['news_rank'], agent)

            for content, point in constants.points_dic.items():
                for seeker_answer in text[content].split(','):
                    for agent_answer in agent[content].split(','):
                        if seeker_answer != agent_answer:
                            continue
                        point_sum += point

            point_list[agent['name']] = round(point_sum, 4)

        return point_list

    # 順位付けされている項目の配点
    @staticmethod
    def calc_news_point(news_rank, agent):
        for agent_name in news_rank:
            rank = news_rank.index(agent_name) + 1
            if agent_name == agent['name']:
                try:
                    return constants.points_news_dic[rank]
                except:
                    return 0

        return 0
