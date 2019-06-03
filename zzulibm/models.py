from django.db import models

class MD(models.Model):
    uname=models.CharField('姓名',max_length=50)#姓名
    ug=models.CharField('岗位类别',max_length=50)#岗位类别
    ument=models.CharField('部门',max_length=50)#部门
    ufangxiang=models.CharField('专业方向',max_length=150)#专业方向
    sex=models.CharField('性别',max_length=4)#性别
    date=models.CharField('出生日期',max_length=50)#日期
    img=models.ImageField(upload_to='img')#图片
    jg=models.CharField('籍贯',max_length=50)#籍贯
    minzu=models.CharField('民族',max_length=50)#民族
    zzmm=models.CharField('政治面貌',max_length=50)#政治面貌
    topxl=models.CharField('最高学历',max_length=50)#最高学历
    topxw=models.CharField('最高学位',max_length=50)#最高学位
    gym=models.CharField('参加工作时间',max_length=50)#参加工作时间
    phone=models.CharField('手机号',max_length=50)#手机号
    Email=models.CharField('电子邮箱',max_length=50)#电子邮箱
    Ewater=models.CharField('外语水平',max_length=50)#外语水平
    nowwork=models.CharField('现工作单位',max_length=100)#现工作单位
    zhiwu=models.CharField('职务',max_length=50)#职务
    jingli1=models.CharField('学习经历',max_length=200,null=True,blank=True)#学习经历
    jingli2=models.CharField(max_length=200,null=True,blank=True)
    jingli3=models.CharField(max_length=200,null=True,blank=True)
    jingli4 = models.CharField(max_length=200, null=True, blank=True)
    jingli5 = models.CharField(max_length=200, null=True, blank=True)
    jingli6 = models.CharField(max_length=200, null=True, blank=True)
    jingli7 = models.CharField(max_length=200, null=True, blank=True)
    jopexp1=models.CharField('工作经历',max_length=200,null=True,blank=True)#工作经历
    jopexp2=models.CharField(max_length=200,null=True,blank=True)
    jopexp3 = models.CharField(max_length=200, null=True, blank=True)
    jopexp4 = models.CharField(max_length=200, null=True, blank=True)
    jopexp5 = models.CharField(max_length=200, null=True, blank=True)
    jopexp6 = models.CharField(max_length=200, null=True, blank=True)
    jopexp7 = models.CharField(max_length=200, null=True, blank=True)
    Paper1=models.CharField('论文情况',max_length=200,null=True,blank=True)#论文情况
    Paper2=models.CharField(max_length=200,null=True,blank=True)
    Paper3=models.CharField(max_length=200,null=True,blank=True)
    Paper4 = models.CharField(max_length=200, null=True, blank=True)
    Paper5 = models.CharField(max_length=200, null=True, blank=True)
    Paper6 = models.CharField(max_length=200, null=True, blank=True)
    Paper7 = models.CharField(max_length=200, null=True, blank=True)
    project1=models.CharField('项目成果',max_length=200,null=True,blank=True)#项目成果
    project2=models.CharField(max_length=200, null=True, blank=True)
    project3 = models.CharField(max_length=200, null=True, blank=True)
    project4 = models.CharField(max_length=200, null=True, blank=True)
    project5 = models.CharField(max_length=200, null=True, blank=True)
    project6 = models.CharField(max_length=200, null=True, blank=True)
    project7 = models.CharField(max_length=200, null=True, blank=True)
    reward1=models.CharField('奖励情况',max_length=200,null=True,blank=True)#奖励情况
    reward1 = models.CharField(max_length=200, null=True, blank=True)
    reward2 = models.CharField(max_length=200, null=True, blank=True)
    reward3 = models.CharField(max_length=200, null=True, blank=True)
    reward4 = models.CharField(max_length=200, null=True, blank=True)
    reward5 = models.CharField(max_length=200, null=True, blank=True)
    reward6 = models.CharField(max_length=200, null=True, blank=True)
    reward7 = models.CharField(max_length=200, null=True, blank=True)
    reward8 = models.CharField(max_length=200, null=True, blank=True)
    reward9 = models.CharField(max_length=200, null=True, blank=True)
    reward10 = models.CharField(max_length=200, null=True, blank=True)
    textname=models.TextField('担任学生干部情况',null=True,blank=True)#担任学生干部情况
    #imgname=models.CharField(max_length=100)

    def __str__(self):
        return self.uname

    class Meta:
        verbose_name="报名信息"
        verbose_name_plural="报名信息"

class FILE(models.Model):
    file=models.FileField('报名表',upload_to='pdf')
    filename=models.CharField('姓名',max_length=20)

    def __str__(self):
        return self.filename
    class Meta:
        verbose_name="报名表"
        verbose_name_plural="报名表"