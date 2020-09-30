from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import reverse

from librarys.mixin.permission import LoginRequiredMixin
from backend.models.users import Users


class IndexAPIView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        result = {'homeInfo': {'title': '首页', 'href': reverse("welcome")},
                  'logoInfo': {'title': '后台管理', 'image': '/static/backend/images/logo.png', 'href': ''},
                  'menuInfo': [
                      {'title': '常规管理', 'icon': 'fa fa-address-book', 'href': '', 'target': '_self', 'child': [
                          {'title': '主页模板', 'href': '', 'icon': 'fa fa-home', 'target': '_self', 'child': [
                              {'title': '欢迎', 'href': reverse("welcome"), 'icon': 'fa fa-tachometer',
                               'target': '_self'},
                              {'title': '用户管理', 'href': reverse('user'), 'icon': 'fa fa-tachometer',
                               'target': '_self'},
                              {'title': '主页三', 'href': 'page/welcome-3.html', 'icon': 'fa fa-tachometer',
                               'target': '_self'}]},
                          {'title': '菜单管理', 'href': reverse("menu"), 'icon': 'fa fa-window-maximize',
                           'target': '_self'},
                          {'title': '系统设置', 'href': reverse("setting"), 'icon': 'fa fa-gears', 'target': '_self'},
                          {'title': '表格示例', 'href': reverse("table"), 'icon': 'fa fa-file-text', 'target': '_self'},
                          {'title': '表单示例', 'href': '', 'icon': 'fa fa-calendar', 'target': '_self',
                           'child': [
                               {'title': '普通表单', 'href': 'page/form.html', 'icon': 'fa fa-list-alt', 'target': '_self'},
                               {'title': '分步表单', 'href': 'page/form-step.html', 'icon': 'fa fa-navicon',
                                'target': '_self'}]},
                          {'title': '登录模板', 'href': '', 'icon': 'fa fa-flag-o', 'target': '_self', 'child': [
                              {'title': '登录-1', 'href': 'page/login-1.html', 'icon': 'fa fa-stumbleupon-circle',
                               'target': '_blank'},
                              {'title': '登录-2', 'href': 'page/login-2.html', 'icon': 'fa fa-viacoin',
                               'target': '_blank'},
                              {'title': '登录-3', 'href': 'page/login-3.html', 'icon': 'fa fa-tags',
                               'target': '_blank'}]},
                          {'title': '异常页面', 'href': '', 'icon': 'fa fa-home', 'target': '_self', 'child': [
                              {'title': '404页面', 'href': 'page/404.html', 'icon': 'fa fa-hourglass-end',
                               'target': '_self'}]},
                          {'title': '其它界面', 'href': '', 'icon': 'fa fa-snowflake-o', 'target': '', 'child': [
                              {'title': '按钮示例', 'href': 'page/button.html', 'icon': 'fa fa-snowflake-o',
                               'target': '_self'},
                              {'title': '弹出层', 'href': 'page/layer.html', 'icon': 'fa fa-shield',
                               'target': '_self'}]}]},
                      {'title': '组件管理', 'icon': 'fa fa-lemon-o', 'href': '', 'target': '_self',
                       'child': [
                           {'title': '图标列表', 'href': 'page/icon.html', 'icon': 'fa fa-dot-circle-o', 'target': '_self'},
                           {'title': '图标选择', 'href': 'page/icon-picker.html', 'icon': 'fa fa-adn', 'target': '_self'},
                           {'title': '颜色选择', 'href': 'page/color-select.html', 'icon': 'fa fa-dashboard',
                            'target': '_self'},
                           {'title': '下拉选择', 'href': 'page/table-select.html', 'icon': 'fa fa-angle-double-down',
                            'target': '_self'},
                           {'title': '文件上传', 'href': 'page/upload.html', 'icon': 'fa fa-arrow-up', 'target': '_self'},
                           {'title': '富文本编辑器', 'href': 'page/editor.html', 'icon': 'fa fa-edit', 'target': '_self'},
                           {'title': '省市县区选择器', 'href': 'page/area.html', 'icon': 'fa fa-rocket', 'target': '_self'}]},
                      {'title': '其它管理', 'icon': 'fa fa-slideshare', 'href': '', 'target': '_self', 'child': [
                          {'title': '多级菜单', 'href': '', 'icon': 'fa fa-meetup', 'target': '', 'child': [
                              {'title': '按钮1', 'href': 'page/button.html?v=1', 'icon': 'fa fa-calendar',
                               'target': '_self',
                               'child': [{'title': '按钮2', 'href': 'page/button.html?v=2', 'icon': 'fa fa-snowflake-o',
                                          'target': '_self', 'child': [
                                       {'title': '按钮3', 'href': 'page/button.html?v=3', 'icon': 'fa fa-snowflake-o',
                                        'target': '_self'},
                                       {'title': '表单4', 'href': 'page/form.html?v=1', 'icon': 'fa fa-calendar',
                                        'target': '_self'}]}]}]},
                          {'title': '失效菜单', 'href': 'page/error.html', 'icon': 'fa fa-superpowers',
                           'target': '_self'}]}]}

        return JsonResponse(result)


