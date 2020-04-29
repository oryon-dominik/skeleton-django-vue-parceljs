<template>
  <div id="container" class="container">
    <img alt="Vue logo" src="./assets/images/logo.png">
    <div class="message">{{msg}}</div>
    <Hello msg="Welcome to a Vue.js App powered by parceljs"></Hello>
  </div>
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
  width: 100%;
  text-align: center;
}
</style>
