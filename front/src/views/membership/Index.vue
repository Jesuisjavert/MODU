
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'Membership',

    metaInfo: { title: 'Membership' },

    extends: View,

    mixins: [
      LoadSections([
        'Membership',
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'Membership',
      },
    },
  }
</script>
