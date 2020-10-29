
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'Mypage',

    metaInfo: { title: 'Mypage' },

    extends: View,

    mixins: [
      LoadSections([
        'Mypage',
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'Mypage',
      },
    },
  }
</script>
