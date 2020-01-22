from wagtail.core import hooks

@hooks.register('register_rich_text_features')
def register_h1_feature(features):
    features.default_features.insert(0, 'h1')
