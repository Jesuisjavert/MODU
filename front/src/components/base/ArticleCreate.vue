<template>
  <div>
    <!-- <v-responsive
      class="mx-auto"
      max-width="1280"
    >
      <editor
        ref="toastuiEditor"
        :inital-value="Text"
        :options="editorOptions"
      />
    </v-responsive> -->

    <editor
      ref="toastuiEditor"
      :inital-value="Text"
      :options="editorOptions"
      height="600px"
    />
    <!-- <button @click="createAction">
      이때 내용 저장하게끔 하는 함수를 만들어야함
    </button> -->
    <!-- <v-btn
      dark
      text
      @click="createArticle"
    >
      Save
    </v-btn> -->
    <v-container class="text-center">
      <router-link to="/community">
        저장하기
      </router-link>
    </v-container>
    <!-- 여기에 라우터링크가 들어갈게 아니라 함수가 들어가서 데이터를 옮기는것, 링크 옮기는것 동시에 작업되야함 -->
    <!-- <viewer
      :initial-value="viewerText"
      height="500px"
    /> -->
  </div>
</template>

<script>
 // import axios from 'axios'

  const API_URL = 'http://localhost:4000'
  import 'codemirror/lib/codemirror.css'
  import '@toast-ui/editor/dist/toastui-editor.css'
  // eslint-disable-next-line no-unused-vars
  import { Editor, Viewer } from '@toast-ui/vue-editor'

  import '@toast-ui/editor/dist/toastui-editor-viewer.css'

  export default {
    name: 'ArticleCreate',

    components: {
      editor: Editor,
    },
    data () {
      return {
        Text: 'text',
        editorOptions: {
          minHeight: '500px',
          language: 'en-US',
          useCommandShortcut: true,
          useDefaultHTMLSanitizer: true,
          usageStatistics: true,
          hideModeSwitch: false,
          toolbarItems: [
            'heading',
            'bold',
            'italic',
            'strike',
            'divider',
            'hr',
            'quote',
            'divider',
            'ul',
            'ol',
            'task',
            'indent',
            'outdent',
            'divider',
            'table',
            'image',
            'link',
            'divider',
            'code',
            'codeblock',
          ],
        },
        viewerText: '### 안녕',
      }
    },
    methods: {
      createAction () {
        var content = this.$refs.toastuiEditor.invoke('getMarkdown')
      },
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
