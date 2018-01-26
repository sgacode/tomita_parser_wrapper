# coding=UTF-8

from tomita.parser import DocumentFact


def persons_data_provider():
    return [
        (
            'Яков Миркин (заведующий отделом международных рынков капитала Института '
            'мировой экономики и международных отношений РАН)',
            [
                DocumentFact('ЯКОВ МИРКИН', 0, 0, 11, lead_id=0)
            ]
        ),
        (
            'Просто текст без каки-либо ФИО, написанный 26.01.2018',
            []
        ),
        (
            'Джим Фултон, создатель Zope, придумал язык разметки StructuredText, напоминающий упрощённую разметку '
            'WikiWikiWeb. Проблемы StructuredText привели к созданию Дэвидом Гуджером языка разметки, '
            'названного ReStructuredText.',
            [
                DocumentFact('ДЖИМ ФУЛТОН', 0, 0, 11, lead_id=0),
                DocumentFact('ДЭВИД ГУДЖЕР', 1, 157, 16, lead_id=1)
            ]
        ),
    ]