# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1585369676.1452968
_enable_loop = True
_template_filename = '/Users/hrnmy/Documents/Projects/hrmyd.github.io/plugins/projectpages/templates/mako/project.tmpl'
_template_uri = 'project.tmpl'
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
    return runtime._inherit_from(context, 'story.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        project = _mako_get_namespace(context, 'project')
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        project_index = context.get('project_index', UNDEFINED)
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
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context)
        title = context.get('title', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        project_index = context.get('project_index', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <header class="page-header">\n        <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n    </header>\n    \n    <div class="media">\n      <div class="media-body">\n\n    <div class="card project-card border-primary">\n    <div class="card-header bg-primary"><h3><i class="fa fa-info-circle"></i><span class="project-header-details">Details</span></h3></div>\n\n    <table class="table table-hover">\n    <tr>\n    <td><b>Description</b></td>\n    <td>')
        __M_writer(str(post.meta('description')))
        __M_writer('</td>\n    </tr>\n    \n    <tr>\n    <td><b>Status</b></td>\n    <td>')
        __M_writer(str(project.devstatus(post.meta('devstatus'))))
        __M_writer('</td>\n    </tr>\n\n')
        if post.meta('language'):
            __M_writer('    <tr>\n    <th>Language</th>\n    <td>')
            __M_writer(str(post.meta('language')))
            __M_writer('</td>\n    </tr>\n')
        __M_writer('\n')
        if post.meta('license'):
            __M_writer('    <tr>\n    <th>License</th>\n    <td>')
            __M_writer(str(post.meta('license')))
            __M_writer('</td>\n    </tr>\n')
        __M_writer('\n')
        if post.meta('role'):
            __M_writer('    <tr>\n    <th>Role</th>\n    <td>')
            __M_writer(str(post.meta('role')))
            __M_writer('</td>\n    </tr>\n')
        __M_writer('\n    </table>\n')
        if post.meta('link') or post.meta('download') or post.meta('github') or post.meta('bitbucket') or post.meta('bugtracker'):
            __M_writer('    <div class="card-footer">\n')
            if post.meta('link'):
                __M_writer('    <a href="')
                __M_writer(str(post.meta('link')))
                __M_writer('" class="btn btn-lg btn-primary"><i class="fa fa-link"></i> Website</a>\n')
            if post.meta('download') and not post.meta('link'):
                __M_writer('    <a href="')
                __M_writer(str(post.meta('download')))
                __M_writer('" class="btn btn-lg btn-primary"><i class="fa fa-download"></i> Download</a>\n')
            elif post.meta('download'):
                __M_writer('    <a href="')
                __M_writer(str(post.meta('download')))
                __M_writer('" class="btn btn-lg btn-success"><i class="fa fa-download"></i> Download</a>\n')
            if post.meta('github'):
                __M_writer('    <a href="')
                __M_writer(str(post.meta('github')))
                __M_writer('" class="btn btn-lg btn-info"><i class="fab fa-github"></i> GitHub</a>\n')
            if post.meta('bitbucket'):
                __M_writer('    <a href="')
                __M_writer(str(post.meta('bitbucket')))
                __M_writer('" class="btn btn-lg btn-info"><i class="fab fa-bitbucket"></i> BitBucket</a>\n')
            if post.meta('gallery'):
                __M_writer('    <a href="')
                __M_writer(str(post.meta('gallery')))
                __M_writer('" class="btn btn-lg btn-success"><i class="far fa-image"></i> Gallery</a>\n')
            if post.meta('bugtracker'):
                __M_writer('    <a href="')
                __M_writer(str(post.meta('bugtracker')))
                __M_writer('" class="btn btn-lg btn-danger"><i class="fa fa-bug"></i> Bug Tracker</a>\n')
            __M_writer('    </div>\n')
        __M_writer('    </div>\n          ')
        __M_writer(str(post.text(lang)))
        __M_writer('\n      </div>\n      <div class="float-md-right">\n        <p><a href="')
        __M_writer(str(project_index[lang]))
        __M_writer('" class="btn btn-secondary btn-header-line">← Projects</a></p>\n')
        if post.meta('logo'):        
            __M_writer('        <p><img class="media-object" src="')
            __M_writer(str(post.meta('logo')))
            __M_writer('" alt="')
            __M_writer(str(title))
            __M_writer('"></p>\n')
        __M_writer('      </div>\n    </div>\n   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/hrnmy/Documents/Projects/hrmyd.github.io/plugins/projectpages/templates/mako/project.tmpl", "uri": "project.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "41": 2, "42": 3, "52": 4, "63": 4, "64": 6, "65": 6, "66": 18, "67": 18, "68": 23, "69": 23, "70": 26, "71": 27, "72": 29, "73": 29, "74": 32, "75": 33, "76": 34, "77": 36, "78": 36, "79": 39, "80": 40, "81": 41, "82": 43, "83": 43, "84": 46, "85": 48, "86": 49, "87": 50, "88": 51, "89": 51, "90": 51, "91": 53, "92": 54, "93": 54, "94": 54, "95": 55, "96": 56, "97": 56, "98": 56, "99": 58, "100": 59, "101": 59, "102": 59, "103": 61, "104": 62, "105": 62, "106": 62, "107": 64, "108": 65, "109": 65, "110": 65, "111": 67, "112": 68, "113": 68, "114": 68, "115": 70, "116": 72, "117": 73, "118": 73, "119": 76, "120": 76, "121": 77, "122": 78, "123": 78, "124": 78, "125": 78, "126": 78, "127": 80, "133": 127}}
__M_END_METADATA
"""
