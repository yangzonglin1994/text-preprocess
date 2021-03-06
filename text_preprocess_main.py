import extract_from_markup_texts
from sentence_segment import SentenceSegment
from data_cleaner import DataCleaner
from baidu_nlp_use import TextsSegmentation
from transform_words import WordsTransformer

# if __name__ == '__main__':
#     src_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)"
#     extract_from_markup_texts.extract_content_from_markup_texts(src_path)
#
# if __name__ == '__main__':
#     src_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_train'
#     target_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_seq'
#     SentenceSegment().process_srcpath_to_targetpath(src_path, target_path, '.seq')

# if __name__ == '__main__':
#     src_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_seq'
#     target_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_clean'
#     DataCleaner().process_srcpath_to_targetpath(src_path, target_path, '.clean')

# if __name__ == '__main__':
#     src_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_clean'
#     target_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_gbk格式'
#     extract_from_markup_texts.convert_files_encoding(src_path, target_path,
#                                                      src_encoding='utf-8', target_encoding='gbk',
#                                                      filename_suffix='.gbk')

# if __name__ == '__main__':
#     src_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_gbk格式'
#     target_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_segment'
#     TextsSegmentation().process_srcpath_to_targetpath(src_path, target_path,
#                                                       filename_suffix='.segment',
#                                                       src_encoding='gbk', target_encoding='gbk')

if __name__ == '__main__':
    src_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_tag'
    target_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_transformed'
    WordsTransformer().process_srcpath_to_targetpath(src_path, target_path,
                                                     filename_suffix='.transformed',
                                                     src_encoding='gbk', target_encoding='gbk')
