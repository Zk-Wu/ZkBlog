from django import template
from django.utils.safestring import mark_safe

register = template.Library()

TEMP1 = """
    <div class="list-div"  style='margin-left:%spx;'>
        <div class="media">
            <div class="media-body">
                <p class="mt-0">%s</p>
                <p>
                    <i class="oi oi-monitor red"></i>
                    %s
                    <small style="padding-left:20px;">
                        <i class="oi oi-clock red"></i>
                        %s
                    </small>
                    <small style="padding-left:20px;">
                        <span class="mya sendmes" data-toggle="modal" data-target="#UserMessageModal" data-mesid="%s" data-nicheng="%s">
                            <i class="oi oi-comment-square red"></i>
                            回复
                        </span>
                    </small>
                </p>
            </div>
        </div>
    </div>
"""


@register.simple_tag
def usermes_tag(comment_dic):
    html=''
    for k, v_dic in comment_dic.items():
        html += '<div class="listssdiv">'
        html += TEMP1 % (0, k[2],k[1],k[3],k[0],k[1])
        # 假如子元素的值为真,说明有子评论
        if v_dic:
            # 递归处理,直到全部处理完
            html += generate_comment_html(v_dic, k[1], 30)
        html += '</div>'
        # print(html)
    html += '</div>'
    return mark_safe(html)


def generate_comment_html(sub_comment_dic, fumes,margin_left_val):
    # 遍历子元素
    html=''
    # print(sub_comment_dic)
    for k, v_dic in sub_comment_dic.items():
        html += TEMP1 % (margin_left_val, '回复@'+fumes+':'+k[2],k[1],k[3],k[0],k[1])
        # 假如子元素的值为真,说明有子评论
        if v_dic:
            # 递归处理,直到全部处理完
            html += generate_comment_html(v_dic, k[1], margin_left_val)
    return html
