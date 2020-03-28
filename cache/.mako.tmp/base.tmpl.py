# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1585369997.840318
_enable_loop = True
_template_filename = 'themes/maupassant/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sourcelink', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n<div class="body_container">\n    <div id="header">\n        <div class="site-name">\n')
        if logo_url:
            __M_writer('            <a id="logo" href="')
            __M_writer(str(blog_url))
            __M_writer('"><img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('"></a>\n')
        else:
            __M_writer('                <h1>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</h1>\n')
        __M_writer('        </div>\n\n        <div id="nav-menu">\n            <div class="bitcron_nav_container">\n                <div class="bitcron_nav">\n                    <div class="site_nav_wrap">\n                        <ul class="site_nav sm sm-base">\n                            ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\n                            ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n                        </ul>\n                        <div class="clear clear_nav_inline_end"></div>\n                    </div>\n                </div>\n                <div class="clear clear_nav_end"></div>\n            </div>\n        </div>\n    </div>\n    <div id="layout">\n        <div class="pure-g">\n            <div class=" pure-u-24-24 pure-u-sm-24-24 pure-u-md-18-24 pure_cell">\n                <div class="content_container">\n                    <!--Body content-->\n                    <div class="row">\n                        ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n                </div>\n                <!--End of body content-->\n                <div style="clear:both;height:0;"></div>\n            </div>\n        </div>\n\n        <!-- Sidebar -->\n\n        <div class=" pure-u-6-24 pure_cell">\n            <div id="sidebar">\n                <div class="widget">\n                    <div id="search_bar">\n')
        if search_form:
            __M_writer('                        ')
            __M_writer(str(search_form))
            __M_writer('\n')
        __M_writer('                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n    <div id="footer">\n        ')
        __M_writer(str(content_footer))
        __M_writer('\n        ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n    </div>\n\n    <!--FIXME: put these somewhere                            -->\n    <!--%if len(translations) > 1:-->\n    <!--<li>')
        __M_writer(str(base.html_translations()))
        __M_writer('</li>-->\n    <!--%endif-->\n    <!--% if show_sourcelink:-->\n    <!--')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('-->\n    <!--%endif-->\n    <link href="/assets/css/duoshuo.css" type="text/css" rel="stylesheet"/>\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    <script>$(\'a.image-reference:not(.islink) img:not(.islink)\').parent().colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    <!-- fancy dates -->\n    <script>\n    moment.locale("')
        __M_writer(str(momentjs_locales[lang]))
        __M_writer('");\n    fancydates(')
        __M_writer(str(date_fanciness))
        __M_writer(', ')
        __M_writer(str(js_date_format))
        __M_writer(');\n    </script>\n    <!-- end fancy dates -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/maupassant/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "54": 2, "55": 3, "56": 3, "57": 4, "58": 4, "63": 7, "64": 8, "65": 8, "66": 14, "67": 15, "68": 15, "69": 15, "70": 15, "71": 15, "72": 15, "73": 15, "74": 16, "75": 17, "76": 17, "77": 17, "78": 19, "79": 26, "80": 26, "81": 27, "82": 27, "83": 42, "84": 42, "89": 43, "90": 56, "91": 57, "92": 57, "93": 57, "94": 59, "95": 65, "96": 65, "97": 66, "98": 66, "99": 71, "100": 71, "105": 74, "106": 77, "107": 77, "108": 81, "109": 81, "110": 82, "111": 82, "112": 82, "113": 82, "118": 85, "119": 86, "120": 86, "121": 87, "122": 87, "128": 5, "136": 5, "142": 43, "155": 74, "168": 85, "181": 168}}
__M_END_METADATA
"""
