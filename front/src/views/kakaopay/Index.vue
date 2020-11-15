
<script>
  import View from '@/views/View'
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'KakaopayApprove',

    metaInfo: { title: 'KakaopayApprove' },

    extends: View,

    mixins: [
      LoadSections([
        'KakaopayApprove',
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'KakaopayApprove',
      },
    },
  }
</script>
