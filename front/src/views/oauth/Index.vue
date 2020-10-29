
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'Oauth',

    metaInfo: { title: 'Oauth' },

    extends: View,

    mixins: [
      LoadSections([
        'Oauth',
      ]),
    ],
  }
</script>
