def extract_article_text_from_page(dic):
    '''
    Takes json dict as input. 
    Outputs 
    {
        'Title' : str or None,
        'Text' : str or None,
        'Error' : str or None,
        'Message' : str or None
    }
    '''
    out = {}
    try:
        text = []
        for block in dic['result']['blocks']:  # list of blocks
            if block['type'] in ['text', 'quote']:
                text.append(_clear_http(block['data']['text']))
        out['title'] = dic['result']['title']
        out['text'] = "\n".join(text)
        out['error'] = None
        out['mess'] = None
    except:
        out['title'] = None
        out['text'] = None
        out['error'] = dic['error']['code']
        out['mess'] = dic['message']
    finally:
        return out


def extract_sausages_from_page(dic):
    '''
    Takes json dict as input. 
    Outputs 
    {
        'Title' : str or None,
        'Text' : str or None,
        'Error' : str or None,
        'Message' : str or None
    }
    '''
    out = {}
    try:
        comments = dic['result']['items']
        out['texts'] = []
        out['likes'] = []
        for comment in comments:
            if comment['level'] == 0:
                text = comment['text'].lower()
                if 'сосис' in text:
                    out['texts'].append(text)
                    out['likes'].append(x['summ'])
        out['error'] = None
        out['mess'] = None

    except:
        out['texts'] = None
        out['likes'] = None
        out['error'] = dic['error']['code']
        out['mess'] = dic['message']

    finally:
        return out


def _clear_http(text: str) -> str:
    newstr = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
                     ' ', 
                     text, 
                     flags=re.MULTILINE
                     )
    return newstr.replace('[', ' ').replace(']', ' ')
    