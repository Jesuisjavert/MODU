<template>
  <v-container>
    <v-row class="justify-space-around">
      <v-col class="col-2 text-center client">
        <h2>회원 목록</h2>
        <div id="lnb">
          <div id="lnb-calendars" class="lnb-calendars">
            <div class="calendarItemList">
              <input type='checkbox' @click="checkAll()" v-model='isCheckAll'>스케줄 모두보기
              <ul class="program-list">
                <li v-for="calendarListItem in calendarList" :key="calendarListItem.id">
                <input type='checkbox' checked  v-bind:value="calendarListItem.id" v-model="workList" @change='updateCheckall()'>{{ calendarListItem.name }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </v-col>
      <v-col class="col-9">
        <div id="menu">
          <div>
            {{ getTime }}
          </div>
          <span class="dropdown">
            <button
              id="dropdownMenu-calendarType"
              class="btn btn-default btn-sm dropdown-toggle"
              type="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="true"
            >
              <span id="calendarTypeName" style="width:120px;">{{ view }}</span
              >&nbsp;
            </button>
            <ul
              class="dropdown-menu"
              role="menu"
              aria-labelledby="dropdownMenu-calendarType"
            >
              <li role="presentation">
                <a
                  class="dropdown-menu-title"
                  role="menuitem"
                  data-action="toggle-monthly"
                >
                  <i class="fas fa-th month-icon"></i>Month
                </a>
              </li>
              <li role="presentation">
                <a
                  class="dropdown-menu-title"
                  role="menuitem"
                  data-action="toggle-weekly"
                >
                  <i class="fas fa-bars weekly-icon"></i>Weekly
                </a>
              </li>
              <li role="presentation">
                <a
                  class="dropdown-menu-title"
                  role="menuitem"
                  data-action="toggle-daily"
                >
                  <i class="fas fa-bars daily-icon"></i>Daily
                </a>
              </li>
              <li role="presentation">
                <a
                  class="dropdown-menu-title"
                  role="menuitem"
                  data-action="toggle-weeks2"
                >
                  <i class="calendar-icon ic_view_week"></i>2 weeks
                </a>
              </li>
              <li role="presentation">
                <a
                  class="dropdown-menu-title"
                  role="menuitem"
                  data-action="toggle-weeks3"
                >
                  <i class="calendar-icon ic_view_week"></i>3 weeks
                </a>
              </li>
              <li role="presentation" class="dropdown-divider"></li>
              <li role="presentation">
                <a role="menuitem" data-action="toggle-workweek">
                  <input
                    type="checkbox"
                    class="tui-full-calendar-checkbox-square"
                    value="toggle-workweek"
                    checked
                  />
                  <span class="checkbox-title"></span>Show weekends
                </a>
              </li>
            </ul>
          </span>
          <span id="menu-navi">
            <button
              type="button"
              class="btn btn-today"
              data-action="move-today"
              @click="moveToTday()"
            >
              Today
            </button>
            <button
              type="button"
              class="btn btn-move"
              data-action="move-prev"
              @click="moveToNextOrPrevRange(-1)"
            >
              <i class="fas fa-angle-left" data-action="move-prev"></i>
            </button>
            <button
              type="button"
              class="btn btn-move"
              data-action="move-next"
              @click="moveToNextOrPrevRange(1)"
            >
              <i class="fas fa-angle-right" data-action="move-next"></i>
            </button>
          </span>
          <span id="renderRange" class="render-range"></span>
        </div>
        <calendar
          style="height: 620px;"
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
          :disableClick="disableClick"
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
import "tui-calendar/dist/tui-calendar.css";
import { Calendar } from "@toast-ui/vue-calendar";

// If you use the default popups, use this.
import "tui-date-picker/dist/tui-date-picker.css";
import "tui-time-picker/dist/tui-time-picker.css";

export default {
  name: "myCalendar",
  components: {
    calendar: Calendar
  },
  created(){
    this.schedule.forEach((item)=>{
      item.bgColor = this.color[Number(item.calendarId)]
      item.borderColor = this.color[Number(item.calendarId)]
      item.color = this.fontColor[Number(item.calendarId)]
    })
  },
  mounted() {
    this.setRenderRangeText(), this.setEventListener();
    this.calendarList.forEach((item)=>{
      this.workList.push(item.id)
    })
  },
  computed: {
    scheduleList(){
      console.log(this.schedule)
      if (this.isCheckAll == true){
        return this.schedule
      } else {
        return this.schedule.filter((item)=>{
          return this.workList.indexOf(item.calendarId) != -1
        })

      }
       return []

    }
  },
  watch :{
  },
  data() {
    return {
      isCheckAll: true,
      workList: [],
      color: ['#1F85DE', '#4BDEBD', '#DE4B6C',  '#159A5D', '#AA1A45', '#DE781F', '#651AAA' ,'#F6F64F'],
      fontColor: ['#ffffff', '#000000', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#000000' ],
      calendarList: [
        {
          id: "0",
          name: "퍼스널 트레이닝"
        },
        {
          id: "1",
          name: "스피닝"
        }
      ],
      schedule: [
        {
          calendarId: "1",
          title: "my schedule",
          category: "time",
          dueDateClass: "",
          start: "2020-11-03T22:30:00+09:00",
          end: "2020-11-04T22:30:00+09:00",
        },
        {
          calendarId: "0",
          title: "second schedule",
          category: "time",
          dueDateClass: "",
          start: "2020-11-18T17:30:00+09:00",
          end: "2020-11-19T17:29:00+09:00"
        }
      ],
      view: "month",
      taskView: false,
      scheduleView: ["time"],
      theme: {
        "month.dayname.height": "30px",
        "month.dayname.borderLeft": "1px solid #ff0000",
        "month.dayname.textAlign": "center",
        "week.today.color": "#333",
        "week.daygridLeft.width": "100px",
        "week.timegridLeft.width": "100px"
      },
      week: {
        narrowWeekend: true,
        showTimezoneCollapseButton: true,
        timezonesCollapsed: false
      },
      month: {
        visibleWeeksCount: 5,
        startDayOfWeek: 0
      },
      timezones: [
        {
          timezoneOffset: 540,
          displayLabel: "GMT+09:00",
          tooltip: "Seoul"
        },
        {
          timezoneOffset: -420,
          displayLabel: "GMT-08:00",
          tooltip: "Los Angeles"
        }
      ],
      disableDblClick: false,
      isReadOnly: false,
      disableClick: false,
      template: {
        milestone: function(schedule) {
          return `<span style="color:red;">${schedule.title}</span>`;
        },
        milestoneTitle: function() {
          return "MILESTONE";
        }
      },
      useCreationPopup: false,
      useDetailPopup: true,
      getTime: ""
    };
  },
  methods: {
    checkAll: function(){
      this.isCheckAll = !this.isCheckAll;
      this.workList = [];
      if(this.isCheckAll){ // Check all
        for (var key in this.calendarList) {
          this.workList.push(this.calendarList[key]);
        }
      }
    },
    updateCheckall: function(){
      if(this.workList.length == this.calendarList.length){
         this.isCheckAll = true;
      }else{
         this.isCheckAll = false;
      }
    },
    moveToNextOrPrevRange(val) {
      if (val === -1) {
        this.$refs.tuiCalendar.invoke("prev");
      } else if (val === 1) {
        this.$refs.tuiCalendar.invoke("next");
      }
    },

    // 오늘 날짜로 이동
    moveToTday() {
      this.$refs.tuiCalendar.invoke("today");
    },
    // setCalendarList() {
    //   var calendarItemList = document.getElementById("calendarItemList");
    //   var html = [];
    //   this.calendarList.forEach(function(calendar) {
    //     html.push(
    //       '<div class="lnb-calendars-item"><label>' +
    //         '<input type="checkbox" class="tui-full-calendar-checkbox-round" value="' +
    //         Calendar.id +
    //         '" checked>' +
    //         '<span style="border-color: ' +
    //         Calendar.borderColor +
    //         "; background-color: " +
    //         Calendar.borderColor +
    //         ';"></span>' +
    //         "<span>" +
    //         Calendar.name +
    //         "</span>" +
    //         "</label></div>"
    //     );
    //   });
    //   calendarItemList.innerHTML = html.join("\n");
    // },
    //
    setRenderRangeText() {
      var renderRange = document.getElementById("renderRange");
      var options = this.$refs.tuiCalendar.invoke("getOptions");
      var viewName = this.$refs.tuiCalendar.invoke("getViewName");
      var html = [];
      if (viewName === "day") {
        html.push(this.currentCalendarDate("YYYY.MM.DD"));
      } else if (
        viewName === "month" &&
        (!options.month.visibleWeeksCount ||
          options.month.visibleWeeksCount > 4)
      ) {
        html.push(this.currentCalendarDate("YYYY.MM"));
      } else {
        html.push(
          this.$moment(
            this.$refs.tuiCalendar.invoke("getDateRangeStart").getTime()
          ).format("YYYY.MM.DD")
        );
        html.push(" ~ ");
        html.push(
          this.$moment(
            this.$refs.tuiCalendar.invoke("getDateRangeEnd").getTime()
          ).format(" MM.DD")
        );
      }
      renderRange.innerHTML = html.join("");
    },

    // dropdown menu 변경
    onClickMenu(e) {
      var target = $(e.target).closest('a[role="menuitem"]')[0];
      var action = this.getDataAction(target);
      var options = this.$refs.tuiCalendar.invoke("getOptions");
      var viewName = "";

      console.log(target);
      console.log(action);
      switch (action) {
        case "toggle-daily":
          viewName = "day";
          break;
        case "toggle-weekly":
          viewName = "week";
          break;
        case "toggle-monthly":
          options.month.visibleWeeksCount = 0;
          viewName = "month";
          break;
        case "toggle-weeks2":
          options.month.visibleWeeksCount = 2;
          viewName = "month";
          break;
        case "toggle-weeks3":
          options.month.visibleWeeksCount = 3;
          viewName = "month";
          break;
        case "toggle-narrow-weekend":
          options.month.narrowWeekend = !options.month.narrowWeekend;
          options.week.narrowWeekend = !options.week.narrowWeekend;
          viewName = this.$refs.tuiCalendar.invoke("getViewName");

          target.querySelector("input").checked = options.month.narrowWeekend;
          break;
        case "toggle-start-day-1":
          options.month.startDayOfWeek = options.month.startDayOfWeek ? 0 : 1;
          options.week.startDayOfWeek = options.week.startDayOfWeek ? 0 : 1;
          viewName = this.$refs.tuiCalendar.invoke("getViewName");

          target.querySelector("input").checked = options.month.startDayOfWeek;
          break;
        case "toggle-workweek":
          options.month.workweek = !options.month.workweek;
          options.week.workweek = !options.week.workweek;
          viewName = this.$refs.tuiCalendar.invoke("getViewName");

          target.querySelector("input").checked = !options.month.workweek;
          break;
        default:
          break;
      }
      console.log("들어왔습니다.");
      this.$refs.tuiCalendar.invoke("setOptions", (options, true));
      console.log("여기가 문제냐?");
      console.log(viewName, "여기는 Vue에요");
      this.$refs.tuiCalendar.invoke("changeView", ("newViewName", viewName));
      console.log("위에가 끝났습니다.");
      console.log(this.calendarList);
      this.setDropdownCalendarType();
      this.setRenderRangeText();
      this.setSchedules();
    },
    setSchedules() {
      this.$refs.tuiCalendar.invoke("clear");
      console.log(
        "문제",
        this.$refs.tuiCalendar.invoke("getViewName"),
        this.$refs.tuiCalendar.invoke("getDateRangeStart"),
        this.$refs.tuiCalendar.invoke("getDateRangeEnd")
      );
      this.generateSchedule(
        this.$refs.tuiCalendar.invoke("getViewName"),
        this.$refs.tuiCalendar.invoke("getDateRangeStart"),
        this.$refs.tuiCalendar.invoke("getDateRangeEnd")
      );
      this.scheduleList.forEach(item => {
        this.$refs.tuiCalendar.invoke("createSchedules", [item]);
        console.log(item, "여기는 반복문입니다.");
      });

      this.refreshScheduleVisibility();
    },
    getDataAction(target) {
      return target.dataset
        ? target.dataset.action
        : target.getAttribute("data-action");
    },
    currentCalendarDate(format) {
      var currentDate = this.$moment([
        this.$refs.tuiCalendar.invoke("getDate").getFullYear(),
        this.$refs.tuiCalendar.invoke("getDate").getMonth(),
        this.$refs.tuiCalendar.invoke("getDate").getDate()
      ]);

      return currentDate.format(format);
    },
    setRenderRangeText() {
      var renderRange = document.getElementById("renderRange");
      var options = this.$refs.tuiCalendar.invoke("getOptions");
      var viewName = this.$refs.tuiCalendar.invoke("getViewName");

      var html = [];
      if (viewName === "day") {
        html.push(this.currentCalendarDate("YYYY.MM.DD"));
      } else if (
        viewName === "month" &&
        (!options.month.visibleWeeksCount ||
          options.month.visibleWeeksCount > 4)
      ) {
        html.push(this.currentCalendarDate("YYYY.MM"));
      } else {
        html.push(
          this.$moment(
            this.$refs.tuiCalendar.invoke("getDateRangeStart").getTime()
          ).format("YYYY.MM.DD")
        );
        html.push(" ~ ");
        html.push(
          this.$moment(
            this.$refs.tuiCalendar.invoke("getDateRangeEnd").getTime()
          ).format(" MM.DD")
        );
      }
      renderRange.innerHTML = html.join("");
    },
    setDropdownCalendarType() {
      var calendarTypeName = document.getElementById("calendarTypeName");
      var options = this.$refs.tuiCalendar.invoke("getOptions");
      var type = this.$refs.tuiCalendar.invoke("getViewName");

      if (type === "day") {
        type = "Daily";
      } else if (type === "week") {
        type = "Weekly";
      } else if (options.month.visibleWeeksCount === 2) {
        type = "2 weeks";
      } else if (options.month.visibleWeeksCount === 3) {
        type = "3 weeks";
      } else {
        type = "Monthly";
      }
      console.log("끝");
      calendarTypeName.innerHTML = type;
    },
    setEventListener() {
      // $('#menu-navi').on('click', onClickNavi);
      $('.dropdown-menu a[role="menuitem"]').on("click", this.onClickMenu);
      $("#lnb-calendars").on("change", this.onChangeCalendars);

      // $('#btn-save-schedule').on('click', onNewSchedule);
      // $('#dropdownMenu-calendars-list').on('click', onChangeNewScheduleCalendar);

      // window.addEventListener('resize', resizeThrottled);
    },
  }
};
</script>

<style scoped>
.client {
  border: solid 2px rgba(122, 122, 122, 0.2);
}

#menu {
  display: flex;
  margin-bottom: 12px;
  align-items: center;
}

ul {
  padding: 4px 0px;
}

.btn {
  border: 1px solid #aaaaaa;
  padding: 6px 12px;
  font-size: 16px;
  font-weight: bold;
  margin-right: 8px;
}

.btn:focus {
  outline: none;
}

.fas {
  margin-right: 8px;
}

.weekly-icon {
  transform: rotate(90deg);
}

.btn-move {
  width: 39px;
  font-size: 18px;
  border-radius: 50%;
}

.btn-move i {
  margin: auto;
}

.program-list {
  list-style: none;
}
</style>
