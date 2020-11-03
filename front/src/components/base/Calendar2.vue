<template>
  <div>
    <div id="menu">

    </div>
    <calendar style="height: 620px;"
        :calendars="calendarList"
        :schedules="scheduleList"
        :view="view"
        :taskView="taskView"
        :scheduleView="scheduleView"
        :theme="theme"
        :week="week"
        :month="month"
        :timezones="timezones"
        :disableDblClick="disableDblClick"
        :isReadOnly="isReadOnly"
        :template="template"
        :useCreationPopup="useCreationPopup"
        :useDetailPopup="useDetailPopup"
    />
  </div>
</template>

<script>
import 'tui-calendar/dist/tui-calendar.css'
import { Calendar } from '@toast-ui/vue-calendar'

// If you use the default popups, use this.
import 'tui-date-picker/dist/tui-date-picker.css';
import 'tui-time-picker/dist/tui-time-picker.css';

export default {
  name: 'myCalendar',
  components: {
      'calendar': Calendar
  },
  data() {
      return {
          calendarList: [
              {
                  id: '0',
                  name: 'home'
              },
              {
                  id: '1',
                  name: 'office'
              }
          ],
          scheduleList: [
              {
                  id: '1',
                  calendarId: '1',
                  title: 'my schedule',
                  category: 'time',
                  dueDateClass: '',
                  start: '2020-11-03T22:30:00+09:00',
                  end: '2020-11-04T22:30:00+09:00'
              },
              {
                  id: '2',
                  calendarId: '1',
                  title: 'second schedule',
                  category: 'time',
                  dueDateClass: '',
                  start: '2020-11-18T17:30:00+09:00',
                  end: '2020-11-19T17:31:00+09:00'
              }
          ],
          view: 'month',
          taskView: false,
          scheduleView: ['time'],
          theme: {
              'month.dayname.height': '30px',
              'month.dayname.borderLeft': '1px solid #ff0000',
              'month.dayname.textAlign': 'center',
              'week.today.color': '#333',
              'week.daygridLeft.width': '100px',
              'week.timegridLeft.width': '100px'
          },
          week: {
              narrowWeekend: true,
              showTimezoneCollapseButton: true,
              timezonesCollapsed: false
          },
          month: {
              visibleWeeksCount: 5,
              startDayOfWeek: 1
          },
          timezones: [{
              timezoneOffset: 540,
              displayLabel: 'GMT+09:00',
              tooltip: 'Seoul'
          }, {
              timezoneOffset: -420,
              displayLabel: 'GMT-08:00',
              tooltip: 'Los Angeles'
          }],
          disableDblClick: true,
          isReadOnly: false,
          template: {
              milestone: function(schedule) {
                  return `<span style="color:red;">${schedule.title}</span>`;
              },
              milestoneTitle: function() {
                  return 'MILESTONE';
              },
          },
          useCreationPopup: true,
          useDetailPopup: false,
      }
  },
  methods : {
    
  }
}
</script>

<style>

</style>