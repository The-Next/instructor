import datetime

from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import *

from instructor.settings import BASE_DIR
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
import reportlab.lib.fonts
from zzulibm.models import *
reportlab.lib.fonts.ps2tt = lambda psfn: ('STSong-Light', 0, 0)
reportlab.lib.fonts.tt2ps = lambda fn, b, i: 'STSong-Light'
from reportlab.lib.styles import ParagraphStyle


def rpt(i,id):
    A=MD.objects.filter(uname=i).values('uname','sex','date','ug','ument','ufangxiang','img','jg','minzu','zzmm','topxl',
                                        'topxw','gym','phone','Email','Ewater','nowwork','zhiwu',
                                        'jingli1','jingli2','jingli3','jingli4','jingli5','jingli6',
                                        'jingli7','jopexp1','jopexp2','jopexp3','jopexp4','jopexp5',
                                        'jopexp6','jopexp7','Paper1','Paper2','Paper3','Paper4','Paper5',
                                        'Paper6','Paper7','project1','project2','project3','project4',
                                        'project5','project6','project7','reward1','reward2','reward3',
                                        'reward4','reward5','reward6','reward7','reward8','reward9','reward10',
                                        'textname')
    story=[]

    I=Image(BASE_DIR+'/media/'+A[0]['img'])
    I.drawHeight=110
    I.drawWidth=80
    reportlab.lib.styles.ParagraphStyle.defaults['wordWrap'] = 'CJK'
    stylesheet = getSampleStyleSheet()
    normalStyle = stylesheet['Normal']
    style=stylesheet['BodyText']#担任学生干部情况大框的样式
    style.fontName='STSong-Light'
    style.leading=10#行距
    styleword=stylesheet['Normal']
    styleword.wordWrap='CJK'
    styleword.fontName='STSong-Light'
    styleword.leading=10
    styleword.alignment=1#居中
    ParagraphStyle.defaults['workWrap']="CJK"#中文自动换行
    rpt_title = '<para autoLeading="off" fontSize=16 align=center><b><font face="STSong-Light">郑州轻工业学院%s年度招聘人事代理人员报名表</font></b><br/><br/><br/></para>'%(datetime.datetime.now().year)
    rpt_list = '<para autoLeading="off" fontSize=13 align=center><font face="STSong-Light">岗位类别：</font><font face="STSong-Light" fontSize=11>%s&nbsp;&nbsp;</font><font face="STSong-Light">部门：</font><font face="STSong-Light" fontSize=11>%s&nbsp;&nbsp;</font><font face="STSong-Light">专业(方向：</font><font face="STSong-Light" fontSize=11>%s&nbsp;&nbsp;</font><br/><br/><br/></para>'%(A[0]['ug'],A[0]['ument'],A[0]['ufangxiang'])
    component_data=[['姓名',A[0]['uname'],'性别',A[0]['sex'],'出生年月','',A[0]['date'],I],
                    ['籍贯', A[0]['jg'], '民族', A[0]['minzu'], '政治面貌','',A[0]['zzmm'], ''],
                    ['最高学历', A[0]['topxl'], '最高学位', A[0]['topxw'], '参加工作时间','', A[0]['gym'], ''],
                    ['手机号', A[0]['phone'], '电子邮箱', Paragraph(A[0]['Email'], styleword), '外语水平','',A[0]['Ewater'], ''],
                    ['现工作单位', '', Paragraph(A[0]['nowwork'], styleword), '', '职称、职务','',A[0]['zhiwu'], ''],
                    #['担任学\n生干部\n情况', '', Paragraph(A[0]['textname'].replace('\r\n','<br/>'),style), '', '', '', '', ''],
                    ]
    xxjllist=1
    gzjllist=1
    lwqklist=1
    xmktlist=1
    jlqklist=1
    countlist=[xxjllist,gzjllist,lwqklist,xmktlist,jlqklist]
    xuexijingli_data = ['学习\n经历', '起止时间', '', '毕业院校', '', '专业(方向)', '', '学历、学位']
    component_data.append(xuexijingli_data)
    for num in range(1, 8):
        if (len(A[0]['jingli' + str(num)]) == 0):
            break
        else:
            x = A[0]['jingli' + str(num)].split('|')
            xxjl = ['', Paragraph(x[0], styleword), '', Paragraph(x[1], styleword), '', Paragraph(x[2], styleword), '', Paragraph(x[3], styleword)]
            component_data.append(xxjl)
            xxjllist+=1

    gongzuojingli_data = ['工作\n经历', '起止时间', '', '单位', '', '从事专业技术工作', '', '职称、职务']
    component_data.append(gongzuojingli_data)
    for num in range(1, 8):
        if (len(A[0]['jopexp' + str(num)]) == 0):
            break
        else:
            x = A[0]['jopexp'+ str(num)].split('|')
            jobexp = ['', Paragraph(x[0], styleword), '', Paragraph(x[1], styleword), '', Paragraph(x[2], styleword), '', Paragraph(x[3], styleword)]
            component_data.append(jobexp)

            gzjllist+=1

    lunwenqingkuang_data = ['业绩及\n获奖情\n况', '发表\n研究\n论文\n情况', '时间', '论文题目', '', '刊物名称', '', '个人名次']
    component_data.append(lunwenqingkuang_data)
    for num in range(1, 8):
        if (len(A[0]['Paper' + str(num)]) == 0):
            break
        else:
            x = A[0]['Paper' + str(num)].split("|")
            Paper=['', '', Paragraph(x[0], styleword), Paragraph(x[1], styleword), '', Paragraph(x[2], styleword), '', Paragraph(x[3], styleword)]
            component_data.append(Paper)
            lwqklist+=1

    xiangmuketi_data=['','项目\n(课题)、\n成果等', '时间', '项目(成果)名称', '', '项目(成果)等级', '', '个人名次']
    component_data.append(xiangmuketi_data)
    for num in range(1, 8):
        if (len(A[0]['project' + str(num)]) == 0):
            break
        else:
            x = A[0]['project' + str(num)].split("|")
            project=['', '', Paragraph(x[0], styleword), Paragraph(x[1], styleword), '', Paragraph(x[2], styleword), '', Paragraph(x[3], styleword)]
            component_data.append(project)
            xmktlist+=1

    jiangliqingkyuang_data=['', '奖励\n情况', '获奖时间', '奖项名称', '', '获奖级别', '', '个人名次']
    component_data.append(jiangliqingkyuang_data)
    for num in range(1, 8):
        if (len(A[0]['reward' + str(num)]) == 0):
            break
        else:
            x = A[0]['reward' + str(num)].split("|")
            reward=['', '', Paragraph(x[0], styleword), Paragraph(x[1], styleword), '', Paragraph(x[2], styleword), '', Paragraph(x[3], styleword)]
            component_data.append(reward)
            jlqklist+=1


    print(xxjllist,"..",gzjllist,"..",lwqklist,"..",xmktlist,"..",jlqklist)

    xueshengganbu=['担任学\n生干部\n情况', '', Paragraph(A[0]['textname'].replace('\r\n','<br/>'),style), '', '', '', '', '']

    component_data.append(xueshengganbu)



    stylex=[
        ('ALIGN', (0, 0), (-1, -2), 'CENTER'),
        ('ALIGN', (0, -1), (0, -1), 'CENTER'),
        ('ALIGN', (2, -1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'STSong-Light'),  # 字体
        ('TEXTCOLOR', (0, 1), (-2, -1), colors.black),  # 设置表格内文字颜色
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # 设置表格框线为黑色色，线宽为0.5
        ('SPAN', (-4, 0), (-3, 0)),
        ('SPAN', (-4, 1), (-3, 1)),
        ('SPAN', (-4, 2), (-3, 2)),
        ('SPAN', (-4, 3), (-3, 3)),
        ('SPAN', (-4, 4), (-3, 4)),#出生年月那一溜
        ('SPAN', (-4, 0), (-3, 0)),
        ('SPAN', (-1, 0), (-1, 4)),#照片
        ('SPAN', (0, 4), (1, 4)),
        ('SPAN', (2, 4), (3, 4)),#现工作单位
    ]
    #工作经历，业绩情况，项目课题，奖励情况五大模块样式
    for num in range(1,xxjllist+1):
        x=('SPAN', (1, 4+num), (2, 4+num))
        y=('SPAN', (3, 4+num), (4, 4+num))
        z=('SPAN', (5, 4+num), (6, 4+num))
        print('1')
        stylex.append(x)
        stylex.append(y)
        stylex.append(z)
        print(x)
    print(xxjllist)
    for num in range(1,gzjllist+1):
        x=('SPAN', (3, 4+xxjllist+num), (4, 4+xxjllist+num))
        y=('SPAN', (1, 4+xxjllist+num), (2, 4+xxjllist+num))
        z=('SPAN', (5, 4+xxjllist+num), (6, 4+xxjllist+num))
        stylex.append(x)
        stylex.append(y)
        stylex.append(z)

    for num in range(1,lwqklist+1):
        x=('SPAN', (3, 4+xxjllist+gzjllist+num), (4, 4+xxjllist+gzjllist+num))
        y=('SPAN', (5, 4+gzjllist+xxjllist+num), (6, 4+gzjllist+xxjllist+num))
        stylex.append(x)
        stylex.append(y)


    for num in range(1,xmktlist+1):
        y = ('SPAN', (3, 4 + xxjllist + gzjllist + lwqklist +num), (4, 4 + xxjllist + gzjllist + lwqklist +num))
        stylex.append(y)
        x= ('SPAN', (5, 4 + xxjllist + gzjllist + lwqklist +num), (6, 4 + xxjllist + gzjllist + lwqklist +num))
        stylex.append(x)


    for num in range(1,jlqklist+1):
        x=('SPAN', (5, 4 + xxjllist + gzjllist + lwqklist + xmktlist + num), (6, 4 + xxjllist + gzjllist + lwqklist + xmktlist + num))
        y = ('SPAN', (3, 4 + xxjllist + gzjllist + lwqklist + xmktlist + num), (4, 4 + xxjllist + gzjllist + lwqklist + xmktlist + num))
        stylex.append(y)
        stylex.append(x)


    a1=('SPAN', (0, 5), (0, 4+xxjllist))
    a2=('SPAN', (0, 5+xxjllist), (0, 4+xxjllist+gzjllist))
    a3=('SPAN', (1, 5+xxjllist+gzjllist), (1, 4+xxjllist+gzjllist+lwqklist))
    a4=('SPAN', (1, 5+xxjllist+gzjllist+lwqklist), (1, 4+xxjllist+gzjllist+lwqklist+xmktlist))
    a5=('SPAN', (1, 5+xxjllist+gzjllist+lwqklist+xmktlist), (1, 4+xxjllist+gzjllist+lwqklist+xmktlist+jlqklist))
    a6=('SPAN', (0, 5+xxjllist+gzjllist), (0, -2))
    a7=('SPAN', (0, -1), (1, -1))  # 最后一行
    a8=('SPAN', (2, -1), (-1, -1))
    stylex.append(a1)
    stylex.append(a2)
    stylex.append(a3)
    stylex.append(a4)
    stylex.append(a5)
    stylex.append(a6)
    stylex.append(a7)
    stylex.append(a8)


#整合样式
    component_table = Table(component_data, colWidths=[50, 80, 50, 90, 50, 40, 80, 80])
    component_table.setStyle(TableStyle(stylex))
    story.append(Paragraph(rpt_title,normalStyle))
    story.append(Paragraph(rpt_list,normalStyle))
    story.append(component_table)
    sss = reportlab.platypus.SimpleDocTemplate(BASE_DIR+'/media/pdf/'+A[0]['uname']+'-'+str(id)+'.pdf')#
    sss.build(story)
    A=FILE.objects.create(file='pdf/'+i+'-'+str(id)+'.pdf',filename=i+'-'+str(id))
    #db=pymysql.connect(user='root',password='20141232',database='test',charset='utf8')
    #cursor=db.cursor()
    #p='pdf/'+i+'.pdf'
    #try:
     #   sql="INSERT INTO bm_file(file,filename)VALUES('%s','%s')"%(p,i)
      #  print(sql)
       # cursor.execute(sql)
    #except:
     #   db.rollback()
    #db.close()




#if __name__ == '__main__':
#    rpt()