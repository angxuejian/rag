# Html

1. 使用语义化标签替代通用 div 标签：
    
    header, main, section, article, nav, aside, footer 等

2. 使⽤双引号(" ") ⽽不是单引号(' ')

3. 使⽤ 2 个空格（⼀个 tab）、嵌套的节点应该缩进。

4. 在每⼀个块状元素，列表元素和表格元素后，加上⼀对 HTML 注释。注释格式

# Css

1. 类名使用小写字母，多个单词使用 - 连接（kebab-case）。

2. 使用 BEM 命名规范：block__element--modifier。

3. 所有 class 和 ID 的命名需语义化，表达其目的和作用，避免外观式命名（如 .red-box）。

    使用选择器时：

        仅使用 类选择器（class）或 ID 选择器，避免使用标签名（如 div、span 等）

        避免使用 后代选择器（空格）

        推荐使用 子选择器（>） 表达层级结构

        不使用通配选择器（如 *）

4. 省略0后⾯的单位

5. 避免使⽤ID选择器及全局标签选择器防⽌污染全局样式

# Javascript

1. 使用 let 或 const，避免使用 var。

2. 使用箭头函数（() => {}） 替代传统的 function 声明（除非必须使用构造函数或类方法）。

3. 保持代码简洁、清晰、易读。

4. 函数命名规范（严格遵循）：

    - 函数名使用 camelCase 命名法，首字母小写，词语间首字母大写

    - 使用动词开头，表达清晰动作语义

    - 避免模糊命名，如 doSomething

    - 名字尽量简短、精准

    不同功能类别，使用以下前缀：

    | 类别        | 前缀                    | 示例                                |
    | --------- | --------------------- | --------------------------------- |
    | 获取数据      | `get`                 | `getUserInfo()`                   |
    | 计算数据      | `calc`                | `calcTotal()`                     |
    | 设置数据      | `set`                 | `setUserName()`                   |
    | 更新数据      | `update`              | `updateSize()`                    |
    | 新增数据      | `add`                 | `addItem()`                       |
    | 移除数据      | `remove`              | `removeItem()`                    |
    | 删除数据      | `delete`              | `deleteUser()`                    |
    | 处理事件      | `handle`              | `handleClick()`                   |
    | 判断 / 校验   | `is` / `check`        | `isVisible()` / `checkAuth()`     |
    | 请求远程数据    | `load`                | `loadData()`                      |
    | 创建对象 / 实体 | `create` / `generate` | `createUser()` / `generateUUID()` |