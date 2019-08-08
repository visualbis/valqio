comment = {
    'author': {
        'type': 'string',
        'required': True,
    },
    'comment': {
        'type': 'string',
        'required': True,
    },
    'time': {
        'type': 'string',
        'required': True,
    },
    'id': {
        'type': 'string',
        'required': True,
    }
}
initiative = {
    'id': {
        'type': 'number',
        'required': True,
    },
    'name': {
        'type': 'string',
        'required': True,
    },
    'title': {
        'type': 'string',
        'required': True,
    },
    'descr': {
        'type': 'string',
        'required': True,
    },
    'defaultDescr': {
        'type': 'string',
        'required': True,
    },
    'compare': {
        'type': 'boolean',
        'required': True,
    },
    'simVar': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'name': {'type': 'string'},
                'value': {'type': 'string'},
                'sMeth': {'type': 'string'},
                'manSim': {'type': 'list'}
            }
        }
    },
    'simActions': {
        'type': 'dict'
    },
    'author': {
        'type': 'string',
        'required': True,
    },
    'isInitiative': {
        'type': 'boolean',
        'required': True
    },
    'relatedScenario': {
        'type': 'string',
        'required': True
    },
    'enabled': {
        'type': 'boolean',
        'required': True
    },
    'comments': {
        'type': 'dict'
    }

}

scenario = {
    'name': {
        'type': 'string',
        'required': True,
    },
    'title': {
        'type': 'string',
        'required': True,
    },
    'descr': {
        'type': 'string',
        'required': True,
    },
    'defaultDescr': {
        'type': 'string',
        'required': True,
    },
    'compare': {
        'type': 'boolean',
        'required': True,
    },
    'simVar': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'name': {'type': 'string'},
                'value': {'type': 'string'},
                'sMeth': {'type': 'string'},
                'manSim': {'type': 'list'}
            }
        }
    },
    'simActions': {
        'type': 'dict'
    },
    'author': {
        'type': 'string',
        'required': True,
    },
    'initiatives': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': initiative
        }
    },
    'activeInitiative': {
        'type': 'string',
        'required': True
    },
    'collapsed': {
        'type': 'boolean'
    }
}


schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'document': {
        'type': 'string',
        'required': True,
    },
    'application': {
        'type': 'string',
        'required': True,
    },
    'author': {
        'type': 'string',
        'required': True,
    },
    'name': {
        'type': 'string',
        'required': True,
    },
    'description': {
        'type': 'string',
        'required': True,
    },
    'scenarios': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': scenario
        }
    },
    'activeScenario': {
        'type': 'string',
        'required': True,
    },
    'comments': {
        'type': 'dict'
    }
}


scenarios = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'scenario',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': '_id'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}
