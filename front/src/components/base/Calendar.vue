<template>
  <v-container>
    <v-row class="justify-space-around">
      <v-col class="col-2 text-center client">
        <h2>회원 목록</h2>
        <div id="lnb">
          <div id="lnb-calendars" class="lnb-calendars">
            <div class="calendarItemList">
              <div class="calendarItemList-title">
                <input
                  type="checkbox"
                  @click="checkAll()"
                  v-model="isCheckAll"
                />
                <h3>스케줄 모두보기</h3>
              </div>
              <ul class="program-list">
                <li
                  class="program-list-item"
                  :style="
                    `background-color : ${
                      color[calendarListItem.id]
                    }; color : ${fontColor[calendarListItem.id]};`
                  "
                  v-for="calendarListItem in calendarList"
                  :key="calendarListItem.id"
                >
                  <input
                    type="checkbox"
                    v-bind:value="calendarListItem.id"
                    v-model="workList"
                    @change="updateCheckall()"
                  />
                  <span>{{ calendarListItem.name }}</span>
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
          <v-col class="d-flex" cols="6" sm="2">
            <v-select
              class="dropdown"
              :items="modeSelect"
              v-model="selected"
              label="달력 선택"
              dense
              outlined
              v-on:change="changeRoute()"
            ></v-select>
          </v-col>
          <div class="top-item">
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
import axios from "axios";
// If you use the default popups, use this.
import "tui-date-picker/dist/tui-date-picker.css";
import "tui-time-picker/dist/tui-time-picker.css";
import { mapState } from "vuex";
import constants from "@/api/constants.js";

export default {
  name: "myCalendar",
  components: {
    calendar: Calendar
  },
  created() {
    this.getSchedule();
  },
  mounted() {
    this.setRenderRangeText(), this.setEventListener();
    this.calendarList.forEach(item => {
      this.workList.push(item.id);
    });
  },
  computed: {
    ...mapState(["userToken"]),
    scheduleList() {
      if (this.isCheckAll == true) {
        return this.schedule;
      } else {
        return this.schedule.filter(item => {
          return this.workList.indexOf(item.calendarId) != -1;
        });
      }
      return [];
    }
  },
  watch: {},
  data() {
    return {
      constants,
      modeSelect: ["month", "week", "day"],
      modetoggle: ["toggle-monthly", "toggle-weekly", "toggle-daily"],
      selected: "month",
      isCheckAll: true,
      workList: [],
      color: [
        "#1F85DE",
        "#4BDEBD",
        "#DE4B6C",
        "#159A5D",
        "#AA1A45",
        "#DE781F",
        "#651AAA",
        "#F6F64F"
      ],
      fontColor: [
        "#ffffff",
        "#000000",
        "#ffffff",
        "#ffffff",
        "#ffffff",
        "#ffffff",
        "#ffffff",
        "#000000"
      ],
      calen: [],
      calendarList: [],
      schedule: [],
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
    async getSchedule() {
      const Token = "Bearer " + this.userToken;
      await axios
        .get(`${this.constants.API_URL}trainer/schedule/`, {
          headers: {
            Authorization: Token
          }
        })
        .then(res => {
          res.data.forEach(item => {
            if (this.calen.indexOf(item.clientname) == -1) {
              this.calen.push(item.clientname);
              this.calendarList.push({
                id: this.calendarList.length,
                name: item.clientname
              });
            }
            let ind = this.calen.indexOf(item.clientname);
            let new_obj = {};
            new_obj.calendarId = ind;
            new_obj.title = item.programname;
            new_obj.category = "time";
            new_obj.dueDateClass = "";
            new_obj.start = `${item.programday}T${item.start_hour}`;
            new_obj.end = `${item.programday}T${item.end_hour}`;
            this.schedule.push(new_obj);
          });
          this.schedule.forEach(item => {
            item.bgColor = this.color[Number(item.calendarId)];
            item.borderColor = this.color[Number(item.calendarId)];
            item.color = this.fontColor[Number(item.calendarId)];
          });
        });
    },
    changeRoute() {
      const index = this.modeSelect.indexOf(this.selected);
      const togglemenu = this.modetoggle[index];
      const options = this.$refs.tuiCalendar.invoke("getOptions");
      let viewName = "";
      switch (togglemenu) {
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
      }
      this.$refs.tuiCalendar.invoke("setOptions", (options, true));
      this.$refs.tuiCalendar.invoke("changeView", ("newViewName", viewName));
      this.setDropdownCalendarType();
      this.setRenderRangeText();
      this.setSchedules();
    },
    checkAll: function() {
      this.isCheckAll = !this.isCheckAll;
      this.workList = [];
      if (this.isCheckAll) {
        // Check all
        for (var key in this.calendarList) {
          this.workList.push(this.calendarList[key]);
        }
      }
    },
    updateCheckall: function() {
      if (this.workList.length == this.calendarList.length) {
        this.isCheckAll = true;
      } else {
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
      // var target = $(e.target).closest('a[role="menuitem"]')[0];
      console.log(target, "target입니다.");
      var action = this.getDataAction(target);
      var options = this.$refs.tuiCalendar.invoke("getOptions");
      var viewName = "";

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
      this.$refs.tuiCalendar.invoke("setOptions", (options, true));
      this.$refs.tuiCalendar.invoke("changeView", ("newViewName", viewName));
      this.setDropdownCalendarType();
      this.setRenderRangeText();
      this.setSchedules();
    },
    setSchedules() {
      this.$refs.tuiCalendar.invoke("clear");
      this.scheduleList.forEach(item => {
        this.$refs.tuiCalendar.invoke("createSchedules", [item]);
      });
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
      calendarTypeName.innerHTML = type;
    },
    setEventListener() {
      $('.dropdown-menu a[role="menuitem"]').on("click", this.onClickMenu);
      $("#lnb-calendars").on("change", this.onChangeCalendars);
    }
  }
};
</script>

<style scoped>
.client {
  border: solid 2px rgba(122, 122, 122, 0.2);
}

.client h2 {
  margin-bottom: 15px;
}

.calendarItemList-title {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 16px;
}

.calendarItemList-title input {
  margin-right: 8px;
}

.program-list-item {
  width: 150px;
  border-radius: 20px;
  font-size: 18px;
  background-color: #aaaaaa;
  margin: 0px auto 12px;
  position: relative;
}

.program-list-item input {
  position: absolute;
  top: 7px;
  left: 18px;
  margin-right: 4px;
  background-color: #aaaaaa;
}

.program-list-item span {
}

#menu {
  display: flex;
  height: 90px;
}

ul {
  padding: 4px 0px;
}

.dropdown {
  width: 100px;
}

.top-item {
  margin-top: 10px;
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
