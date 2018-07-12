#! python3
"""
简单的获取列表
新增对象
获取对象详细信息
更新对象
删除对象
"""
__all__ = ['old_generate_dict_from_object', 'old_generate_list_dict', 'generate_list_dict', 'generate_dict_from_dict', 'generate_dict_from_object','generate_contains_search_dict','generate_equal_search_dict','generate_create_params_dict','generate_update_params_dict','generate_date_filter']

from datetime import timedelta

##################################################
## 旧的
#################################################


def old_generate_list_dict(query_set, attr_list):
    """
    获取列表
    :param query_set:
    :param attr_list:
    :return:
    """
    count = query_set.count()
    if count == 0:
        return count, None
    response = [old_generate_dict_from_object(c, attr_list) for c in query_set]
    return count, response


def old_generate_dict_from_object(obj, attr_list):
    """
    根据 attr_list 生成dict
    :param obj:
    :param attr_list:
    是一个列表，每一项是一个 tuple，tuple第一项是属性名，第二项为别名，没有别名则放None
    :return:
    """
    my_dict = {}
    for attr, alias in attr_list:
        if '.' in attr:
            cur_obj = obj
            attrs = str.split(attr, '.')
            for a in attrs:
                cur_obj = getattr(cur_obj, a)
            my_dict[alias if alias else attr] = cur_obj
        else:
            my_dict[alias if alias else attr] = getattr(obj, attr)
    return my_dict


##################################################
## 新的
###################################################


def generate_list_dict(attr_list, query_set):
    """
    获取列表
    :param query_set:
    :param attr_list:
    :return:
    """
    count = len(query_set)
    if count == 0:
        return []
    response = [generate_dict_from_object(attr_list, c) for c in query_set]
    return response


def generate_dict_from_object(attr_list, obj):
    """
    根据 attr_list 从对象obj中获取属性，然后生成dict
    :param obj:
    :param attr_list:
    是一个tuple，每一项是tuple或str，
    tuple第一项是属性名，第二项为别名
    str的话直接就是属性名
    如果是关系数据，直接在属性中使用点号，最后生成的属性名是将点号替换为下划线
    :return:
    """
    my_dict = {}

    for item in attr_list:
        if type(item) is tuple:
            # 如果有别名
            attr, alias = item
            if alias is None:
                raise Exception('别名不能为空')
            my_dict[alias] = get_value(obj, attr)
        elif type(item) is str:
            # 没有别名
            my_dict[item.replace('.', '_').replace('()', '')] = get_value(obj, item)
        else:
            raise Exception('attr_list中的项只能是字符串或者是tuple')
    return my_dict


def generate_dict_from_dict(attr_list, force=True, **kwargs):
    my_dict = {}
    for item in attr_list:
        if type(item) is tuple:
            # 如果有别名
            attr, alias = item
            if alias is None:
                raise Exception('别名不能为空')
            try:
                my_dict[alias] = kwargs[attr]
            except KeyError:
                if force:
                    raise Exception('没有属性' + attr)
        elif type(item) is str:
            # 没有别名
            try:
                my_dict[item] = kwargs[item]
            except KeyError:
                if force:
                    raise Exception('没有属性' + item)
        else:
            raise Exception('attr_list中的项只能是字符串或者是tuple')
    return my_dict


def get_value(obj, attr_or_method):
    my_eval = 'obj.' + attr_or_method
    return eval(my_eval)


##########################################################
# 尽快淘汰掉
##########################################################
def generate_create_params_dict(param_list, **kwargs):
    """
    生成create参数的 dict
    :param param_list:
    :param kwargs:
    :return:
    """
    create_param = {}
    for p in param_list:
        create_param[p] = kwargs[p]
    return create_param


def generate_update_params_dict(param_list, **kwargs):
    """
    生成更新参数的 dict
    :param param_list:
    :param kwargs:
    :return:
    """
    update_param = {}
    for p in param_list:
        if p in kwargs:
            update_param[p] = kwargs[p]
    return update_param


def generate_contains_search_dict(param_list, **kwargs):
    """
    生成 字符匹配包含 的搜索dict
    :param param_list:
    :param search_param:
    :param kwargs:
    :return:
    """
    search_param = {}
    for p in param_list:
        if p in kwargs:
            search_param[p + '__contains'] = kwargs[p]
    return search_param


def generate_equal_search_dict(param_list, **kwargs):
    """
    生成 值判等 的搜索dict
    :param param_list:
    :param search_param:
    :param kwargs:
    :return:
    """
    search_param = {}
    for p in param_list:
        if p in kwargs:
            search_param[p] = kwargs[p]
    return search_param


def generate_date_filter(date_param_name, date_start=None, date_end=None):
    """
    生成时间筛选
    """
    search_param = dict()
    if date_start is not None:
        search_param[date_param_name + '__gte'] = date_start
    if date_end is not None:
        search_param[date_param_name + '__lt'] = date_end + timedelta(days=1)
    return search_param
