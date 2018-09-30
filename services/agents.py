from repositories.agents import AgentsRepository
from services.crawl import Crawl
from services.language_processing import LanguageProcessingService


class AgentsService:

    def __init__(self):
        self.language_processing_service = LanguageProcessingService()
        self.crawl = Crawl()

    def get(self):
        agent_repository = AgentsRepository()
        agents = agent_repository.get()

        return self.__append_tfidf(self.crawl.execute(agents))

    def __append_tfidf(self, agents):
        return self.language_processing_service.tfidf(text_list=agents)
