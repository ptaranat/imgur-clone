<template>
  <div class="card bg-dark text-white mb-4">
    <img class="card-img-top" :src="img" alt="" />
    <div class="card-body">
      <h5 class="card-title">{{ img }}</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImageCard",
  props: ["img"],
};
</script>

<style>
</style>