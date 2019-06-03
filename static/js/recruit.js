var count_stuexp=0;
var count_jobexp=0;
var count_pubexp=0;
var count_proexp=0;
var count_winexp=0;

function add(flag){
    var count,ok=0;

    if(flag =='stuexp' && count_stuexp<7){
        count_stuexp++;
        var newone = $(stuexp).clone().attr('id', flag+count_stuexp);
        count=count_stuexp;
        ok=1;
    }
    if(flag =='jobexp' && count_jobexp<7){
        count_jobexp++;
        var newone = $(jobexp).clone().attr('id', flag+count_jobexp);
        count=count_jobexp;
        ok=2;
    }
    if(flag =='pubexp' && count_pubexp<7){
        count_pubexp++;
        var newone = $(pubexp).clone().attr('id', flag+count_pubexp);
        count=count_pubexp;
        ok=3;
    }
    if(flag =='proexp' && count_proexp<7){
        count_proexp++;
        var newone = $(proexp).clone().attr('id', flag+count_proexp);
        count=count_proexp;
        ok=4;
    }
    if(flag =='winexp' && count_winexp<7){
        count_winexp++;
        var newone = $(winexp).clone().attr('id', flag+count_winexp);
        count=count_winexp;
        ok=5;
    }
    if(ok){
        newone.find('label').html('');
        newone.removeAttr("hidden");
        newone.find('#copydiv_1').find('input').attr('name',function(){return this.name+count});
        newone.find('#copydiv_2').find('input').attr('name',function(){return this.name+count});
        newone.find('#copydiv_3').find('input').attr('name',function(){return this.name+count});
        newone.find('#copydiv_4').find('input').attr('name',function(){return this.name+count});
        $("#insert_"+ok).append(newone);
    }
}

function YYYYMMDDstart()
{
    MonHead = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    //先给年下拉框赋内容
    var y  = new Date().getFullYear();
    for (var i = (y-30); i < (y+30); i++) //以今年为准，前30年，后30年
        document.reg_testdate.YYYY.options.add(new Option(" "+ i +" 年", i));

    //赋月份的下拉框
    for (var i = 1; i < 13; i++)
        document.reg_testdate.MM.options.add(new Option(" " + i + " 月", i));

    document.reg_testdate.YYYY.value = y;
    document.reg_testdate.MM.value = new Date().getMonth() + 1;
    var n = MonHead[new Date().getMonth()];
    if (new Date().getMonth() ==1 && IsPinYear(YYYYvalue)) n++;
    writeDay(n); //赋日期下拉框Author:meizz
    document.reg_testdate.DD.value = new Date().getDate();
}

if(document.attachEvent)
    window.attachEvent("onload", YYYYMMDDstart);
else
    window.addEventListener('load', YYYYMMDDstart, false);

function YYYYDD(str) //年发生变化时日期发生变化(主要是判断闰平年)
{
    var MMvalue = document.reg_testdate.MM.options[document.reg_testdate.MM.selectedIndex].value;
    if (MMvalue == ""){ var e = document.reg_testdate.DD; optionsClear(e); return;}
    var n = MonHead[MMvalue - 1];
    if (MMvalue ==2 && IsPinYear(str)) n++;
    writeDay(n)
}

function MMDD(str)   //月发生变化时日期联动
{
    var YYYYvalue = document.reg_testdate.YYYY.options[document.reg_testdate.YYYY.selectedIndex].value;
    if (YYYYvalue == ""){ var e = document.reg_testdate.DD; optionsClear(e); return;}
    var n = MonHead[str - 1];
    if (str ==2 && IsPinYear(YYYYvalue)) n++;
    writeDay(n)
}

function writeDay(n)   //据条件写日期的下拉框
{
    var e = document.reg_testdate.DD; optionsClear(e);
    for (var i=1; i<(n+1); i++)
        e.options.add(new Option(" "+ i + " 日", i));
}

function IsPinYear(year)//判断是否闰平年
{     
    return(0 == year%4 && (year%100 !=0 || year%400 == 0));
}

function optionsClear(e)
{
    e.options.length = 1;
}