from calendar import HTMLCalendar, month_name
from .models import DailyData

#https://alexpnt.github.io/2017/07/15/django-calendar/
class TrainingData(HTMLCalendar):

    def __init__(self, data=None):
        super(TrainingData, self).__init__()
        self.data = []

    def formatday(self, day, weekday, events):
        data_html = "<ul>"
        for event in self.data:
            data_html += " test <br>"
        data_html += "</ul>"
        
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, data_html)

    def formatweek(self, theweek, data):
        s = ''.join(self.formatday(d, wd, self.data) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonthname(self, theyear, themonth, withyear=True):
        s = month_name[themonth]
        if withyear:
            s += (' ' + str(theyear))
        return '<h5 class="text-secondary">%s</h5>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        month = []
        month.append(self.formatmonthname(theyear, themonth, withyear=withyear))
        month.append('\n')
        month.append('<table border="0" cellpadding="0" cellspacing="0" class="table table-bordered">')
        month.append('\n')
        month.append(self.formatweekheader())
        month.append('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            month.append(self.formatweek(week, self.data))
            month.append('\n')
        month.append('</table>')
        month.append('\n')
        return ''.join(month)
