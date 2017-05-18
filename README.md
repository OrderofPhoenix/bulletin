# Phoenix e-Bulletin Prototype

## 已经实现的功能：
### 用户管理部分
* 注册
* 验证激活
* 登陆
* 密码找回
* 修改密码
* 查看个人资料（Profile）
* 加入了注册页面的表单验证机制（尚不完美有时间再做）
### 公告板业务部分
* 创建公告板
* 关注公告板
* 取消关注公告板
* 删除公告板（仅限创建者）
* 发布公告
* 删除公告（仅限发布者）
* 公告下进行评论
* 删除公告下的评论（目前仅限评论人）
* 搜索公告板
* 查看用户公告板（包括所创建及所关注的）
## 如有时间期望实现的功能：
* 发布公告页面加入MarkDown文本编辑器
* 注册等页面的表单加入即时验证功能
## 几个需要注意的地方：
* 在改写models中User模型时最好继承AbstractUser对象，否则后面request.user中的用户跟models.user（区别于django.contrib.auth.models.User）
中的用户不对称，带来一些不必要的麻烦。
* 对于数据库中ManyToManyField类型的属性需要使用[table].objects.filter()来获得一个iterable对象，不能用[table].objects.get()来获取。

__注：访问地址请去查看urls.py文件__