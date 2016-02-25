from pipeline.storage import PipelineCachedStorage, GZIPMixin

class GZIPPipelineStorage(GZIPMixin, PipelineCachedStorage):
    pass
