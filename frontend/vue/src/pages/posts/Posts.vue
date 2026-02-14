<template>
  <Header />
  <h1>Posts</h1>
  <div v-for="value in posts" :key="value.id">

    <p>post title: {{ value.title }}</p>
    <p>post text: {{ value.text }}</p>
    <p>user name: {{ value.author.name }}</p>

    <img
      v-if="value.upload_url"
      :src="api.defaults.baseURL + value.upload_url"
      style="max-width: 300px"  
    />
    <br>
    <RouterLink :to="`/posts/${value.id}`">Open post</RouterLink> <hr>
  </div>
  <div v-if="posts.length == 0">
    <p>No post</p>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { onMounted, ref } from 'vue'

const posts = ref([])
console.log("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
console.log(api)
onMounted(async () => {

  const res = await api.get("/posts");
  posts.value = res.data;
  
});

</script>

<style scoped>

</style>
