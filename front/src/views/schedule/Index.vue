
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'Schedule',

    metaInfo: { title: 'Schedule' },

    extends: View,

    mixins: [
      LoadSections([
        'Schedule',
        
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'home',
      },
    },
  }
</script>
