<template>
  <v-container
    id="contact"
    class="pa-0 grey lighten-3 flex-wrap align-start fill-height"
    fluid
    tag="section"
  >
    <iframe
      allowfullscreen
      frameborder="0"
      height="500"
      src="https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=Gwangju+(Apolio)&amp;t=&amp;z=7&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"
      style="border:0"
      width="100%"
    />

    <v-row
      class="ma-0"
      justify="center"
    >
      <v-col
        cols="12"
        md="4"
      >
        <h1 class="display-1 mb-8 font-weight-bold">
          Contact Info:
        </h1>

        <div class="mb-8">
          광주광역시 광산구 비아동 삼성 사업장
        </div>

        <div class="mb-4">
          <strong>Address</strong> 광주 광산구 하남산단6번로 107
        </div>

        <div class="mb-4">
          <strong>Name</strong>: 강 동 훈 ( Kang Donghoon )
        </div>

        <div class="mb-4">
          <strong>Phone</strong> +82) 10 - 4873 - 3847
        </div>

        <div class="mb-4">
          <strong>Email</strong> jesuisjavert@gmail.com
        </div>

        <div class="mb-4">
          <strong>Company</strong> Samsung Software Academy For Youth
        </div>
      </v-col>

      <v-col
        cols="12"
        md="5"
      >
        <v-form>
          <v-row class="mb-6">
            <v-col
              cols="12"
              md="6"
            >
              <v-sheet>
                <v-text-field
                  flat
                  hide-details
                  label="Your Name"
                  solo
                />
              </v-sheet>
            </v-col>

            <v-col
              cols="12"
              md="6"
            >
              <v-sheet>
                <v-text-field
                  flat
                  hide-details
                  label="Your Email"
                  solo
                />
              </v-sheet>
            </v-col>

            <v-col cols="12">
              <v-sheet>
                <v-text-field
                  flat
                  hide-details
                  label="Your Title"
                  solo
                />
              </v-sheet>
            </v-col>

            <v-col cols="12">
              <v-sheet>
                <v-textarea
                  flat
                  hide-details
                  label="Your Message"
                  solo
                />
              </v-sheet>
            </v-col>
          </v-row>

          <v-btn
            :block="$vuetify.breakpoint.smAndDown"
            class="white--text"
            color="black"
            x-large
          >
            Send Message
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'Contact',
  }
</script>
