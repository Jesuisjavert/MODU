
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'ProgramApply',

    metaInfo: { title: 'ProgramApply' },

    extends: View,

    mixins: [
      LoadSections([
        'ProgramApply',
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'ProgramApply',
      },
    },
  }
</script>
