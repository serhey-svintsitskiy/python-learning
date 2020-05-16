l = [
    'Accessories',
    'CustomFormParamSubgroups',
    'CustomForms',
    'ExtraFields',
    'ModuleSets',
    'ProductTopGroups',
    'ReportsTemplates',
    'UserProfile',
    'CustomFormFields',
    'CustomFormSkuParams',
    'ExportFiles',
    'ImportLog',
    'OrderSkipReasons',
    'PromotionBonusProducts',
    'Routes',
    'Users',
    'CustomFormOtherParams',
    'CustomFormSubgroups',
    'ExportLog',
    'Juniors',
    'Orders',
    'PromotionProducts',
    'ShopsFilter',
    'VisitSkipReasons',
    'CustomFormParamGroups',
    'CustomFormSubgroups2Fields',
    'ExtraFieldValueList',
    'LiteAttributes',
    'OtherWorks',
    'Promotions',
    'TTWorkersRel',
]

import io

word = u'привет'
with io.open('heap.txt', encoding='utf-8') as file:
    for line in file:
        for word in l:
            if word in line:
                l.remove(word)

print(l)
