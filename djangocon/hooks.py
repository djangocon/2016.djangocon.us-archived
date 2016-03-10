import markdown

import pinax.boxes.hooks
import pinax.pages.hooks


def markup_renderer(content):
    return markdown.markdown(content)


class PinaxBoxesHookSet(pinax.boxes.hooks.DefaultHookSet):

    def parse_content(self, content):
        return markup_renderer(content)


class PinaxPagesHookSet(pinax.pages.hooks.DefaultHookSet):

    def parse_content(self, content):
        return markup_renderer(content)
