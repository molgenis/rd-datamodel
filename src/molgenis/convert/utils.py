

# @name emxAttributes:
# @description
# All valid EMX attribute names. This allows the input model to be
# parsed and validated when building the primary EMX elements:
# packages, entities, and attributes sheets. Valid dataTypes are
# also included.
emxAttributes = {
    'packages': ['name', 'label', 'description', 'parent', 'tags'],
    'entities': [
        # 'entity',  # required
        'name',  # required
        'label',
        'extends',
        'package',
        'abstract',
        'description',
        'backend',
        'tags'
    ],
    'attributes': [
        'entity',         # required attributes
        'name',           # required attributes
        'dataType',
        'refEntity',
        'nillable',
        'idAttribute',
        'auto',
        'description',
        'rangeMin',
        'rangeMax',
        'lookupAttribute',
        'label',
        'aggregateable',
        'labelAttribute',
        'readOnly',
        'tags',
        'validationExpression',
        'visible',
        'defaultValue',
        'partOfAttribute',
        'expression'
    ],
    'dataTypes': [
        'bool',
        'categorical',
        'categorical_mref',
        'compound',
        'date',
        'datetime',
        'decimal',
        'email',
        'enum',
        'file',
        'hyperlink',
        'int',
        'long',
        'mref',
        'one_to_many',
        'string',
        'text',
        'xref'
    ]
}