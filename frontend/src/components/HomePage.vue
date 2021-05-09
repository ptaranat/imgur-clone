<template>
  <div>
    <div class="container pt-4">
      <div class="row">
        <div v-for="image in latest" v-bind:key="image" class="col-lg-4">
          <!-- <ImageCard :img="image" /> -->
          <ImageCard
            v-bind:img="
              'https://dev-image-repo-bucket.s3.us-east-2.amazonaws.com/' +
              image
            "
            alt=""
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ImageCard from "./ImageCard.vue";

export default {
  name: "HomePage",
  components: {
    ImageCard,
  },
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
  background-color: #1c1f22;
}
</style>