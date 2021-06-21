<template>
  <v-row>
    <v-col class="text-center">
      <h1>Welcome {{ name }}</h1>
      <v-card class="mx-auto" max-width="400">
        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title class="text-h5">
              {{ weather.location }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-card-text>
          <v-row align="center">
            <v-col class="text-h3" cols="6"
              >{{ weather.today.temp }}&deg;C
            </v-col>
            <v-col cols="6">
              <v-img
                :src="weather.today.icon"
                alt="Weather image"
                width="92"
              ></v-img>
            </v-col>
          </v-row>
        </v-card-text>

        <v-list class="transparent">
          <v-list-item>
            <v-list-item-title class="text-left">Tomorrow</v-list-item-title>

            <v-list-item-icon>
              <v-img :src="weather.tomorrow.icon" alt="Sunny image"></v-img>
            </v-list-item-icon>

            <v-list-item-subtitle class="text-right">
              {{ weather.tomorrow.temp }}
            </v-list-item-subtitle>
          </v-list-item>
        </v-list>

        <v-list class="transparent">
          <v-list-item>
            <v-list-item-title class="text-left"
              >The day after tomorrow</v-list-item-title
            >

            <v-list-item-icon>
              <v-img
                :src="weather['the day after tomorrow'].icon"
                alt="Sunny image"
              ></v-img>
            </v-list-item-icon>

            <v-list-item-subtitle class="text-right">
              {{ weather["the day after tomorrow"].temp }}
            </v-list-item-subtitle>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>
export default {
  data: () => ({
    name: "",
    city: "",
    weather: {
      location: "",
      today: {},
      tomorrow: {},
      "the day after tomorrow": {},
    },
  }),

  mounted() {
    this.name = this.$route.query.name;
    this.city = this.$route.query.city;
  },
  async fetch() {
    let query = "";
    if (this.$route.query.name) {
      query += "name=" + this.$route.query.name;
    }
    if (this.$route.query.city) {
      query += "&city=" + this.$route.query.city;
    }
    this.weather = await fetch(
      "http://127.0.0.1:8000/api/weather?" + query
    ).then((res) => res.json());
  },
};
</script>

