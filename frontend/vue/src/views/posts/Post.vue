<template>
<h1>Post</h1>
  <div v-if="post" style="padding: 10px;">
    <p>author: {{ post.author.name }} <br> name: {{ post.name }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const post_id = route.params.id;

const post = ref(null);


async function loadPost() {
  try {
    const res = await fetch(`http://localhost:8000/posts/${post_id}`);
    post.value = await res.json();
  } 
  catch (error) {
    console.log("Error", error);
  }
}

onMounted(loadPost);
</script>
