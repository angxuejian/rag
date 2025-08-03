# Button按钮

常用的操作按钮。

## 默认样式
浏览器默认自带的样式，只对其width/height/color/font-size保持一致，其余均为浏览器自带样式

> plain属性、text属性均不会生效

::: demo
<diyButton text default>Default</diyButton>
:::

## 基础用法
使用```plain```、```text```来定义按钮的样式，其中```Primary```为默认样式

::: demo
<diyButton default>Default</diyButton>
<diyButton>Primary</diyButton>
<diyButton plain>Plain primary</diyButton>
<diyButton text>Text primary</diyButton>
:::

## 加载状态
通过设置 loading 属性为 true 来显示加载中状态。
::: demo
<diyButton loading default>Default</diyButton>
<diyButton loading>Primary</diyButton>
<diyButton loading plain>Plain primary</diyButton>
<diyButton loading text>Text primary</diyButton>
:::

## 禁用状态
使用 disabled 属性来控制按钮是否为禁用状态
::: demo
<diyButton disabled default>Default</diyButton>
<diyButton disabled>Primary</diyButton>
<diyButton disabled plain>Plain primary</diyButton>
<diyButton disabled text>Text primary</diyButton>
:::

## Button Attributes

属性名 | 说明 | 类型 | 默认值
---   | --- | --- | ---
default| 是否显示浏览器默认样式 | boolean | false
plain | 是否为朴素按钮 | boolean | false
text | 是否为文本按钮 | boolean | false
loading| 是否为加载状态 | boolean | false
disabled | 是否为禁用状态 | boolean | false

## Button Slots

插槽名 | 说明
--- | ---
default | 自定义默认内容