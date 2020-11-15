
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
        'SiteFeat',
        'feature2',
        'info',
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
