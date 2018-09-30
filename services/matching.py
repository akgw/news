from constants import constants
from services.agents import AgentsService
from services.job_seekers import JobSeekersService


class Matching:

    def execute(self):
        agents_service = AgentsService()
        agent_list = agents_service.get()

        job_seekers_service = JobSeekersService(agent_list)
        job_seekers_list = job_seekers_service.get()

        for key, text in job_seekers_list.items():
            job_seekers_list[key]['point'] = self.calc_point(text, agent_list)

        job_seekers_service.update(job_seekers_list)

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
