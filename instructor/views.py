from django.contrib.auth.models import User
from django.http import FileResponse
from django.shortcuts import render, redirect

from user.models import Profile
from zzulibm import PDF
from zzulibm.models import *
from instructor.settings import BASE_DIR

def index(request):
    context = {}
    return render(request, 'index.html', context)

def recruit(request):
    if request.method=='POST':
        img = request.FILES.get('img')  # 图片
        uname = request.POST['uname']  # 姓名
        ug = request.POST['ug']  # 岗位类别
        ument = request.POST['ument']  # 部门
        ufangxiang = request.POST['ufangxiang']  # 专业方向
        sex = request.POST['sex']  # 性别
        YYYY = request.POST['YYYY']
        DD = request.POST['DD']
        MM = request.POST['MM']
        jg = request.POST['jg']  # 籍贯
        minzu = request.POST['minzu']  # 民族
        zzmm = request.POST['zzmm']  # 政治面貌
        topxl = request.POST['topxl']  # 最高学历
        topxw = request.POST['topxw']  # 最高学位
        #GYYY = request.POST['GYYY']  # 工作年
        #GM = request.POST['GM']  # 工作月
        Ewater = request.POST['Ewater']  # 英语水平
        nowwork = request.POST['nowwork']  # 现在工作单位
        zhiwu = request.POST['zhiwu']  # 职务
        Email = request.POST['Email']  # 电子邮件
        phone = request.POST['phone']  # 手机号
        GYYYM=request.POST.get('GYYYM')
        context={}
        if(len(uname)==0):
            context['message1']='姓名不能为空！'

        if(len(ufangxiang)==0):
            context['message4']='专业方向不能为空!'
        if(len(jg)==0):
            context['message5']='籍贯不能为空！'
        if(len(minzu)==0):
            context['message6']='民族不能为空!'
        if(len(zzmm)==0):
            context['message7']='政治面貌不能为空！'
        if(len(topxl)==0):
            context['message8']='学历不能为空!'
        if(len(topxw)==0):
            context['message9']='学位不能为空！'
        if(len(Ewater)==0):
            context['message10']='请选择英语水平!'


        if(len(Email)==0):
            context['message13']='邮箱不能为空！'
        if(len(phone)==0):
            context['message14']='手机号不能为空！'

        if not img:
            context['message16']='请上传照片！'

        if(len(context)!=0):
            print(context)
            return render(request,'recruit.html',context)

        jingli1=""#学习经历
        jingli2=""
        jingli3=""
        jingli4 = ""
        jingli5 = ""
        jingli6 = ""
        jingli7 = ""
        jopexp1=""#工作经历
        jopexp2=""
        jopexp3 = ""
        jopexp4 = ""
        jopexp5 = ""
        jopexp6 = ""
        jopexp7 = ""
        Paper1=""#论文情况
        Paper2=""
        Paper3=""
        Paper4 = ""
        Paper5 = ""
        Paper6 = ""
        Paper7 = ""
        project1=""#项目成果
        project2 = ""
        project3 = ""
        project4 = ""
        project5 = ""
        project6 = ""
        project7 = ""
        reward1=""#获奖记录
        reward2 = ""
        reward3 = ""
        reward4 = ""
        reward5 = ""
        reward6 = ""
        reward7 = ""
        reward8 = ""
        reward9 = ""
        reward10 = ""
        listjingli=[jingli1,jingli2,jingli3,jingli4,jingli5,jingli6,jingli7]#学习经历
        listjobexp=[jopexp1,jopexp2,jopexp3,jopexp4,jopexp5,jopexp6,jopexp7]#工作经历
        listPaper=[Paper1,Paper2,Paper3,Paper4,Paper5,Paper5,Paper6,Paper7]#论文
        listproject=[project1,project2,project3,project4,project5,project6,project7]#项目成果
        listreward=[reward1,reward2,reward3,reward4,reward5,reward6,reward7,reward8,reward9,reward10]#获奖记录
        for num in range(0,7):
          try:
              listjingli[num]=request.POST['sdt'+str(num)] + '|' + request.POST['grd'+str(num)] + '|' + request.POST['zyfx'+str(num)] + '|' + request.POST[
            'xxw'+str(num)]

          except:
              break

        for num in range(0,7):
          try:
              listjobexp[num]=request.POST['ym'+str(num)]+'|'+request.POST['gzdw'+str(num)]+'|'+request.POST['csgz'+str(num)]+'|'+request.POST['zczw'+str(num)]
          except:
              break

        for num in range(0,7):
          try:
              listPaper[num]=request.POST['lwyear'+str(num)]+'|'+request.POST['lwtm'+str(num)]+'|'+request.POST['kwmc'+str(num)]+'|'+request.POST['grmc'+str(num)]
          except:
              break

        for num in range(0,7):
          try:
              listproject[num]=request.POST['xmyear'+str(num)]+'|'+request.POST['xmmc'+str(num)]+"|"+request.POST['xmdj'+str(num)]+"|"+request.POST['xmgr'+str(num)]
          except:
              break

        for num in range(0,10):
          try:
              listreward[num]=request.POST['pryear'+str(num)]+'|'+request.POST['pxmmc'+str(num)]+"|"+request.POST['hjhb'+str(num)]+"|"+request.POST['prgr'+str(num)]
          except:
              break



        #gym = GYYY + '年' + GM + '月'
        YMD = YYYY + '.' + MM + '.' + DD  # 出生日期
        textname = request.POST['textname']  # 学生干部情况
        create = MD.objects.create(uname=uname, ug=ug, ument=ument, ufangxiang=ufangxiang, sex=sex, date=YMD, img=img,
                                   jg=jg, minzu=minzu, zzmm=zzmm, topxl=topxl, topxw=topxw, gym=GYYYM, jingli1=listjingli[0],
                                   jingli2=listjingli[1], jingli3=listjingli[2],jingli4=listjingli[3],jingli5=listjingli[4],jingli6=listjingli[5],
                                   jingli7=listjingli[6],Ewater=Ewater, nowwork=nowwork, zhiwu=zhiwu,
                                   Email=Email, phone=phone, jopexp1=listjobexp[0],jopexp2=listjobexp[1],jopexp3=listjobexp[2],jopexp4=listjobexp[3],
                                   jopexp5=listjobexp[4],jopexp6=listjobexp[5],jopexp7=listjobexp[6],Paper1=listPaper[0],Paper2=listPaper[1]
                                   ,Paper3=listPaper[2],Paper4=listPaper[3],Paper5=listPaper[4],Paper6=listPaper[5],Paper7=listPaper[6],project1=listproject[0],
                                   project2=listproject[1],project3=listproject[2],project4=listproject[3],project5=listproject[4],project6=listproject[5],project7=listproject[6],textname=textname,
                                   reward1=listreward[0],reward2=listreward[1],reward3=listreward[2],reward4=listreward[3],reward5=listreward[4],reward6=listreward[5]
                                   ,reward7=listreward[6],reward8=listreward[7],reward9=listreward[8],reward10=listreward[9])
        PDF.rpt(uname,str(request.user.id))
        user=User.objects.get(id=request.user.id)
        print(user)
        print("1313132")
        user.profile.submited=True
        print(user.profile.submited)
        user.profile.save();
        return render(request, 'recruit.html')
    context = {}
    return render(request, 'recruit.html', context)

def download(request):
    filename=FILE.objects.filter(filename__endswith='-'+str(request.user.id)).values('filename')
    file = open(BASE_DIR + '/media/pdf/' + filename[0]['filename'] + '.pdf', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s.pdf"' % (filename[0]['filename'])
    return response

def test(request):
    context = {}
    return render(request, 'base_2.html', context)