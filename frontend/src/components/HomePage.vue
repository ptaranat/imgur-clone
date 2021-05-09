<template>
  <div>
    <b-container class="container pt-4">
      <b-row>
        <b-card-group
          deck
          v-for="(image, index) in latest"
          :key="index"
          class="col-lg-4"
        >
          <b-card
            v-bind:title="image"
            v-bind:img-src="
              'https://dev-image-repo-bucket.s3.us-east-2.amazonaws.com/' +
              image
            "
            img-top
            img-alt=""
            bg-variant="dark"
            text-variant="white"
            class="image-card mb-4"
          >
            <b-card-text>asdf</b-card-text>
            <b-card-text class="small text-muted"
              >Last updated 3 mins ago</b-card-text
            >
          </b-card>
        </b-card-group>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomePage",
  data() {
    return {
      latest: [],
    };
  },
  created() {
    axios
      .get("https://75v2tuitm6.execute-api.us-east-2.amazonaws.com/dev/list")
      .then((response) => {
        console.log(response);
        this.latest = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
body {
  background-color: #1c1f22 !important;
}
.image-card {
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.4);
}
</style>