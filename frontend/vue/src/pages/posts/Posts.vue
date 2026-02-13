<template>
  <Header />

  <h1>Posts</h1>

  <div v-for="value in posts" :key="value.id">
    <p>post title: {{ value.title }}</p>
    <p>user name: {{ value.author.name }}</p>

    <!-- КАРТИНКА -->
    <img
      v-if="value.file_path"
      :src="'http://localhost:8000' + value.file_path"
      style="max-width: 300px"
    />

    <br>

    <RouterLink :to="`/posts/${value.id}`">Open post</RouterLink>
    <hr>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue';
import api from '@/api/api';
import { onMounted, ref } from 'vue';

const posts = ref([]);

onMounted(async () => {
  const res = await api.get("/posts");
  posts.value = res.data;
});
</script>
