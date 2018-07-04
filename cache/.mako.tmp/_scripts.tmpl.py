# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1530670625.614889
_enable_loop = True
_template_filename = 'themes/yesplease/templates/_scripts.tmpl'
_template_uri = '_scripts.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        if use_bundles:
            __M_writer('  <script src="/assets/js/bundle.js"></script>\n')
        else:
            __M_writer('  <script src="/assets/js/jquery-2.1.4.min.js"></script>\n  <script src="/assets/js/jquery.ba-throttle-debounce.min.js"></script>\n  <script src="/assets/js/moment.js"></script>\n  <script defer src="/assets/js/sidebar.js"></script>\n  <script defer src="/assets/js/jquery.fluidbox.min.js"></script>\n  <script defer src="/assets/js/highlight.pack.js"></script>\n\n')
            __M_writer('  <script defer src="/assets/js/init.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/_scripts.tmpl", "source_encoding": "ascii", "uri": "_scripts.tmpl", "line_map": {"16": 0, "32": 26, "22": 1, "23": 2, "24": 3, "25": 4, "26": 12}}
__M_END_METADATA
"""
