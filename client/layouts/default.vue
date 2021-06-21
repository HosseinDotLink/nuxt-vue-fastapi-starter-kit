<template>
  <v-app>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <v-btn icon @click.prevent="logout">
        <v-text style="color: red; font-size: 24px">⏼</v-text>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <v-footer :absolute="!fixed" app>
      <span>&copy; {{ new Date().getFullYear() }} | Hossein MohammadiPour</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      fixed: false,
      title: "Weather app that save your name and location",
    };
  },
  methods: {
    logout() {
      this.$cookiz.removeAll();
      this.$router.push("/");
    },
  },
};
</script>
