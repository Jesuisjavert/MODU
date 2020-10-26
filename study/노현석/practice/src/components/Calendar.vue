<template>
    <div>
        <div id="calendar" style="height: 100px;"></div>
    </div>
</template>

<script>
import Calendar from 'tui-calendar';
import 'tui-calendar/dist/tui-calendar.css';
import 'tui-date-picker/dist/tui-date-picker.css';
import 'tui-time-picker/dist/tui-time-picker.css';

const calendar = new Calendar('#calendar', {
  defaultView: 'week',
  useCreationPopup: true,
  useDetailPopup: true
});

calendar.render();

export default {
    
}
</script>