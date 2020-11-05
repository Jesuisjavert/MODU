
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'About',

    metaInfo: { title: 'About' },

    extends: View,

    mixins: [
      LoadSections([
        'Aboutus',
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'aboutus',
      },
    },
  }
</script>
