<template>
  <div>
    <h1>Posts</h1>

      <div v-for="post in posts" :key="post.id" style="padding: 10px;">
         
        <router-link :to="`/posts/${ post.id }`"> author: {{ post.author.name }} <br> post: {{ post.name }} </router-link>
      </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const posts = ref([]);

async function loadPosts() {
  try {
    const res = await fetch("http://localhost:8000/posts/");
    posts.value = await res.json();
  } 
  catch (error) {
    console.log("Error", error);
  }
}

onMounted(loadPosts);
</script>