class MenuApiView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        menu = {'code': 0, 'msg': '', 'count': 19, 'data': [
            {'authorityId': 1, 'authorityName': '系统管理', 'orderNumber': 1, 'menuUrl': None, 'menuIcon': 'layui-icon-set',
             'createTime': '2018/06/29 11:05:41', 'authority': None, 'checked': 0, 'updateTime': '2018/07/13 09:13:42',
             'isMenu': 0, 'parentId': -1},
            {'authorityId': 2, 'authorityName': '用户管理', 'orderNumber': 2, 'menuUrl': 'system/user', 'menuIcon': None,
             'createTime': '2018/06/29 11:05:41', 'authority': None, 'checked': 0, 'updateTime': '2018/07/13 09:13:42',
             'isMenu': 0, 'parentId': 1},
            {'authorityId': 3, 'authorityName': '查询用户', 'orderNumber': 3, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/07/21 13:54:16', 'authority': 'user:view', 'checked': 0,
             'updateTime': '2018/07/21 13:54:16', 'isMenu': 1, 'parentId': 2},
            {'authorityId': 4, 'authorityName': '添加用户', 'orderNumber': 4, 'menuUrl': None, 'menuIcon': None,
             'createTime': '2018/06/29 11:05:41', 'authority': 'user:add', 'checked': 0,
             'updateTime': '2018/07/13 09:13:42', 'isMenu': 1, 'parentId': 2},
            {'authorityId': 5, 'authorityName': '修改用户', 'orderNumber': 5, 'menuUrl': None, 'menuIcon': None,
             'createTime': '2018/06/29 11:05:41', 'authority': 'user:edit', 'checked': 0,
             'updateTime': '2018/07/13 09:13:42', 'isMenu': 1, 'parentId': 2},
            {'authorityId': 6, 'authorityName': '删除用户', 'orderNumber': 6, 'menuUrl': None, 'menuIcon': None,
             'createTime': '2018/06/29 11:05:41', 'authority': 'user:delete', 'checked': 0,
             'updateTime': '2018/07/13 09:13:42', 'isMenu': 1, 'parentId': 2},
            {'authorityId': 7, 'authorityName': '角色管理', 'orderNumber': 7, 'menuUrl': 'system/role', 'menuIcon': None,
             'createTime': '2018/06/29 11:05:41', 'authority': None, 'checked': 0, 'updateTime': '2018/07/13 09:13:42',
             'isMenu': 0, 'parentId': 1},
            {'authorityId': 8, 'authorityName': '查询角色', 'orderNumber': 8, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/07/21 13:54:59', 'authority': 'role:view', 'checked': 0,
             'updateTime': '2018/07/21 13:54:58', 'isMenu': 1, 'parentId': 7},
            {'authorityId': 9, 'authorityName': '添加角色', 'orderNumber': 9, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/06/29 11:05:41', 'authority': 'role:add', 'checked': 0,
             'updateTime': '2018/07/13 09:13:42', 'isMenu': 1, 'parentId': 7},
            {'authorityId': 10, 'authorityName': '修改角色', 'orderNumber': 10, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/06/29 11:05:41', 'authority': 'role:edit', 'checked': 0,
             'updateTime': '2018/07/13 09:13:42', 'isMenu': 1, 'parentId': 7},
            {'authorityId': 11, 'authorityName': '删除角色', 'orderNumber': 11, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/06/29 11:05:41', 'authority': 'role:delete', 'checked': 0,
             'updateTime': '2018/07/13 09:13:42', 'isMenu': 1, 'parentId': 7},
            {'authorityId': 12, 'authorityName': '角色权限管理', 'orderNumber': 12, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/06/29 11:05:41', 'authority': 'role:auth', 'checked': 0,
             'updateTime': '2018/07/13 15:27:18', 'isMenu': 1, 'parentId': 7},
            {'authorityId': 13, 'authorityName': '权限管理', 'orderNumber': 13, 'menuUrl': 'system/authorities',
             'menuIcon': None, 'createTime': '2018/06/29 11:05:41', 'authority': None, 'checked': 0,
             'updateTime': '2018/07/13 15:45:13', 'isMenu': 0, 'parentId': 1},
            {'authorityId': 14, 'authorityName': '查询权限', 'orderNumber': 14, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/07/21 13:55:57', 'authority': 'authorities:view', 'checked': 0,
             'updateTime': '2018/07/21 13:55:56', 'isMenu': 1, 'parentId': 13},
            {'authorityId': 15, 'authorityName': '添加权限', 'orderNumber': 15, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/06/29 11:05:41', 'authority': 'authorities:add', 'checked': 0,
             'updateTime': '2018/06/29 11:05:41', 'isMenu': 1, 'parentId': 13},
            {'authorityId': 16, 'authorityName': '修改权限', 'orderNumber': 16, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/07/13 09:13:42', 'authority': 'authorities:edit', 'checked': 0,
             'updateTime': '2018/07/13 09:13:42', 'isMenu': 1, 'parentId': 13},
            {'authorityId': 17, 'authorityName': '删除权限', 'orderNumber': 17, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/06/29 11:05:41', 'authority': 'authorities:delete', 'checked': 0,
             'updateTime': '2018/06/29 11:05:41', 'isMenu': 1, 'parentId': 13},
            {'authorityId': 18, 'authorityName': '登录日志', 'orderNumber': 18, 'menuUrl': 'system/loginRecord',
             'menuIcon': None, 'createTime': '2018/06/29 11:05:41', 'authority': None, 'checked': 0,
             'updateTime': '2018/06/29 11:05:41', 'isMenu': 0, 'parentId': 1},
            {'authorityId': 19, 'authorityName': '查询登录日志', 'orderNumber': 19, 'menuUrl': '', 'menuIcon': '',
             'createTime': '2018/07/21 13:56:43', 'authority': 'loginRecord:view', 'checked': 0,
             'updateTime': '2018/07/21 13:56:43', 'isMenu': 1, 'parentId': 18}]}

        return JsonResponse(menu)


class UserApiView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        # 从前端获取当前的页码数,默认为1
        page = request.GET.get('page', 1)
        count = request.GET.get('limit', 10)

        # 把当前的页码数转换成整数类型
        currentPage = int(page)
        countList = int(count)
        user_list = Users.objects.all()
        paginator_user = user_list[(currentPage - 1) * countList:currentPage * countList]

        new_list = list()

        for i, v in enumerate(paginator_user):
            new_dict = {'id': i + 1 + ((currentPage - 1) * countList), 'username': v.username, 'sex': v.sex,
                        'super': v.is_superuser,
                        'create': v.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                        'experience': 255,
                        'logins': 24, 'wealth': 82830700, 'classify': '作家', 'score': 57, "uid": v.id}
            new_list.append(new_dict)

        user = {'code': 0, 'msg': '', 'count': user_list.count(), 'data': new_list}

        return JsonResponse(user)
