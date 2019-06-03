from django.contrib import admin
from django.http import StreamingHttpResponse

from zzulibm.models import *
import xlwt
# Register your models here.
#admin.site.register(MD)
admin.site.register(FILE)

class DebitAdmin(admin.ModelAdmin):
    list_display = ['uname','sex','date','zzmm','ug','ufangxiang','ument','Email','phone']
    search_fields = ['uname','phone']
    list_filter = ['uname','ufangxiang','ument','ug','sex']


    actions = ['saveexecl']
    def saveexecl(self,request,queryset):
        filename="result.xls"
        Begin=xlwt.Workbook()
        sheet=Begin.add_sheet("response")
        sheet.write(0,0,"姓名")#表头
        sheet.write(0,1,"性别")
        sheet.write(0,2,"年龄")
        sheet.write(0,3,"民族")
        sheet.write(0,4,"政治面貌")
        sheet.write(0,5,"籍贯")
        sheet.write(0,6,"岗位类别")
        sheet.write(0,7,"部门")
        sheet.write(0,8,"专业方向")
        sheet.write(0,9,"最高学历")
        sheet.write(0,10,"最高学位")
        sheet.write(0,11,"参加工作时间")
        sheet.write(0,12,"手机号")
        sheet.write(0,13,"电子邮箱")
        sheet.write(0,14,"外语水平")
        sheet.write(0,15,"现工作单位")
        sheet.write(0,16,"职务")
        cols=1

        sheet.col(5).width=3333
        sheet.col(6).width = 3333
        sheet.col(7).width = 3333
        sheet.col(8).width = 3333
        sheet.col(11).width = 3333
        sheet.col(12).width = 3333
        sheet.col(13).width = 5555
        sheet.col(15).width = 4444

        for query in queryset:#从查询集合中向表写入数据
            sheet.write(cols,0,str(query.uname))
            sheet.write(cols,1,str(query.sex))
            sheet.write(cols,2,str(query.date))
            sheet.write(cols,3,str(query.minzu))
            sheet.write(cols,4,str(query.zzmm))
            sheet.write(cols,5,str(query.jg))
            sheet.write(cols,6,str(query.ug))
            sheet.write(cols,7,str(query.ument))
            sheet.write(cols,8,str(query.ufangxiang))
            sheet.write(cols,9,str(query.topxl))
            sheet.write(cols,10,str(query.topxw))
            sheet.write(cols,11,str(query.gym))
            sheet.write(cols,12,str(query.phone))
            sheet.write(cols,13,str(query.Email))
            sheet.write(cols,14,str(query.Ewater))
            sheet.write(cols,15,str(query.nowwork))
            sheet.write(cols,16,str(query.zhiwu))
            cols+=1
        Begin.save("%s"%(filename))
        def file_iterator(filename,chuck_size=512):#读取迭代
            with open(filename,"rb") as f:
                while True:
                    c=f.read(chuck_size)
                    if c:
                        yield c
                    else:
                        break

        response=StreamingHttpResponse(file_iterator(filename))
        response['Content-type']='application/octet-stream'
        response['Content-Disposition']='attachment;filename="{}"'.format("result.xls")
        return response
    saveexecl.short_description = "导出Excel"

admin.site.register(MD,DebitAdmin)