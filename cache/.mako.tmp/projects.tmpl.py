# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1585369927.471304
_enable_loop = True
_template_filename = '/Users/hrnmy/Documents/Projects/hrmyd.github.io/plugins/projectpages/templates/mako/projects.tmpl'
_template_uri = 'projects.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('project', context._clean_inheritance_tokens(), templateuri='project_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'project')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        project = _mako_get_namespace(context, 'project')
        projects = context.get('projects', UNDEFINED)
        title = context.get('title', UNDEFINED)
        featured = context.get('featured', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        project = _mako_get_namespace(context, 'project')
        projects = context.get('projects', UNDEFINED)
        title = context.get('title', UNDEFINED)
        featured = context.get('featured', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <header class="page-header">\n        <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n    </header>\n\n')
        if featured:
            __M_writer('<div class="carousel">\n')
            for p in featured:
                __M_writer('  <input type="checkbox" class="faux-ui-facia">\n  <div class="slide" annot="')
                __M_writer(str(p.title()))
                __M_writer('">\n    <img src="')
                __M_writer(str(p.meta('previewimage')))
                __M_writer('" alt="')
                __M_writer(str(p.title()))
                __M_writer('">\n  </div>\n')
            __M_writer('</div>\n')
        __M_writer('\n<h2>All projects</h2>\n    <ul class="project-list">\n')
        for p in projects:
            __M_writer('        <li class="project project-sort-')
            __M_writer(str(p.meta('sort')))
            __M_writer('"><a href="')
            __M_writer(str(p.permalink()))
            __M_writer('">')
            __M_writer(str(p.title()))
            __M_writer('</a> ')
            __M_writer(str(project.devstatus(p.meta('devstatus'))))
            __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hrnmy/Documents/Projects/hrmyd.github.io/plugins/projectpages/templates/mako/projects.tmpl", "uri": "projects.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "40": 2, "41": 3, "51": 4, "61": 4, "62": 6, "63": 6, "64": 9, "65": 10, "66": 11, "67": 12, "68": 13, "69": 13, "70": 14, "71": 14, "72": 14, "73": 14, "74": 17, "75": 19, "76": 22, "77": 23, "78": 23, "79": 23, "80": 23, "81": 23, "82": 23, "83": 23, "84": 23, "85": 23, "86": 25, "92": 86}}
__M_END_METADATA
"""
