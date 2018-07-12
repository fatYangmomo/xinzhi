__all__ = ['id_reg', 'IdcardValidator']

from django.core.validators import RegexValidator

id_reg = '^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9X]$'


class IdcardValidator(RegexValidator):
    def __init__(self):
        super(IdcardValidator, self).__init__(id_reg, '身份证号码不正确，请填写18位身份证号码，如果结尾包含X，请使用大写字母。')
