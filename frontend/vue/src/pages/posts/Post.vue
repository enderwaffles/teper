<template>
  <Header />

  <h1>Post</h1>

  <div v-if="post">

    <p>post title: {{ post.title }}</p>
    <p>post text: {{ post.text }}</p>
    <p>user name: {{ post.author?.name }}</p>

    <img
      v-if="post.upload_url"
      :src="'http://localhost:8000' + post.upload_url"
      style="max-width: 400px"
    />

    <br>
    <div v-if="auth.user.id == post.author.id">
      <button type="button" @click="delete_post">Delete</button>
    </div>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue';
import api from '@/api/api';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const route = useRoute();
const router = useRouter();
const auth = useAuthStore()


const post = ref(null);
const post_id = route.params.id;

onMounted(async () => {
  const res = await api.get(`/posts/${post_id}`);
  post.value = res.data;
});

async function delete_post() {
  await api.delete(`/posts/${post_id}`);
  router.push("/posts");
}
</script>
