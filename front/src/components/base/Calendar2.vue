<template>
  <v-container>
    <v-row class="justify-space-around">
      <v-col class="col-2 text-center client">
        <h2>회원 목록</h2>
        <div v-for="calendarName in calendarList" :key="calendarList.id">
          {{calendarName.name}}
        </div>
      </v-col>
      <v-col class="col-9">
        <div id="menu">
          <span id="menu-navi">
            <button type="button" class="btn btn-default btn-sm move-today" data-action="move-today" @click="moveToTday()">Today</button>
            <button type="button" class="btn btn-default btn-sm move-day" data-action="move-prev">
              <i class="fas fa-angle-left" data-action="move-prev" @click="moveToNextOrPrevRange(-1)"></i>
            </button>
            <button type="button" class="btn btn-default btn-sm move-day" data-action="move-next">
              <i class="fas fa-angle-right" data-action="move-next" @click="moveToNextOrPrevRange(1)"></i>
            </button>
          </span>
          <span id="renderRange" class="render-range"></span>
        </div>
        <calendar style="height: 620px;"
          ref="tuiCalendar"
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
      </v-col>
    </v-row>
  </v-container>
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
                  name: '퍼스널 트레이닝'
              },
              {
                  id: '1',
                  name: '스피닝'
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
    moveToNextOrPrevRange(val) {
      if (val === -1) {
      this.$refs.tuiCalendar.invoke('prev');
      } else if (val === 1) {
      this.$refs.tuiCalendar.invoke('next');
      }
    },
    moveToTday() {
      this.$refs.tuiCalendar.invoke('today');
    },
  }
}
</script>

<style>
.client{
  border: solid 2px rgba(122, 122, 122, 0.2)
}
</style>