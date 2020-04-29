<template>

    <v-app>
      <div id="container" class="container">
        <img alt="Vue logo" src="./assets/images/logo.png">
        <div class="message">{{msg}}</div>
        <Hello msg="Welcome to a Vue.js App powered by parceljs"></Hello>
      </div>

      <v-app-bar app color="secondary" dark>
        <div class="d-flex align-center">
          <p>This is a vuetify component</p>
        </div>
        <v-spacer></v-spacer>
        <v-btn href="#" target="_blank" text>
          <span class="mr-2">Link</span>
          <v-icon>mdi-open-in-new</v-icon>
        </v-btn>
      </v-app-bar>
    </v-app>

</template>

<script lang="ts">
import Vue from "vue";
import Hello from './components/Hello.vue'

export default Vue.extend({
  name: 'App',
  components: {
    Hello
  },
  data() {
    return {
      msg: "ParcelJS-Application"
    };
  }
});
</script>

<style lang="scss" scoped>
.message {
  color: green;
}
.container {
  padding-top: 8rem;
  width: 100%;
  text-align: center;
}
</style>
