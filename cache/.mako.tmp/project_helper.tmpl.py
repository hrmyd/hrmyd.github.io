# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1593107540.256634
_enable_loop = True
_template_filename = '/Users/hrnmy/Documents/Projects/hrmyd.github.io/plugins/projectpages/templates/mako/project_helper.tmpl'
_template_uri = 'project_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['devstatus']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_devstatus(context,desc):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        __M_writer = context.writer()
        __M_writer('\n')
        if desc == '1':
            __M_writer('        <span class="badge badge-default">Planning</span>\n')
        elif desc == '2':
            __M_writer('        <span class="badge badge-danger">Pre-Alpha</span>\n')
        elif desc == '3':
            __M_writer('        <span class="badge badge-warning">Alpha</span>\n')
        elif desc == '4':
            __M_writer('        <span class="badge badge-info">Beta</span>\n')
        elif desc == '5':
            __M_writer('        <span class="badge badge-success">Production/Stable</span>\n')
        elif desc == '6':
            __M_writer('        <span class="badge badge-success">Mature</span>\n')
        elif desc == '7':
            __M_writer('        <span class="badge badge-danger">Inactive</span>\n')
        else:
            __M_writer('        <span class="badge badge-default">')
            __M_writer(str(desc))
            __M_writer('</span>\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hrnmy/Documents/Projects/hrmyd.github.io/plugins/projectpages/templates/mako/project_helper.tmpl", "uri": "project_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 21, "28": 3, "33": 3, "34": 4, "35": 5, "36": 6, "37": 7, "38": 8, "39": 9, "40": 10, "41": 11, "42": 12, "43": 13, "44": 14, "45": 15, "46": 16, "47": 17, "48": 18, "49": 19, "50": 19, "51": 19, "58": 51}}
__M_END_METADATA
"""
