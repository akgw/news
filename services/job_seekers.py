from repositories.job_seekers import JobSeekersRepository
from services.crawl import CrawlService
from services.language_processing import LanguageProcessingService


class JobSeekersService:

    def __init__(self, agent_list):
        self.language_processing_service = LanguageProcessingService()
        self.job_seekers_repository = JobSeekersRepository()
        self.crawl = CrawlService()
        self.agent_list = agent_list

    # 求職者の情報を取得
    def get(self):
        job_seekers = self.job_seekers_repository.get()

        job_seekers = self.__append_tfidf(self.crawl.execute(job_seekers))
        return self.__append_cos_similarity(job_seekers)

    def __append_tfidf(self, job_seekers):
        return self.language_processing_service.append_tfidf(text_list=job_seekers)

    def __append_cos_similarity(self, job_seekers):
        return self.language_processing_service.append_cos_similarity(text_list=job_seekers, agent_list=self.agent_list)

    # 求職者の情報を更新
    def update(self, job_seekers):
        return self.job_seekers_repository.update(job_seekers)

    # 求職者の指定したニュースのTFIDFが高い単語情報を付加
    def update_tfidf_words(self, job_seekers):
        return self.job_seekers_repository.update_tfidf_words(job_seekers)
