
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'ProgramDetail',

    metaInfo: { title: 'ProgramDetail' },

    extends: View,

    mixins: [
      LoadSections([
        'ProgramDetail',
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'ProgramDetail',
      },
    },
  }
</script>
