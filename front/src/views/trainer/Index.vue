
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'TrainerDetail',

    metaInfo: { title: 'TrainerDetail' },

    extends: View,

    mixins: [
      LoadSections([
        'TrainerDetail',
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'TrainerDetail',
      },
    },
  }
</script>
