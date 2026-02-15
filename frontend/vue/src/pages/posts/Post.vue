<template>
  <Header />

  <h1>Post</h1>

  <div v-if="post">

    <p>post title: {{ post.title }}</p>
    <p>post text: {{ post.text }}</p>
    <p>user name: {{ post.author?.name }}</p>

    <img
      v-if="post.upload_url"
      :src="api.defaults.baseURL + post.upload_url"
      style="max-width: 400px"
    />

    <br>

    <div v-if="auth.user.id == post.author.id">
      <button type="button" @click="delete_post()">Delete</button>
      <RouterLink :to="`/update_post/${post_id}`">Update</RouterLink>
    </div>

    <hr>
    
    <p>comments: </p>

    <div v-for="value in post.comments">
      <p>author name: {{ value.author.name }}</p>
      <p>comment text: {{ value.text }}</p>
      <button type="button" v-if="auth.user.id == value.author.id" v-on:click="delete_comment(value.id)">Delete</button>
    </div>
    
    <hr>
    <div v-if="auth.user">
      <p>write comment: </p>  
      <p>{{ auth.user.name }}</p>
      <input type="text" v-model="comment" placeholder="comment">
      <button type="button" v-on:click="send_comment()">send</button>
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


const post = ref(null)
const post_id = route.params.id

const comment = ref("")

onMounted(async () => {
  const res = await api.get(`/posts/${post_id}`)
  post.value = res.data
  
});

async function delete_post() {
  await api.delete(`/posts/${post_id}`)
  router.push('/posts')

}

// comments
async function send_comment() {
  const form = new FormData()
  form.append("text", comment.value)
  const res = await api.post(`/posts/comments/${post_id}`, form)
  post.value.comments.push(res.data) // 👈 добавили сразу в список
  comment.value = "" // очистить input
}

async function delete_comment(id) {
  await api.delete(`/posts/comments/${id}`)
  post.value.comments = post.value.comments.filter(
    comment => comment.id !== id
  )

}

</script>

<style scoped>

</style>
